'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: acs_server.py
@time: 2025/12/15 11:04
@desc: 
'''

from flask import Flask, url_for, request, redirect, make_response
from flask import render_template
from flask import Flask

from flask import Flask, request, jsonify, abort
from urllib.parse import urlparse, parse_qs
import re

app = Flask(__name__)

'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: acs_server.py
@time: 2025/12/15 11:04
@desc: TR-069 ACS服务器 - 无认证版本
'''

from flask import Flask, request, make_response, jsonify
import xml.etree.ElementTree as ET
import uuid
import re
import json
from datetime import datetime

app = Flask(__name__)

# 模拟数据库存储设备信息
devices_db = {}


def parse_cwmp_xml(xml_data):
    """解析CWMP XML数据"""
    try:
        # 移除命名空间简化解析
        xml_data = re.sub(r'xmlns[^=]*="[^"]*"', '', xml_data)

        root = ET.fromstring(xml_data)

        # 获取SOAP头部信息
        header = root.find('.//Header')
        id_elem = header.find('ID') if header is not None else None
        message_id = id_elem.text if id_elem is not None else None

        # 获取SOAP Body
        body = root.find('.//Body')

        if body is not None:
            # 检查消息类型
            if body.find('Inform') is not None:
                return {
                    'type': 'Inform',
                    'id': message_id,
                    'body': parse_inform_message(body.find('Inform'))
                }
            elif body.find('DownloadResponse') is not None:
                return {
                    'type': 'DownloadResponse',
                    'id': message_id,
                    'body': parse_download_response(body.find('DownloadResponse'))
                }
            elif body.find('TransferComplete') is not None:
                return {
                    'type': 'TransferComplete',
                    'id': message_id,
                    'body': parse_transfer_complete(body.find('TransferComplete'))
                }
            elif body.find('GetRPCMethods') is not None:
                return {
                    'type': 'GetRPCMethods',
                    'id': message_id,
                    'body': {}
                }
            elif body.find('GetParameterValues') is not None:
                return {
                    'type': 'GetParameterValues',
                    'id': message_id,
                    'body': parse_get_parameter_values(body.find('GetParameterValues'))
                }
            elif body.find('SetParameterValues') is not None:
                return {
                    'type': 'SetParameterValues',
                    'id': message_id,
                    'body': parse_set_parameter_values(body.find('SetParameterValues'))
                }
            elif body.find('GetParameterNames') is not None:
                return {
                    'type': 'GetParameterNames',
                    'id': message_id,
                    'body': parse_get_parameter_names(body.find('GetParameterNames'))
                }

        return {'type': 'unknown', 'id': message_id, 'body': {}}

    except Exception as e:
        print(f"Error parsing XML: {e}")
        return {'type': 'error', 'id': None, 'body': {}}


def parse_inform_message(inform_elem):
    """解析Inform消息"""
    device_info = {}

    # 解析设备ID
    device_id = inform_elem.find('DeviceId')
    if device_id is not None:
        device_info['manufacturer'] = get_element_text(device_id.find('Manufacturer'))
        device_info['oui'] = get_element_text(device_id.find('OUI'))
        device_info['product_class'] = get_element_text(device_id.find('ProductClass'))
        device_info['serial_number'] = get_element_text(device_id.find('SerialNumber'))

    # 解析事件
    events = []
    event_list = inform_elem.find('Event')
    if event_list is not None:
        for event_struct in event_list.findall('EventStruct'):
            event_code = get_element_text(event_struct.find('EventCode'))
            command_key = get_element_text(event_struct.find('CommandKey'))
            events.append({
                'event_code': event_code,
                'command_key': command_key
            })
    print("event_code = ", event_code)
    # 解析参数列表
    parameters = {}
    param_list = inform_elem.find('ParameterList')
    if param_list is not None:
        for param_struct in param_list.findall('ParameterValueStruct'):
            name = get_element_text(param_struct.find('Name'))
            value_elem = param_struct.find('Value')
            if value_elem is not None:
                # 获取值的类型和内容
                value_type = value_elem.get('{http://www.w3.org/2001/XMLSchema-instance}type')
                value = value_elem.text or ""
                parameters[name] = {
                    'value': value,
                    'type': value_type
                }

    device_info['events'] = events
    device_info['parameters'] = parameters
    device_info['max_envelopes'] = get_element_text(inform_elem.find('MaxEnvelopes'))
    device_info['current_time'] = get_element_text(inform_elem.find('CurrentTime'))
    device_info['retry_count'] = get_element_text(inform_elem.find('RetryCount'))

    return device_info


def parse_download_response(download_response_elem):
    """解析Download响应"""
    return {
        'status': get_element_text(download_response_elem.find('Status')),
        'start_time': get_element_text(download_response_elem.find('StartTime')),
        'complete_time': get_element_text(download_response_elem.find('CompleteTime'))
    }


def parse_transfer_complete(transfer_complete_elem):
    """解析TransferComplete消息"""
    return {
        'command_key': get_element_text(transfer_complete_elem.find('CommandKey')),
        'fault_struct': parse_fault_struct(transfer_complete_elem.find('FaultStruct')),
        'start_time': get_element_text(transfer_complete_elem.find('StartTime')),
        'complete_time': get_element_text(transfer_complete_elem.find('CompleteTime'))
    }


def parse_get_parameter_values(get_param_elem):
    """解析GetParameterValues消息"""
    parameter_names = []
    param_names = get_param_elem.find('ParameterNames')
    if param_names is not None:
        for name in param_names.findall('string'):
            parameter_names.append(name.text)

    return {'parameter_names': parameter_names}


def parse_set_parameter_values(set_param_elem):
    """解析SetParameterValues消息"""
    parameters = {}
    param_list = set_param_elem.find('ParameterList')
    if param_list is not None:
        for param_struct in param_list.findall('ParameterValueStruct'):
            name = get_element_text(param_struct.find('Name'))
            value_elem = param_struct.find('Value')
            if value_elem is not None:
                value_type = value_elem.get('{http://www.w3.org/2001/XMLSchema-instance}type')
                value = value_elem.text or ""
                parameters[name] = {
                    'value': value,
                    'type': value_type
                }

    return {
        'parameters': parameters,
        'parameter_key': get_element_text(set_param_elem.find('ParameterKey'))
    }


def parse_get_parameter_names(get_param_names_elem):
    """解析GetParameterNames消息"""
    return {
        'parameter_path': get_element_text(get_param_names_elem.find('ParameterPath')),
        'next_level': get_element_text(get_param_names_elem.find('NextLevel'))
    }


def parse_fault_struct(fault_struct_elem):
    """解析故障结构"""
    if fault_struct_elem is None:
        return None

    return {
        'fault_code': get_element_text(fault_struct_elem.find('FaultCode')),
        'fault_string': get_element_text(fault_struct_elem.find('FaultString'))
    }


def get_element_text(elem):
    """安全获取元素文本"""
    return elem.text if elem is not None else ""


def create_soap_envelope(message_id, body_content, no_more_requests=0):
    """创建SOAP信封响应"""
    envelope = f'''<?xml version="1.0" encoding="UTF-8"?>
<soap-env:Envelope 
    xmlns:cwmp="urn:dslforum-org:cwmp-1-0"
    xmlns:soap-enc="http://schemas.xmlsoap.org/soap/encoding/"
    xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <soap-env:Header>
        <cwmp:ID soap-env:mustUnderstand="1">{message_id}</cwmp:ID>
        <cwmp:NoMoreRequests>{no_more_requests}</cwmp:NoMoreRequests>
    </soap-env:Header>
    <soap-env:Body>
        {body_content}
    </soap-env:Body>
</soap-env:Envelope>'''

    return envelope


def create_inform_response(max_envelopes=1):
    """创建Inform响应"""
    return f'''<cwmp:InformResponse>
    <MaxEnvelopes>{max_envelopes}</MaxEnvelopes>
</cwmp:InformResponse>'''


def create_download_command(command_key, firmware_info):
    """创建Download命令"""
    return f'''<cwmp:Download>
    <CommandKey>{command_key}</CommandKey>
    <FileType>1 Firmware Upgrade Image</FileType>
    <URL>{firmware_info['url']}</URL>
    <Username>{firmware_info.get('username', 'cpe')}</Username>
    <Password>{firmware_info.get('password', 'cpe')}</Password>
    <FileSize>{firmware_info['size']}</FileSize>
    <TargetFileName>{firmware_info['filename']}</TargetFileName>
    <DelaySeconds>{firmware_info.get('delay', 0)}</DelaySeconds>
    <SuccessURL>{firmware_info.get('success_url', '')}</SuccessURL>
    <FailureURL>{firmware_info.get('failure_url', '')}</FailureURL>
    <UpgradeControl>{firmware_info.get('upgrade_control', 1)}</UpgradeControl>
</cwmp:Download>'''


def create_empty_response():
    """创建空响应"""
    return "<cwmp:Empty/>"


def create_get_rpc_methods_response():
    """创建GetRPCMethods响应"""
    return '''<cwmp:GetRPCMethodsResponse>
    <MethodList>
        <string>Inform</string>
        <string>GetRPCMethods</string>
        <string>SetParameterValues</string>
        <string>GetParameterValues</string>
        <string>GetParameterNames</string>
        <string>SetParameterAttributes</string>
        <string>GetParameterAttributes</string>
        <string>AddObject</string>
        <string>DeleteObject</string>
        <string>Reboot</string>
        <string>Download</string>
        <string>Upload</string>
    </MethodList>
</cwmp:GetRPCMethodsResponse>'''


def create_get_parameter_values_response(parameters):
    """创建GetParameterValues响应"""
    param_list_xml = ""
    for name, value_info in parameters.items():
        param_list_xml += f'''
        <ParameterValueStruct>
            <Name>{name}</Name>
            <Value xsi:type="{value_info.get('type', 'xsd:string')}">{value_info['value']}</Value>
        </ParameterValueStruct>'''

    return f'''<cwmp:GetParameterValuesResponse>
    <ParameterList soap-enc:arrayType="cwmp:ParameterValueStruct[{len(parameters)}]">{param_list_xml}
    </ParameterList>
</cwmp:GetParameterValuesResponse>'''


def create_set_parameter_values_response(status=0):
    """创建SetParameterValues响应"""
    return f'''<cwmp:SetParameterValuesResponse>
    <Status>{status}</Status>
</cwmp:SetParameterValuesResponse>'''


def create_fault_response(fault_code=9000, fault_string="Internal Error"):
    """创建Fault响应"""
    return f'''<soap-env:Fault>
    <faultcode>Client</faultcode>
    <faultstring>CWMP fault</faultstring>
    <detail>
        <cwmp:Fault>
            <FaultCode>{fault_code}</FaultCode>
            <FaultString>{fault_string}</FaultString>
        </cwmp:Fault>
    </detail>
</soap-env:Fault>'''


# 主路由处理 - 无认证版本
@app.route('/RMS-server/RMS', methods=['POST'])
@app.route('/web/tr069', methods=['POST'])  # 保留原路由
def rms_endpoint():
    """处理TR-069 RMS请求 - 无认证版本"""

    # 获取SN参数
    sn = request.args.get('sn')

    if not sn:
        return make_response("Missing SN parameter", 400)

    # 记录请求信息
    print(f"\n=== Received TR-069 Request ===")
    print(f"SN: {sn}")
    print(f"Headers: {dict(request.headers)}")
    print(f"Content-Length: {request.headers.get('Content-Length')}")

    # 检查是否有请求体
    content_length = int(request.headers.get('Content-Length', 0))

    if content_length == 0:
        # 空请求体，发送固件下载命令
        print("Empty request body - sending download command")
        return handle_empty_request(sn)

    # 解析XML请求
    xml_data = request.data.decode('utf-8', errors='ignore')
    print(f"XML data length: {len(xml_data)}")
    if len(xml_data) > 500:
        print(f"XML preview: {xml_data[:500]}...")
    else:
        print(f"XML data: {xml_data}")

    # 解析CWMP消息
    cwmp_msg = parse_cwmp_xml(xml_data)
    msg_type = cwmp_msg['type']
    msg_id = cwmp_msg['id'] or str(uuid.uuid4())

    print(f"Parsed message - Type: {msg_type}, ID: {msg_id}")

    # 根据消息类型处理
    if msg_type == 'Inform':
        print("Processing Inform message")

        # 处理Inform消息
        device_info = cwmp_msg['body']
        device_info['sn'] = sn
        device_info['last_seen'] = datetime.now().isoformat()
        device_info['remote_addr'] = request.remote_addr

        # 保存设备信息到数据库
        devices_db[sn] = device_info

        print(f"Device registered: SN={sn}, Manufacturer={device_info.get('manufacturer')}")

        # 创建Inform响应
        soap_response = create_soap_envelope(
            msg_id,
            create_inform_response(),
            no_more_requests=0
        )

        response = make_response(soap_response, 200)

    elif msg_type == 'DownloadResponse':
        print("Processing DownloadResponse message")

        # 处理Download响应
        download_info = cwmp_msg['body']
        print(f"Download response received - Status: {download_info.get('status')}")

        # 创建空响应（204 No Content）
        soap_response = create_soap_envelope(
            msg_id,
            create_empty_response(),
            no_more_requests=1
        )

        response = make_response(soap_response, 204)

    elif msg_type == 'TransferComplete':
        print("Processing TransferComplete message")

        # 处理TransferComplete消息
        transfer_info = cwmp_msg['body']
        print(f"Transfer complete - CommandKey: {transfer_info.get('command_key')}")

        soap_response = create_soap_envelope(
            msg_id,
            create_empty_response(),
            no_more_requests=1
        )

        response = make_response(soap_response, 200)

    elif msg_type == 'GetRPCMethods':
        print("Processing GetRPCMethods message")

        # 返回支持的RPC方法
        soap_response = create_soap_envelope(
            msg_id,
            create_get_rpc_methods_response(),
            no_more_requests=0
        )

        response = make_response(soap_response, 200)

    elif msg_type == 'GetParameterValues':
        print("Processing GetParameterValues message")

        # 返回参数值
        param_info = cwmp_msg['body']
        parameters = {}

        # 从设备信息中获取参数值（这里简化处理）
        device = devices_db.get(sn, {})
        device_params = device.get('parameters', {})

        for param_name in param_info.get('parameter_names', []):
            if param_name in device_params:
                parameters[param_name] = device_params[param_name]
            else:
                # 返回默认值
                parameters[param_name] = {
                    'value': '',
                    'type': 'xsd:string'
                }

        soap_response = create_soap_envelope(
            msg_id,
            create_get_parameter_values_response(parameters),
            no_more_requests=0
        )

        response = make_response(soap_response, 200)

    elif msg_type == 'SetParameterValues':
        print("Processing SetParameterValues message")

        # 处理设置参数值
        param_info = cwmp_msg['body']
        print(f"Setting parameters: {list(param_info.get('parameters', {}).keys())}")

        # 返回成功响应
        soap_response = create_soap_envelope(
            msg_id,
            create_set_parameter_values_response(0),  # 0表示成功
            no_more_requests=0
        )

        response = make_response(soap_response, 200)

    else:
        print(f"Unknown message type: {msg_type}")

        # 未知消息类型，返回错误响应
        soap_response = create_soap_envelope(
            msg_id,
            create_fault_response(9000, f"Unknown message type: {msg_type}"),
            no_more_requests=1
        )
        response = make_response(soap_response, 200)

    # 设置响应头
    response.headers['Content-Type'] = 'text/xml;charset=UTF-8'
    response.headers['SN'] = sn
    response.headers['Connection'] = 'keep-alive'

    print(f"Response status: {response.status_code}")
    print("=== Request Completed ===\n")

    return response


def handle_empty_request(sn):
    """处理空请求体的情况（发送固件下载命令）"""
    # 生成命令ID
    command_id = str(uuid.uuid4()).replace('-', '')

    # 固件下载信息（根据实际情况配置）
    firmware_info = {
        'url': 'http://10.0.1.147:8080/rms-acs/download?token=' + str(uuid.uuid4()),
        'filename': 'tiangong2_COGI.V1.0.0_a_V61451607.bin',
        'size': 54001664,
        'username': 'cpe',
        'password': 'cpe',
        'success_url': 'http://10.0.1.147:8080/rms-acs/download?token=0',
        'failure_url': 'http://10.0.1.147:8080/rms-acs/download?token=1',
        'delay': 0,
        'upgrade_control': 1
    }

    # 创建Download命令
    download_command = create_download_command(command_id, firmware_info)

    # 创建SOAP响应
    soap_response = create_soap_envelope(
        command_id,
        download_command,
        no_more_requests=0
    )

    response = make_response(soap_response, 200)
    response.headers['Content-Type'] = 'text/xml;charset=UTF-8'
    response.headers['SN'] = sn
    response.headers['Connection'] = 'keep-alive'

    print(f"Sent download command for SN: {sn}, CommandKey: {command_id}")

    return response


# 设备管理API
@app.route('/api/devices', methods=['GET'])
def get_devices():
    """获取所有设备信息"""
    return jsonify(devices_db)


@app.route('/api/device/<sn>', methods=['GET'])
def get_device(sn):
    """获取特定设备信息"""
    device = devices_db.get(sn)
    if device:
        return jsonify(device)
    return jsonify({"error": "Device not found"}), 404


@app.route('/api/firmware/upgrade', methods=['POST'])
def trigger_firmware_upgrade():
    """触发固件升级"""
    data = request.json
    sn = data.get('sn')

    if not sn or sn not in devices_db:
        return jsonify({"error": "Device not found"}), 404

    # 这里可以触发异步任务或直接响应
    return jsonify({
        "status": "success",
        "message": "Firmware upgrade triggered",
        "sn": sn
    })


@app.route('/health', methods=['GET'])
def health_check():
    """健康检查接口"""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "device_count": len(devices_db)
    })


if __name__ == '__main__':
    print("Starting TR-069 ACS Server (No Authentication)...")
    print("Server will listen on: http://0.0.0.0:9999")
    print("TR-069 endpoint: http://0.0.0.0:9999/RMS-server/RMS")
    print("TR-069 endpoint (alternative): http://0.0.0.0:9999/web/tr069")
    print("Health check: http://0.0.0.0:9999/health")
    print("Devices API: http://0.0.0.0:9999/api/devices")
    print("\nWaiting for TR-069 connections...")

    app.run(
        host='0.0.0.0',
        port=9999,
        debug=True,
        threaded=True  # 支持多线程处理
    )

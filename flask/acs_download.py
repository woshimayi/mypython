'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: acs_download.py
@time: 2025/12/15 13:57
@desc:  建议acs 服务器 模拟测试
'''
import inspect

'''
@author: caopeng
@desc: 极简TR-069服务器 - 只响应Inform消息
'''

from flask import Flask, request, make_response
from werkzeug.serving import WSGIRequestHandler
import uuid


def PP(message=""):
    """打印带行号和函数名的信息"""
    # 获取当前帧信息
    current_frame = inspect.currentframe()
    # 获取调用者的帧信息
    caller_frame = current_frame.f_back

    # 获取行号
    line_no = caller_frame.f_lineno
    # 获取函数名
    func_name = caller_frame.f_code.co_name
    # 获取文件名
    file_name = caller_frame.f_code.co_filename.split('/')[-1]  # 只取文件名

    print(f"[{file_name}:{line_no}] {func_name}(): {message}")

    # 清理引用
    del current_frame
    del caller_frame


app = Flask(__name__)

WSGIRequestHandler.protocol_version = "HTTP/1.1"


@app.route('/web/tr069', methods=['POST'])
def tr069_simple():
    """最简单的TR-069处理"""

    # 获取SN
    sn = request.args.get('sn', 'UNKNOWN')

    # 获取请求内容
    xml_data = request.data.decode('utf-8', errors='ignore')
    # print(xml_data)
    Content_Length = request.headers.get('Content-Length')
    print(f"Content-Length: {request.headers.get('Content-Length')}")

    # 检查是否是Inform
    if '0' == Content_Length:
        print(f"[{sn}] Received Inform message")
        PP()
        status = 200

        # 创建下载命令响应
        command_id = str(uuid.uuid4()).replace('-', '')
        response_xml = f'''
<soap-env:Envelope xmlns:cwmp="urn:dslforum-org:cwmp-1-0" xmlns:soap-enc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<soap-env:Header>
<cwmp:ID soap-env:mustUnderstand="1">{command_id}</cwmp:ID>
<cwmp:NoMoreRequests>0</cwmp:NoMoreRequests>
</soap-env:Header>
<soap-env:Body>
<cwmp:Download>
<CommandKey>{command_id}</CommandKey>
<FileType>1 Firmware Upgrade Image</FileType>
<URL>http://172.16.27.192:8080/tiangong2_multi_upg.bin</URL>
<Username>cpe</Username>
<Password>cpe</Password>
<FileSize>54001664</FileSize>
<TargetFileName>tiangong2_multi_upg.bin</TargetFileName>
<DelaySeconds>0</DelaySeconds>
<SuccessURL>http://172.16.27.192:8080/tiangong2_multi_upg.bin</SuccessURL>
<FailureURL>http://172.16.27.192:8080/tiangong2_multi_upg.bin</FailureURL>
<UpgradeControl>1</UpgradeControl>
</cwmp:Download>
</soap-env:Body>
</soap-env:Envelope>'''
    elif "FaultCode" in xml_data:
        PP()
        response_xml = ''
        status = 204
    elif '<EventCode>2 PERIODIC</EventCode>' in xml_data:
        PP()
        print(f"[{sn}] Received non-Inform message")
        status = 200
        # 对于非Inform消息，返回简单的InformResponse
        response_xml = '''<soap-env:Envelope xmlns:cwmp="urn:dslforum-org:cwmp-1-0" xmlns:soap-enc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><soap-env:Header><cwmp:ID soap-env:mustUnderstand="0">2</cwmp:ID><cwmp:NoMoreRequests>0</cwmp:NoMoreRequests></soap-env:Header><soap-env:Body><cwmp:InformResponse><MaxEnvelopes>1</MaxEnvelopes></cwmp:InformResponse></soap-env:Body></soap-env:Envelope>'''
    elif '7 TRANSFER COMPLETE' in xml_data:
        PP()
        status = 204
        response_xml = ''
    elif 'StartTime' in xml_data:
        PP()
        status = 204
        response_xml = ''
    else:
        PP()
        response_xml = ''
        status = 204

    # 创建响应
    response = make_response(response_xml, status)
    response.headers['Content-Type'] = 'text/xml;charset=UTF-8'
    response.headers['Connection'] = 'keep-alive'
    response.headers['SN'] = sn

    return response


if __name__ == '__main__':
    print("TR-069 Simple Server Started!")
    print("Listening on: http://0.0.0.0:9999/web/tr069")
    app.run(host='0.0.0.0', port=9999, debug=True)

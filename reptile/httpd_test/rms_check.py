'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: rms_check.py
@time: 2025/09/26 16:11
@desc: 
'''


import requests
import sys
import os

inform = '''
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:cwmp="urn:dslforum-org:cwmp-1-0">
	<SOAP-ENV:Header>
		<cwmp:ID xsi:type="xsd:string" SOAP-ENV:mustUnderstand="1">2</cwmp:ID>
	</SOAP-ENV:Header>
	<SOAP-ENV:Body>
		<cwmp:Inform>
			<DeviceId>
				<Manufacturer>SCTY</Manufacturer>
				<OUI>A42A71</OUI>
				<ProductClass>TEWF-7861B</ProductClass>
				<SerialNumber>SCTY74123696</SerialNumber>
			</DeviceId>
			<Event SOAP-ENC:arrayType="cwmp:EventStruct[1]">
				<EventStruct>
					<EventCode>2 PERIODIC</EventCode>
					<CommandKey></CommandKey>
				</EventStruct>
			</Event>
			<MaxEnvelopes>1</MaxEnvelopes>
			<CurrentTime>2025-09-26T17:30:43</CurrentTime>
			<RetryCount>0</RetryCount>
			<ParameterList SOAP-ENC:arrayType="cwmp:ParameterValueStruct[14]">
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.Manufacturer</Name>
					<Value xsi:type="xsd:string">SCTY</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.ManufacturerOUI</Name>
					<Value xsi:type="xsd:string">A42A71</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.ProductClass</Name>
					<Value xsi:type="xsd:string">TEWF-7861B</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.SerialNumber</Name>
					<Value xsi:type="xsd:string">SCTY74123696</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.HardwareVersion</Name>
					<Value xsi:type="xsd:string">HV1.0.0</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.SoftwareVersion</Name>
					<Value xsi:type="xsd:string">COGI.V1.0.0</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.SoftwareCompileDate</Name>
					<Value xsi:type="xsd:string">2025-09-26 17:16:12</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.ManagementServer.ConnectionRequestURL</Name>
					<Value xsi:type="xsd:string">http://172.16.25.6:46000</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.DeviceInfo.X_CMCC_DeviceType</Name>
					<Value xsi:type="xsd:string">Model4</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.1.MACAddress</Name>
					<Value xsi:type="xsd:string">24:8B:E0:E5:2D:78</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.LANDevice.1.X_CMCC_LANAbility</Name>
					<Value xsi:type="xsd:string">2.5GE,GE,GE,GE</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.X_CMCC_UserInfo.Password</Name>
					<Value xsi:type="xsd:string">zsxgpon</Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.X_CMCC_UserInfo.Loid</Name>
					<Value xsi:type="xsd:string"></Value>
				</ParameterValueStruct>
				<ParameterValueStruct>
					<Name>InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.ExternalIPAddress</Name>
					<Value xsi:type="xsd:string">172.16.25.6</Value>
				</ParameterValueStruct>
			</ParameterList>
		</cwmp:Inform>
	</SOAP-ENV:Body>
</SOAP-ENV:Envelope>
'''


class HttpdTest:
    def __init__(self):
        self.headers = {
            'User-Agent': "BCM_TR69_CPE_04_00",
            'Connection': "keep-alive",
            'SOAPAction': '',
            'Content-Type': "text/xml"
        }

    def rms_check(self, url):
        try:
            r = requests.post(url, data=inform, headers=self.headers, timeout=20)
        except:
            print('login fail')


if __name__ == '__main__':
    b = HttpdTest()
    b.rms_check("http://10.5.1.101:5122/itms-server/itms?sn=SCTY18C1092B")
    # b.rms_check("http://172.16.30.128:9090/web/tr069?sn=SCTY18C1092B")
    print('Hello world')

import requests

url = 'http://nmg-ct.cnspeedtest.com:9806/nsupload/uploadfile'
# s = json.dumps({'key1': 'value1', 'key2': 'value2'})
# s = '["a2466664-fa3e-11e9-b00b-cdf201982a79",{ "RPCMethod": "Result", "ID": 103, "ObjectPath": "BUCPE.SiteSpeed", "TaskStatus": 1, "Params": { "BUCPE": { "SiteSpeedResult": { "DestUrl": "http://dldir1.qq.com/qqfile/qq/QQ8.3/18038/QQ8.3.exe", "DestIP": "106.117.248.178", "Threads": "1", "SpeedTable": [ 4742744, 5355536, 5368036, 5723560, 5922258, 5748196, 5468776, 5047052, 5247540, 4408248], "Error": null}}}}]'
# s = '["a2466664-fa3e-11e9-b00b-cdf201982a79",{ "RPCMethod": "Result",
# "ID": null, "ObjectPath": "BUCPE.SiteSpeed", "TaskStatus": null,
# "Params": { "BUCPE": { "SiteSpeedResult": { "DestUrl": null, "DestIP":
# null, "Threads": null, "SpeedTable": null, "Error": null}}}}]'
# s = '["a2466664-fa3e-11e9-b00b-cdf201982a72",{ "RPCMethod": "Result", "ID": null, "ObjectPath": "BUCPE.TraceRoute","TaskStatus": null, "Params": { "BUCPE": { "TraceRouteResult": { "DestIP": null, "MaxTTL": null, "PacketSize": null, "Method": "icmp", "PathTable": null, "Error": null}}}}]'
s = '["a2466664-fa3e-11e9-b00b-cdf201982a70",{"RPCMethod": "Result", "ID": 101, "ObjectPath": "BUCPE.TraceRoute", "TaskStatus": 0, "Params": {"BUCPE": {"TraceRouteResult": {"DestIP": "120.132.6.77", "MaxTTL": 30, "PacketSize": 56, "Method": "icmp", "PathTable": null, "Error": null}}}}]'

r = requests.post(url, data=s)
print(r.text)
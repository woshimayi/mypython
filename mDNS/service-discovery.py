'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: service-discovery.py
@time: 2025/05/22 11:47
@desc: 
'''


'''
from zeroconf import ServiceBrowser, Zeroconf
import socket
import time


class MyListener:
    """
    一个监听器类，用于处理服务发现事件。
    """

    def remove_service(self, zeroconf, type, name):
        """当服务从网络上移除时调用。"""
        print(f"Service {name} removed")

    def add_service(self, zeroconf, type, name):
        """当发现新服务时调用。"""
        info = zeroconf.get_service_info(type, name)
        if info:
            print(f"Service {name} added, type: {type}")
            print(f"  Address: {socket.inet_ntoa(info.addresses[0]) if info.addresses else 'N/A'}")
            print(f"  Port: {info.port}")
            print(f"  Server: {info.server}")
            print(f"  Properties: {info.properties}")
            # print(f"  Host TTL: {info.host_ttl}")
            # print(f"  Service TTL: {info.service_ttl}")


# 示例：发现所有 HTTP 服务
def discover_http_services():
    print("Discovering HTTP services (_http._tcp.local.)...")
    zeroconf = Zeroconf()
    listener = MyListener()
    # 浏览特定服务类型
    browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)

    try:
        # 让程序运行一段时间以发现服务
        time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        # 清理资源
        browser.cancel()
        zeroconf.close()
    print("Discovery stopped.")


# 示例：发现所有 IPP 打印服务
def discover_ipp_services():
    print("Discovering IPP services (_ipp._tcp.local.)...")
    zeroconf = Zeroconf()
    listener = MyListener()
    browser = ServiceBrowser(zeroconf, "_ipp._tcp.local.", listener)

    try:
        time.sleep(10)
    except KeyboardInterrupt:
        pass
    finally:
        browser.cancel()
        zeroconf.close()
    print("Discovery stopped.")


# 运行示例
if __name__ == "__main__":
    discover_http_services()
    print("-" * 30)
    discover_ipp_services()
'''


from zeroconf import ServiceInfo, Zeroconf
import socket
import time

def publish_http_service(name="MyWebServer", port=8000):
    print(f"Publishing HTTP service '{name}' on port {port}...")
    zeroconf = Zeroconf()

    # 服务类型：_http._tcp.local.
    # 服务名称：MyWebServer._http._tcp.local.
    # 主机名：MyWebServer.local.
    # IP 地址：设备的本地 IP 地址（这里我们让 Zeroconf 自动获取）
    # 端口：8000
    # 文本属性 (可选)：一个字典，包含服务的额外信息
    info = ServiceInfo(
        "_http._tcp.local.",
        f"{name}._http._tcp.local.",
        addresses=[socket.inet_aton("172.16.36.35")], # 示例：使用回环地址，实际应用中会用真实IP
        port=port,
        properties={'path': '/index.html', 'version': '1.0'},
        server=f"{socket.gethostname()}.local.", # 广告的主机名，通常是设备的本地主机名
    )

    print(f"Registering service: {info.name}")
    zeroconf.register_service(info)

    try:
        print("Service published. Press Ctrl+C to unregister and exit.")
        # 服务将持续发布，直到程序停止
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Unregistering service...")
    finally:
        # 清理资源
        zeroconf.unregister_service(info)
        zeroconf.close()
        print("Service unregistered and Zeroconf closed.")

# 运行示例
if __name__ == "__main__":
    # 注意：在实际应用中，你需要替换 127.0.0.1 为你的设备实际的局域网 IP 地址
    # 或让 Zeroconf 自动检测（默认行为，如果 addresses 参数省略）
    # 对于测试，可以先用 127.0.0.1
    publish_http_service("PythonTestServer-dof", 8080)
# '''
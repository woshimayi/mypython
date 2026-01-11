'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: pyshark_filter_out_new.py
@time: 2025/10/28 10:48
@desc: 
'''
import pyshark


def filter_packets_pyshark(input_file, output_file, display_filter=None):
    """
    使用Pyshark过滤pcapng文件
    """
    # 创建FileCapture对象读取文件，并应用显示过滤器
    input_capture = pyshark.FileCapture(input_file, display_filter=display_filter)

    # 创建FileCapture对象用于写入过滤后的包
    output_capture = pyshark.FileCapture(output_file, display_filter=display_filter)

    # 遍历过滤后的包并写入输出
    for packet in input_capture:
        output_capture.write(packet)

    # 关闭捕获对象
    input_capture.close()
    output_capture.close()
    print(f"过滤完成！保存至 {output_file}")


# 使用示例
if __name__ == "__main__":
    input_pcap = "input.pcapng"
    output_pcap = "filtered.pyshark.pcapng"
    filter_condition = "http"  # 使用Wireshark显示过滤器语法

    filter_packets_pyshark(input_pcap, output_pcap, filter_condition)

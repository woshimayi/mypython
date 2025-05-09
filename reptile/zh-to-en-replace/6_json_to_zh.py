'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: 6_json_to_zh.py
@time: 2025/05/07 15:15
@desc: 
'''


import json
import re

from file_IO.list_dir_file import find_files_with_suffix


def find_chinese_values_in_json(filepath):
    """
    遍历 JSON 文件，找出其中所有包含中文字符的 value。

    Args:
        filepath (str): JSON 文件的路径。

    Returns:
        list: 包含所有找到的包含中文字符的 value 的列表。
    """
    chinese_values = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            print("2")
            data = json.load(f)
            print("0")

        def extract_values(obj):
            if isinstance(obj, dict):
                for value in obj.values():
                    extract_values(value)
            elif isinstance(obj, list):
                for item in obj:
                    extract_values(item)
            elif isinstance(obj, str):
                if re.search(r'[\u4e00-\u9fa5]', obj):
                    chinese_values.append(obj)
        print("1")
        extract_values(data)

    except FileNotFoundError:
        print(f"错误：文件 '{filepath}' 未找到。")
    except json.JSONDecodeError:
        print(f"错误：文件 '{filepath}' 不是有效的 JSON 文件。")
    except Exception as e:
        print(f"读取文件 '{filepath}' 时发生错误：{e}")

    if chinese_values:
        try:
            with open(filepath + "_ZH.txt", 'w', encoding='utf-8') as f:
                for s in chinese_values:
                    f.write(s + '\n')
        except Exception as e:
            print(f"读取文件失败: {e}")
            return []


    return chinese_values

if __name__ == "__main__":
    # json_file_path = r'E:/mypython_new/reptile/zh-to-en-replace/html/json/tableCfg.json'
    # found_values = find_chinese_values_in_json(json_file_path)
    #
    # if found_values:
    #     print(f"\n在文件 '{json_file_path}' 中找到以下包含中文字符的 value:")
    #     for value in found_values:
    #         print(value)
    # else:
    #     print(f"\n在文件 '{json_file_path}' 中没有找到包含中文字符的 value.")


    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    file_suffix = '.json'

    found_files = find_files_with_suffix(target_dir, file_suffix)
    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)

            json_file_path = file_path
            found_values = find_chinese_values_in_json(json_file_path)

            if found_values:
                print(f"\n在文件 '{json_file_path}' 中找到以下包含中文字符的 value:")
                for value in found_values:
                    print(value)
            else:
                print(f"\n在文件 '{json_file_path}' 中没有找到包含中文字符的 value。")

    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")


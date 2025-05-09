'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: 7_json_value_replace.py
@time: 2025/05/07 15:23
@desc: 
'''

import json
import re

import json
import re

from file_IO.list_dir_file import find_files_with_suffix


def replace_chinese_values_from_en(input_path, en_path, output_path="output.json"):
    """
    读取 input.json 中的中文 value 作为 key，查找 en.json 中的 value 进行替换，
    并输出到 output.json。

    Args:
        input_path (str): input.json 文件的路径。
        en_path (str): en.json 文件的路径。
        output_path (str, optional): 替换后的 JSON 文件的输出路径。
                                      默认为 "output.json"。
    """
    chinese_to_english = {}

    try:
        with open(en_path, 'r', encoding='utf-8') as f:
            en_data = json.load(f)
            # 假设 en.json 是一个扁平的字典，中文 value 作为 key，英文 value 作为 value
            chinese_to_english = en_data
    except FileNotFoundError:
        print(f"错误：文件 '{en_path}' 未找到。")
        return
    except json.JSONDecodeError:
        print(f"错误：文件 '{en_path}' 不是有效的 JSON 文件。")
        return
    except Exception as e:
        print(f"读取文件 '{en_path}' 时发生错误：{e}")
        return

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            input_data = json.load(f)

        def replace_values(obj):
            if isinstance(obj, dict):
                new_dict = {}
                for key, value in obj.items():
                    new_dict[key] = replace_values(value)
                return new_dict
            elif isinstance(obj, list):
                new_list = []
                for item in obj:
                    new_list.append(replace_values(item))
                return new_list
            elif isinstance(obj, str) and re.search(r'[\u4e00-\u9fa5]', obj):
                return chinese_to_english.get(obj, obj)  # 如果 en.json 中找到 key，则替换，否则保留原中文
            return obj

        output_data = replace_values(input_data)

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=4)

        print(f"替换后的 JSON 文件已保存到: {output_path}")

    except FileNotFoundError:
        print(f"错误：文件 '{input_path}' 未找到。")
        return
    except json.JSONDecodeError:
        print(f"错误：文件 '{input_path}' 不是有效的 JSON 文件。")
        return
    except Exception as e:
        print(f"读取文件 '{input_path}' 时发生错误：{e}")
        return

if __name__ == "__main__":
    # input_file_path = r"E:\mypython_new\reptile\zh-to-en-replace\html\json\config.json"
    # en_file_path = r"E:\mypython_new\reptile\zh-to-en-replace\html\json\config.json.json"
    # output_file_path = r"E:\mypython_new\reptile\zh-to-en-replace\html\json\config_en.json"
    #
    # replace_chinese_values_from_en(input_file_path, en_file_path, output_file_path)


    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    file_suffix = '.json'

    found_files = find_files_with_suffix(target_dir, file_suffix)
    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)

            input_file_path = file_path
            en_file_path = file_path + r'.json'
            output_file_path = file_path + r'_en'

            replace_chinese_values_from_en(input_file_path, en_file_path, output_file_path)

    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")


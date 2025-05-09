'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: 4_chinese_extraction-js.py
@time: 2025/05/06 13:34
@desc: 
'''

import re

from file_IO.list_dir_file import find_files_with_suffix

'''
def find_chinese_in_file(filepath):
    """
    查找指定文件中包含的中文字符串。

    Args:
        filepath (str): 要查找的文件路径。

    Returns:
        list: 一个包含所有找到的中文字符串的列表。
              如果文件不存在或读取失败，则返回一个空列表。
    """
    chinese_strings = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                # 使用正则表达式匹配 Unicode 中文字符范围
                chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', line)
                chinese_strings.extend(chinese_matches)
    except FileNotFoundError:
        print(f"错误：文件 '{filepath}' 未找到。")
    except Exception as e:
        print(f"读取文件 '{filepath}' 时发生错误：{e}")
    return chinese_strings

if __name__ == "__main__":
    file_to_search = "example.txt"  # 将其替换为你要查找的文件名

    # 创建一个包含中文字符的示例文件
    with open(file_to_search, 'w', encoding='utf-8') as f:
        f.write("This line contains English words.\n")
        f.write("这一行包含一些中文字符。\n")
        f.write("还有一些中文词语：你好，世界！\n")
        f.write("English again.\n")
        f.write("混合了英文和中文：hello 你好 world。\n")

    found_chinese = find_chinese_in_file(file_to_search)

    if found_chinese:
        print(f"在文件 '{file_to_search}' 中找到以下中文字符串：")
        for s in found_chinese:
            print(s)
    else:
        print(f"在文件 '{file_to_search}' 中没有找到中文字符串。")
'''

import subprocess
import json
import re

import subprocess
import json
import re
import os

def find_chinese_strings_in_js(filepath):
    """
    查找 JS 文件中字符串字面量里包含中文字符的内容（可混有英文），只提取内容，不带引号。
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"读取文件失败: {e}")
        return []

    # 匹配 "..."、'...'、`...` 里包含至少一个中文字符的字符串，提取内容不带引号
    pattern = r'"([^"\n]*[\u4e00-\u9fa5]+[^"\n]*)"|\'([^\'\n]*[\u4e00-\u9fa5]+[^\'\n]*)\'|`([^`\n]*[\u4e00-\u9fa5]+[^`\n]*)`'
    matches = re.findall(pattern, content)

    # re.findall 返回的是每个分组的元组，取非空的那个
    result = []
    for m in matches:
        for s in m:
            if s:
                result.append(s)

    if result:
        try:
            with open(filepath + "_ZH.txt", 'w', encoding='utf-8') as f:
                for s in result:
                    f.write(s + '\n')
        except Exception as e:
            print(f"读取文件失败: {e}")
            return []

    return result


if __name__ == "__main__":

    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    file_suffix = '.js'

    found_files = find_files_with_suffix(target_dir, file_suffix)
    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)
            js_file_path = file_path
            found = find_chinese_strings_in_js(js_file_path)
            if found:
                print(f"\n在文件 '{js_file_path}' 中找到以下包含中文的字符串：\n")
                for s in found:
                    print(s)
            else:
                print(f"\n在文件 '{js_file_path}' 中没有找到包含中文的字符串。")
    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")



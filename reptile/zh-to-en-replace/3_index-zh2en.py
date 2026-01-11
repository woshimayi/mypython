'''
*************************************: 
FilePath     : \zh-to-en-replace\index-zh2en.py
version      : 
Author       : dof
Date         : 2025-04-27 10:39:21
LastEditors  : dof
LastEditTime : 2025-04-27 10:39:21
Descripttion :  
compile      :  
**************************************: 
'''

import re
from bs4 import BeautifulSoup, Comment
import json

from file_IO.list_dir_file import find_files_with_suffix


def replace_chinese_text_in_html(html_content, translation_dict):
    """
    使用提供的翻译字典替换HTML字符串中的中文文本。

    Args:
        html_content (str): 要处理的HTML字符串。
        translation_dict (dict): 包含中文文本到英文文本映射的字典。

    Returns:
        str: 替换后的HTML字符串。
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    soup.prettify()
    text_nodes = [
        text for text in soup.find_all(string=True)
        if not isinstance(text, Comment)
    ]

    for text_node in text_nodes:
        original_text = text_node.strip()
        if original_text in translation_dict:
            # 替换文本
            text_node.replace_with(translation_dict[original_text])

    return str(soup)

if __name__ == '__main__':
    # # 读取HTML文件
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 读取JSON文件
    with open('index_output.json', 'r', encoding='utf-8') as f:
        translation_dict = json.load(f)

    # 替换HTML内容中的中文文本
    modified_html_content = replace_chinese_text_in_html(html_content, translation_dict)

    # 将修改后的HTML写入到新的文件中
    with open('index_en.html', 'w', encoding='utf-8') as f:
        f.write(modified_html_content)

    print("转换完成，已保存到 index_en.html")


    # target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    # file_suffix = '.html'
    #
    # found_files = find_files_with_suffix(target_dir, file_suffix)
    # # found_files = [r'E:/mypython_new/reptile/zh-to-en-replace/index.html']
    # if found_files:
    #     print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
    #     for file_path in found_files:
    #         print(file_path)
    #
    #         # 读取HTML文件
    #         with open(file_path, 'r', encoding='utf-8') as f:
    #             html_content = f.read()
    #
    #         # 读取JSON文件
    #         with open(file_path + r'.json', 'r', encoding='utf-8') as f:
    #             translation_dict = json.load(f)
    #
    #         # 替换HTML内容中的中文文本
    #         modified_html_content = replace_chinese_text_in_html(html_content, translation_dict)
    #
    #         # 将修改后的HTML写入到新的文件中
    #         with open(file_path + r'_en.html', 'w', encoding='utf-8') as f:
    #             f.write(modified_html_content)
    #
    #         print("转换完成，已保存到 {}_en.html".format(file_path))
    #
    #
    # else:
    #     print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")


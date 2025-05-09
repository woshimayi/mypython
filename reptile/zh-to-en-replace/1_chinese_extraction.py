'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: chinese_repetile.py
@time: 2025/04/25 17:06
@desc: 
'''

'''
import re

def find_chinese_entries(index_file):
    """
    从索引文件中查找所有中文词条。

    Args:
        index_file: 索引文件的路径。

    Returns:
        一个包含所有中文词条的列表。
    """
    chinese_entries = []
    try:
        with open(index_file, 'r', encoding='utf-8') as f:  # 确保使用 UTF-8 编码
            for line in f:
                # 匹配包含至少一个中文汉字的行
                if re.search(r'[\u4e00-\u9fa5]+', line):
                    chinese_entries.append(line.strip())  # 去除行尾的空白字符
    except FileNotFoundError:
        print(f"错误：文件 '{index_file}' 未找到。")
    return chinese_entries

if __name__ == "__main__":
    index_file_path = "index.html"  # 替换为你的索引文件路径
    chinese_entries = find_chinese_entries(index_file_path)

    if chinese_entries:
        print("找到的中文词条：")
        for entry in chinese_entries:
            print(entry)
    else:
        print("未找到中文词条。")
'''

'''
import re
from bs4 import BeautifulSoup

def find_pure_chinese_entries(index_file):
    """
    从索引文件中查找所有去除 HTML 信息后只包含汉字的词条。

    Args:
        index_file: 索引文件的路径。

    Returns:
        一个包含所有纯汉字词条的列表。
    """
    pure_chinese_entries = []
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            for line in f:
                # 使用 BeautifulSoup 解析 HTML（如果存在）
                soup = BeautifulSoup(line, 'html.parser')
                text_content = soup.get_text(separator=' ', strip=True)

                # 使用正则表达式查找纯汉字（一个或多个连续汉字）
                chinese_matches = re.findall(r'^[\u4e00-\u9fa5]+$', text_content)
                if chinese_matches:
                    pure_chinese_entries.extend(chinese_matches)

    except FileNotFoundError:
        print(f"错误：文件 '{index_file}' 未找到。")
    return pure_chinese_entries

if __name__ == "__main__":
    index_file_path = "index.html"  # 替换为你的索引文件路径
    pure_chinese_entries = find_pure_chinese_entries(index_file_path)

    if pure_chinese_entries:
        print("找到的纯汉字词条：")
        for entry in pure_chinese_entries:
            print(entry)
    else:
        print("未找到纯汉字词条。")
'''



import re
from bs4 import BeautifulSoup, Comment

def extract_chinese_text(html_content):
    """
    从 HTML 字符串中提取包含中文的文本。

    Args:
        html_content (str): 要解析的 HTML 字符串。

    Returns:
        list: 包含中文文本的字符串列表。
    """
    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # 找到所有文本节点
    text_nodes = soup.find_all(string=True)

    # 找到所有文本节点，并排除注释
    text_nodes = [
        text for text in soup.find_all(string=True)
        if not isinstance(text, Comment)
    ]

    chinese_text_list = []
    for text in text_nodes:
        # print('\t\ttmp', text)
        # 使用正则表达式检测字符串中是否包含中文字符
        if re.search(r'[\u4e00-\u9fa5]', text):
            # 如果包含中文字符，则去除文本中的换行符和多余空格
            cleaned_text = text.replace('\n', '').strip()
            if cleaned_text:  # 确保文本不是空的
                print(cleaned_text)
                chinese_text_list.append(cleaned_text)
    return chinese_text_list

if __name__ == '__main__':
    # 读取HTML文件
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()

    # 调用函数提取中文文本
    result = extract_chinese_text(html_content)

    # 打印结果
    # for text in result:
    #     print(text)

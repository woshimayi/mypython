'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: 8_html_reptile_elements_zh.py
@time: 2025/05/07 17:28
@desc: 
'''

from bs4 import BeautifulSoup, Comment
import re
import json

from file_IO.list_dir_file import find_files_with_suffix


def extract_chinese_text(html_file_path):
    """
    从 HTML 字符串中提取包含中文的文本。

    Args:
        html_content (str): 要解析的 HTML 字符串。

    Returns:
        list: 包含中文文本的字符串列表。
    """
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{html_file_path}' 未找到。")
        return []

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

    if chinese_text_list:
        try:
            with open(html_file_path + "_ZH.txt", 'w', encoding='utf-8') as f:
                for s in chinese_text_list:
                    f.write(s + '\n')
        except Exception as e:
            print(f"读取文件失败: {e}")

    return chinese_text_list


def extract_chinese_from_span_input(html_file_path):
    """
    从 HTML 文件中的 <span> 和 <input> 标签中提取所有的中文字符串，排除注释内容。

    Args:
        html_file_path (str): HTML 文件的路径。

    Returns:
        list: 包含所有提取到的中文字符串的列表。
    """
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"错误：文件 '{html_file_path}' 未找到。")
        return []

    soup = BeautifulSoup(html_content, 'html.parser')
    chinese_strings = []

    # 找到所有文本节点
    text_nodes = soup.find_all(string=True)

    # 查找所有的 <span> 标签
    span_tags = soup.find_all('span')
    for span in span_tags:
        # 排除注释内容
        for child in span.contents:
            if isinstance(child, str):
                if '\n' in child:
                    # print('00000', child)
                    child = child.replace('\n', 'AE')
                    chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', child)
                    print("00000", chinese_matches)
                    chinese_strings.append(child)
                else:
                    chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', child)
                    chinese_strings.extend(chinese_matches)

    # 查找所有的 <span> 标签
    div_tags = soup.find_all('div')
    for div in div_tags:

        titleKey = div.find("div", title=True)
        if titleKey:
            print('div', titleKey['title'])
            chinese_strings.append(titleKey['title'])

        # 排除注释内容
        for child in div.contents:
            if isinstance(child, str):
                chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', child)
                chinese_strings.extend(chinese_matches)

    # 查找所有的 <input> 标签
    input_tags = soup.find_all('input')
    for input_tag in input_tags:
        # 检查 value 属性
        if 'value' in input_tag.attrs:
            value = input_tag['value']
            chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', value)
            chinese_strings.extend(chinese_matches)

        # 检查 placeholder 属性
        if 'placeholder' in input_tag.attrs:
            placeholder = input_tag['placeholder']
            chinese_matches = re.findall(r'[\u4e00-\u9fa5]+', placeholder)
            chinese_strings.extend(chinese_matches)

    with open(html_file_path + r'_ZH.txt', 'w', encoding='utf-8') as f:
        for s in chinese_strings:
            print(s)
            f.write(s + '\n')

    return chinese_strings




def replace_chinese_with_json_value(html_file_path, json_file_path):
    """
    从 HTML 文件的 <span>、<div> 和 <input> 标签中提取中文，
    使用 JSON 文件中的值进行替换，并将替换后的 HTML 写回文件。

    Args:
        html_file_path (str): HTML 文件的路径。
        json_file_path (str): JSON 文件的路径。
    """
    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"错误：HTML 文件 '{html_file_path}' 未找到。")
        return

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError:
        print(f"错误：JSON 文件 '{json_file_path}' 未找到。")
        return
    except json.JSONDecodeError:
        print(f"错误：JSON 文件 '{json_file_path}' 格式不正确。")
        return

    soup = BeautifulSoup(html_content, 'html.parser')


    def replace_text(text):
        for key, value in json_data.items():
            if 'AE' in key:
                key = key.replace('AE', '\n')
                value = value.replace('AE', '\n')
            text = text.replace(key, value)
        return text

    # 替换 <span> 标签中的文本
    span_tags = soup.find_all('span')
    for span in span_tags:
        if span.string:
            span.string.replace_with(replace_text(span.string))
        else:
            # 处理包含子元素的 span
            for child in span.contents:
                if isinstance(child, str):
                    child.replace_with(replace_text(child))

    # 替换 <div> 标签中的文本
    div_tags = soup.find_all('div')
    for div in div_tags:

        if div.find("div", title=True):
            print('div', div.find("div", title=True)['title'])
            div_key = div.find("div", title=True)['title']
            div.find("div", title=True)['title'] = replace_text(div_key)

        if div.string:
            div.string.replace_with(replace_text(div.string))
        else:
            # 处理包含子元素的 div
            for child in div.contents:
                if isinstance(child, str):
                    child.replace_with(replace_text(child))

    # 替换 <input> 标签的 value 属性
    input_tags = soup.find_all('input')
    for input_tag in input_tags:
        if 'value' in input_tag.attrs:
            input_tag['value'] = replace_text(input_tag['value'])
        if 'placeholder' in input_tag.attrs:
            input_tag['placeholder'] = replace_text(input_tag['placeholder'])

    # 将修改后的 HTML 写回文件 (可以修改文件名)
    output_file_path = html_file_path.replace('.html', '_en.html')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"HTML 文件 '{html_file_path}' 中的中文已根据 '{json_file_path}' 中的内容进行替换，并保存到 '{output_file_path}'。")


def replace_chinese_text_in_html(html_file_path, json_file_path):
    """
    使用提供的翻译字典替换HTML字符串中的中文文本。

    Args:
        html_content (str): 要处理的HTML字符串。
        translation_dict (dict): 包含中文文本到英文文本映射的字典。

    Returns:
        str: 替换后的HTML字符串。
    """

    try:
        with open(html_file_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print(f"错误：HTML 文件 '{html_file_path}' 未找到。")
        return

    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            translation_dict = json.load(f)
    except FileNotFoundError:
        print(f"错误：JSON 文件 '{json_file_path}' 未找到。")
        return
    except json.JSONDecodeError:
        print(f"错误：JSON 文件 '{json_file_path}' 格式不正确。")
        return

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

    # 将修改后的 HTML 写回文件 (可以修改文件名)
    output_file_path = html_file_path.replace('.html', '_en.html')
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(str(soup))

    print(f"HTML 文件 '{html_file_path}' 中的中文已根据 '{json_file_path}' 中的内容进行替换，并保存到 '{output_file_path}'。")
    return str(soup)


def create_json_from_txt(zh_file, en_file, output_file):
    """
    Generates a JSON file containing key-value pairs from two text files,
    where the first file contains Chinese text (keys) and the second file
    contains corresponding English text (values).

    Args:
        zh_file (str): Path to the Chinese text file.
        en_file (str): Path to the English text file.
        output_file (str): Path to the output JSON file.
    """

    zh_lines = []
    en_lines = []

    try:
        with open(zh_file, 'r', encoding='utf-8') as f:
            zh_lines = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: Chinese file '{zh_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading Chinese file: {e}")
        return

    try:
        with open(en_file, 'r', encoding='utf-8') as f:
            en_lines = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Error: English file '{en_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading English file: {e}")
        return
    print("zs{}, en{}".format(len(zh_lines), len(en_lines)))
    if len(zh_lines) != len(en_lines):
        print("Error: The number of lines in the Chinese and English files do not match.")
        return

    data = {}
    for i in range(len(zh_lines)):
        data[zh_lines[i]] = en_lines[i]

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"JSON file '{output_file}' created successfully.")
    except Exception as e:
        print(f"Error writing JSON file: {e}")



if __name__ == "__main__":
    html_file = r'index.html'

    zh_file = "index.html_ZH.txt"
    en_file = "index.html_EN.txt"
    output_file = "index_output.json"

    # First extract
    # extract_chinese_text(html_file)
    # replace_chinese_text_in_html(html_file, json_file)

    # Second extract
    # extract_chinese_from_span_input(html_file)

    create_json_from_txt(zh_file, en_file, output_file)
    replace_chinese_with_json_value(html_file, output_file)


    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/second_html/'
    file_suffix = '.html'

    found_files = find_files_with_suffix(target_dir, file_suffix)
    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)

            # extract HTML file
            # extract_chinese_from_span_input(file_path)

            # replace html file
            create_json_from_txt(file_path + r"_ZH.txt", file_path + r"_EN.txt", file_path + r'.json')
            replace_chinese_with_json_value(file_path, file_path + r'.json')

    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")

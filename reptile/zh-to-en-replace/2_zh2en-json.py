'''
*************************************: 
FilePath     : \zh-to-en-replace\zh2en-json.py
version      : 
Author       : dof
Date         : 2025-04-27 10:35:41
LastEditors  : dof
LastEditTime : 2025-04-27 10:35:53
Descripttion :  
compile      :  
**************************************: 
'''
import json

from file_IO.list_dir_file import find_files_with_suffix


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
    # zh_file = "html_ZH.txt"
    # en_file = "html_EN.txt"
    # output_file = "html_output.json"


    # target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    # file_suffix = '.json'
    #
    # found_files = find_files_with_suffix(target_dir, file_suffix)
    # if found_files:
    #     print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
    #     for file_path in found_files:
    #         print(file_path)
    #         zh_file = file_path + r"_ZH.txt"
    #         en_file = file_path + r'_EN.txt'
    #         output_file = file_path + r'.json'
    #         create_json_from_txt(zh_file, en_file, output_file)
    #
    # else:
    #     print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")

    zh_file = "index.html_ZH.txt"
    en_file = "index.html_EN.txt"
    output_file = "index_output.json"
    create_json_from_txt(zh_file, en_file, output_file)
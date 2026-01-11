'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: list_dir_file.py
@time: 2025/05/07 10:27
@desc: 
'''

import os


def find_files_with_suffix(root_dir, suffix):
    """
    遍历指定根目录及其子目录，查找具有特定后缀的文件。

    Args:
        root_dir (str): 要遍历的根目录的路径。
        suffix (str): 要查找的文件后缀（例如 ".txt", ".jpg"）。

    Returns:
        list: 包含所有找到的符合条件的文件完整路径的列表。
    """
    matching_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith(suffix):
                full_path = os.path.join(dirpath, filename)
                matching_files.append(full_path)
    return matching_files


if __name__ == "__main__":
    # target_dir = input("请输入要遍历的根目录路径: ")
    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    file_suffix = '.js'

    found_files = find_files_with_suffix(target_dir, file_suffix)

    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")

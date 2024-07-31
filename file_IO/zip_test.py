'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: zip_test.py
@time: 24/3/9 17:21
@desc: 
'''
import os
import zipfile

def compress_folder(folder_path, output_path):
    """
    压缩文件夹

    Args:
        folder_path: 要压缩的文件夹路径
        output_path: 压缩包输出路径

    Returns:
        None
    """

    # 创建一个 ZipFile 对象
    with zipfile.ZipFile(output_path, 'w') as z:
        # 将文件夹中的所有文件添加到压缩包中
        for root, dirs, files in os.walk(folder_path):
            print("{} {} {}".format(root, dirs, files))
            for file in files:
                print(file)
                if file == output_path:
                    continue
                z.write(os.path.join(root, file))

def compress_file(file_path):
    """
    压缩文件夹

    Args:
        folder_path: 要压缩的文件夹路径
        output_path: 压缩包输出路径

    Returns:
        None
    """

    output_path = file_path.split('\\')[-1]
    # 创建一个 ZipFile 对象
    with zipfile.ZipFile(output_path, 'w') as z:
        # 将文件夹中的所有文件添加到压缩包中
        for file in files:
            print(file)
            if file == output_path:
                continue
            z.write(os.path.join(root, file))

def compress_file_folder(folder_path):
    output_path = folder_path.split('\\')[-1]



print(os.getcwd().split('\\')[-1])

# 压缩文件夹
# compress_folder(os.getcwd(), os.getcwd().split('\\')[-1] + '.zip')



# 压缩包创建成功
print('压缩包创建成功')


# 压缩包创建成功
print('压缩包创建成功')

'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: win32clipboard.py.py
@time: 2025/12/09 14:18
@desc: 
'''
import win32clipboard
import win32api
from PIL import Image  # 仍然保留，但在这里不直接使用

# 定义常用的剪贴板格式 ID
CF_TEXT = 1
CF_DIB = 8  # 图片格式
CF_HDROP = 15  # 文件路径列表格式


def get_clipboard_type_and_data():
    """
    判断 Windows 剪贴板中内容的类型，并尝试返回内容。
    """
    result = {"type": "未知或空 (Unknown/Empty)", "data": None}

    try:
        win32clipboard.OpenClipboard()

        # 1. 检查文件路径 (Files)
        if win32clipboard.IsClipboardFormatAvailable(CF_HDROP):
            try:
                # 获取 HDROP 句柄
                hdrop = win32clipboard.GetClipboardData(CF_HDROP)

                # 查询剪贴板中文件路径的数量
                file_count = win32api.DragQueryFileW(hdrop, -1)
                file_paths = []

                # 遍历并获取每个文件路径
                for i in range(file_count):
                    # DragQueryFileW(句柄, 索引, 缓冲区, 缓冲区大小)
                    # 索引 -1 用于获取文件数量，索引 0, 1, 2... 用于获取具体路径
                    path = win32api.DragQueryFileW(hdrop, i)
                    file_paths.append(path)

                result["type"] = "文件路径 (Files)"
                result["data"] = file_paths
                return result

            except Exception as e:
                # 某些情况下，获取 HDROP 数据可能失败
                print(f"警告: 尝试获取文件路径失败: {e}")

        # 2. 检查图片 (Image)
        if win32clipboard.IsClipboardFormatAvailable(CF_DIB):
            # 因为获取 DIB 并用 PIL 读取的流程复杂，这里只做存在性判断
            result["type"] = "图片 (Image)"
            result["data"] = None  # 暂不提取图片数据
            return result

        # 3. 检查文本 (Text)
        if win32clipboard.IsClipboardFormatAvailable(CF_TEXT):
            text = win32clipboard.GetClipboardData(CF_TEXT)
            if text and text.strip():
                result["type"] = "文本 (Text)"
                result["data"] = text
                return result

        return result

    except Exception as e:
        print(f"访问剪贴板出错: {e}")
        result["type"] = "错误 (Error)"
        result["data"] = str(e)
        return result
    finally:
        try:
            win32clipboard.CloseClipboard()
        except:
            pass  # 确保关闭


# --- 运行示例 ---
# clipboard_data = get_clipboard_type_and_data()
# type_result = clipboard_data["type"]
# content_data = clipboard_data["data"]
#
# print(f"剪贴板内容类型: **{type_result}**")
#
# if type_result == "文件路径 (Files)":
#     print("\n--- 复制的文件路径列表 ---")
#     for i, path in enumerate(content_data):
#         print(f"文件 {i + 1}: {path}")
#
# elif type_result == "文本 (Text)":
#     print("\n--- 文本内容 ---")
#     # 打印前 200 个字符
#     if len(content_data) > 200:
#         print(content_data[:200])
#     else:
#         print(content_data)



import win32clipboard
from PIL import Image
import io

# 定义图片格式 ID
CF_DIB = 8

def copy_image_win32(img):
    """
    使用 win32clipboard 将 PIL Image 对象复制到剪贴板。
    """
    output = io.BytesIO()
    # 必须将 PIL Image 保存为 BMP 格式的字节流，这是 Windows 剪贴板常用的格式。
    img.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:] # 去除 BMP 文件头 (14字节) 以获取 DIB 结构数据
    output.close()

    try:
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        # 设置数据，使用 CF_DIB 格式
        win32clipboard.SetClipboardData(CF_DIB, data)
        print("🎉 (Win32) 图片已成功复制到剪贴板！")
    except Exception as e:
        print(f"❌ (Win32) 复制到剪贴板失败: {e}")
    finally:
        try:
            win32clipboard.CloseClipboard()
        except:
            pass

# --- 运行示例 ---
# 创建一个临时的蓝色图片对象
temp_img = Image.new('RGB', (150, 50), color = 'blue')
copy_image_win32(temp_img)
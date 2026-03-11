'''
@author: caopeng
@license: (C) Copyright 2013-2049, Node Supply Chain Manager Corporation Limited. 
@contact: woshidamayi@gmail.com
@software: dof
@file: omci_988_parse.py
@time: 2025/06/20 11:13
@desc: 
'''

# python_pdf_parser.py

import PyPDF2
import pdfplumber
import fitz  # PyMuPDF
import os


# 创建一个用于测试的简单PDF文件 (如果不存在)
# 实际项目中，您会使用已有的PDF文件
def create_dummy_pdf(filename="sample.pdf", reportlab=None):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(filename, pagesize=letter)
    c.drawString(100, 780, "OMCI G.988 Specification - Example MEs")
    c.drawString(100, 760, "-------------------------------------")
    c.drawString(100, 740, "Managed Entity: ONU-G (ME #1)")
    c.drawString(100, 720, "Description: Represents the ONU equipment itself.")

    # 模拟ME属性的表格结构
    c.drawString(100, 680, "Attributes:")
    c.drawString(100, 660, "ID | Name                 | Type      | R/W | Default | Range/Enum")
    c.drawString(100, 640, "---|----------------------|-----------|-----|---------|-------------------------")
    c.drawString(100, 620, "1  | Vendor ID            | String(4) | R   | N/A     | ABC, XYZ")
    c.drawString(100, 600, "2  | Serial Number        | String(8) | R   | N/A     | Unique SN")
    c.drawString(100, 580, "3  | Software Image 1 Ptr | Pointer   | R/W | Null    | SoftwareImage ME #7")
    c.drawString(100, 560, "4  | Version              | String(14)| R   | N/A     | x.y.z.b")
    c.drawString(100, 540, "5  | Operational State    | Enum      | R   | Enabled | Enabled(0), Disabled(1)")
    c.drawString(100, 520, "6  | Device Capabil.      | Bit Field | R   | N/A     | (Bit 0: VoIP, Bit 1: IPTV)")
    c.drawString(100, 500, "----------------------------------------------------------------------------------")

    c.drawString(100, 450, "Managed Entity: Physical Path Termination Point Ethernet UNI (ME #11)")
    c.drawString(100, 430, "Description: Physical termination for Ethernet user interface.")
    c.drawString(100, 410, "Attributes:")
    c.drawString(100, 390, "ID | Name                 | Type      | R/W | Default | Range/Enum")
    c.drawString(100, 370, "---|----------------------|-----------|-----|---------|-------------------------")
    c.drawString(100, 350, "1  | Port ID              | Uint16    | R   | N/A     | 0-10")
    c.drawString(100, 330, "2  | Loopback Config      | Enum      | R/W | Disable | Disable(0), Enable(1)")
    c.drawString(100, 310, "3  | Auto-Negotiation     | Bool      | R/W | True    | True, False")
    c.drawString(100, 290, "----------------------------------------------------------------------------------")

    # 第二页
    c.showPage()
    c.drawString(100, 750, "这是第二页的内容。")
    c.drawString(100, 730, "可能包含更多MEs或表格。")
    c.save()
    print(f"Created dummy PDF: {filename}")


if not os.path.exists("sample.pdf"):
    create_dummy_pdf()

pdf_file = "sample.pdf"

print("--- 使用 PyPDF2 提取文本 ---")
try:
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        print(f"PDF 包含 {num_pages} 页。")
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            print(f"\n--- 第 {page_num + 1} 页文本 (PyPDF2) ---")
            print(text)
except Exception as e:
    print(f"PyPDF2 提取文本失败: {e}")

print("\n--- 使用 pdfplumber 提取文本和表格 (增强版) ---")
try:
    with pdfplumber.open(pdf_file) as pdf:
        num_pages = len(pdf.pages)
        print(f"PDF 包含 {num_pages} 页。")
        for page_num, page in enumerate(pdf.pages):
            print(f"\n--- 第 {page_num + 1} 页文本 (pdfplumber) ---")
            text = page.extract_text()
            print(text)

            print(f"--- 第 {page_num + 1} 页表格 (pdfplumber 增强) ---")

            # 针对OMCI规范中常见的表格设置
            # 这些参数可能需要根据实际G.988 PDF的表格布局进行微调
            # vertical_strategy/horizontal_strategy: "lines" (根据线条), "text" (根据文本), "explicit" (手动指定)
            # snap_tolerance: 容忍多少像素的偏移来“对齐”线条或文本边界
            # join_tolerance: 容忍多少像素的间距来“连接”断开的线条或文本块
            # min_words_horizontal/min_words_vertical: 识别为表格所需的最小单词数
            # explicit_vertical_lines/explicit_horizontal_lines: 如果表格没有线条，可以手动指定列/行X/Y坐标
            table_settings = {
                "vertical_strategy": "lines",  # 假设表格有垂直线条
                "horizontal_strategy": "lines",  # 假设表格有水平线条
                "snap_tolerance": 3,  # 允许轻微的线条或文本对齐误差
                "join_tolerance": 3,  # 允许轻微的线条断裂
                "edge_min_length": 5,  # 识别为表格边缘所需的最小线条长度
                "min_words_horizontal": 1,  # 每列至少一个单词
                "min_words_vertical": 1,  # 每行至少一个单词
            }

            tables = page.extract_tables(table_settings=table_settings)
            if tables:
                for i, table in enumerate(tables):
                    print(f"  --- 发现表格 {i + 1} ---")
                    # 第一行通常是表头
                    headers = [h.strip() if h else '' for h in table[0]]
                    print(f"    表头: {headers}")
                    for row_num, row_data in enumerate(table[1:]):  # 跳过表头
                        # 清理单元格数据，去除多余空格
                        cleaned_row = [cell.strip() if cell else '' for cell in row_data]
                        print(f"    行 {row_num + 1}: {cleaned_row}")

                        # --- 概念性：这里开始进行语义解析 ---
                        # 假设我们知道表头是 "ID", "Name", "Type", "R/W", "Default", "Range/Enum"
                        # 我们可以将每行数据映射到这些字段
                        if len(headers) == len(cleaned_row):
                            attribute_info = dict(zip(headers, cleaned_row))
                            # 进一步处理 attribute_info 字典
                            # 例如，识别 Type "String(4)" -> type: string, length: 4
                            # R/W "R" -> Read-Only
                            # Range/Enum "Enabled(0), Disabled(1)" -> 解析枚举值
                            # 这是最复杂的部分，需要大量的规则和模式匹配
                            # print(f"      解析后的属性信息: {attribute_info}") # 调试输出
                print("  表格提取完成。")
            else:
                print("  未发现表格。")
except Exception as e:
    print(f"pdfplumber 提取失败: {e}")

print("\n--- 使用 fitz (PyMuPDF) 提取文本 ---")
try:
    doc = fitz.open(pdf_file)
    num_pages = doc.page_count
    print(f"PDF 包含 {num_pages} 页。")
    for page_num in range(num_pages):
        page = doc.load_page(page_num)
        text = page.get_text()
        print(f"\n--- 第 {page_num + 1} 页文本 (fitz) ---")
        print(text)
    doc.close()
except Exception as e:
    print(f"fitz (PyMuPDF) 提取文本失败: {e}")

# 清理生成的PDF文件
# os.remove("sample.pdf")
# print(f"Removed dummy PDF: {filename}")


if __name__ == '__main__':
    print('Hello world')

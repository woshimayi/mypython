import re
import json

from file_IO.list_dir_file import find_files_with_suffix


def replace_chinese_in_js(js_path, json_path, output_path):
    # 读取 JS 文件内容
    with open(js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        # 读取 JSON 映射
        with open(json_path, 'r', encoding='utf-8') as f:
            mapping = json.load(f)
    except Exception as e:
        print("no file ", e)
        return


    # 匹配字符串字面量中的中文
    pattern = r'"([^"\n]*[\u4e00-\u9fa5]+[^"\n]*)"|\'([^\'\n]*[\u4e00-\u9fa5]+[^\'\n]*)\'|`([^`\n]*[\u4e00-\u9fa5]+[^`\n]*)`'

    def replace_func(match):
        # 取出匹配到的内容
        for group in match.groups():
            if group:
                # 用 json 里的 value 替换
                return match.group(0).replace(group, mapping.get(group, group))
        return match.group(0)

    new_content = re.sub(pattern, replace_func, content)

    # 保存为新 Python 文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(new_content)


if __name__ == "__main__":


    target_dir = r'E:/mypython_new/reptile/zh-to-en-replace/html/'
    file_suffix = '.js'

    found_files = find_files_with_suffix(target_dir, file_suffix)
    if found_files:
        print(f"\n在目录 '{target_dir}' 及其子目录下找到以下后缀为 '{file_suffix}' 的文件:")
        for file_path in found_files:
            print(file_path)

            js_file = file_path
            json_file = js_file + r'.json'
            output_file = js_file + r'_en.js'
            replace_chinese_in_js(js_file, json_file, output_file)
            print(f"替换完成，结果已保存到 {output_file}")

    else:
        print(f"\n在目录 '{target_dir}' 及其子目录下没有找到后缀为 '{file_suffix}' 的文件。")




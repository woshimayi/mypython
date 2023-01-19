#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: 2638288078@qq.com
@software: garner
@file: json-append-tofile.py
@time: 21/2/5 15:30
@desc:
'''
import json
import os


def write_json_test(file, obj):
    '''
    写入/追加json文件
    :param obj:
    :return:
    '''

    # 首先读取已有的json文件中的内容
    item_list = []

    if os.access(file, os.F_OK):
        with open(file, 'r') as f:
            
            load_dict = json.load(f)
            num_item = len(load_dict)
            
            for i in range(num_item):
                id = load_dict[i]['id']
                text = load_dict[i]['text']

                background_color = load_dict[i]['background_color']
                text_color = load_dict[i]['text_color']
                item_dict = {
                    'id': id,
                    'text': text,
                    'background_color': background_color,
                    'text_color': text_color}
                item_list.append(item_dict)

    # 读取已有内容完毕
    # 将新传入的dict对象追加至list中
    item_list.append(obj)
    # 将追加的内容与原有内容写回（覆盖）原文件
    with open(file, 'w', encoding='utf-8') as f2:
        json.dump(item_list, f2, ensure_ascii=False,
                  indent=4,
                  separators=(
                      ',',
                      ':'))



class json_Dof():
    """docstring for json_Dof"""
    def __init__(self, arg):
        super(json_Dof, self).__init__()
        self.file = arg
        self.json_data = ''

    def json_format(self):
        print(json.dumps(self.json_data, sort_keys="true", indent=4, separators=(",", ":")))

    # 读取json 文件为字符串
    def read(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def show(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            print(json.dumps(json.load(f), sort_keys="true", indent=4, separators=(",", ":")))

    # 追加字典到json文件中
    def add(self, obj):
        '''
        写入/追加json文件
        :param obj:
        :return:
        '''
        
        # 首先读取已有的json文件中的内容
        if os.access(self.file, os.F_OK):
            item_list = []
            with open(self.file, 'r') as f:
        
                load_dict = json.load(f)
                print(load_dict)
                # num_item = len(load_dict)
        
                # for i in range(num_item):
                #     url = load_dict[i]['url']
                #     title = load_dict[i]['title']
                #
                #     item_dict = {
                #         'url': url,
                #         'title': title}
                #     item_list.append(item_dict)
                
                for i in range(len(obj)):
                    load_dict.append(obj[i])
                data = load_dict
        else:
            data = obj
            
        # 读取已有内容完毕
        # 将新传入的dict对象追加至list中
        # 将追加的内容与原有内容写回（覆盖）原文件
        with open(self.file, 'w', encoding='utf-8') as f2:
            json.dump(data, f2, ensure_ascii=False,
                      indent=4,
                      separators=(
                          ',',
                          ':'))

    #
    def delete(self, key):
        L = self.find(key)

    # #
    # def change(self, key):
    #
    # #
    # def search(self, key):

    #
    # def find(self, key):
    #     if os.access(self.file, os.F_OK):
    #         with open(self.file, 'r') as f:
    #             array = json.load(f)
    #             print('dict', array)
    #             L = []
    #             for dict in array:
    #                 print('dict:%s, %s' % (dict['url'], dict['title']))
    #                 if key == str(dict.key()) or key == str(dict.value()):
    #                     L.append(dict)
    #
    #             return L
    #     else:
    #         print('file not access')

    def find(self, key):
        if os.access(self.file, os.F_OK):
            with open(self.file, 'r') as f:
                array = json.load(f)
                # print('dict', array)
                L = []
                for dicts in array:
                    L.append(dicts.get(key))
                return L
        else:
            print('file not access')

    # def find(self, key):
    #     with open(self.file, 'r') as f:
    #         array = json.load(f)
    #         dataList = [item.get('name') for item in array]
    #         return dataList


if __name__ == '__main__':
    # obj字典对象为新增内容
    obj = [{"url": 111, "title": "DATEdddd"}]

    # j = json_Dof("labels.json")
    # j.add(obj)
    # j.add(obj)
    # L = j.find("url")
    # J = j.find("title")
    # print(L)
    # print(J)

    j = json_Dof("main.json")
    # L = j.find('options')
    # print(j.read().json_format())
    # print(j.find('options'))
    for i in j.find('options'):
        print(i, type(i))
        if isinstance(i, dict):
            print(i)
        elif isinstance(i, list):
            for lists in i:
                print(lists)
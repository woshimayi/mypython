#!/usr/bin/env python
# encoding: utf-8
'''
@author: woshimayi
@license: (C) Copyright 2015-2049, Node Supply Chain Manager Corporation Limited.
@contact: xxxxxxxx@qq.com
@software: garner
@file: json-append-tofile.py
@time: 21/2/5 15:30
@desc:
'''
import json
import logging
import os

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(funcName)s:line:%(lineno)d] - %(levelname)s:%(message)s')


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

def json_format(data):
    print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))


class json_Dof():
    """docstring for json_Dof"""
    def __init__(self, arg):
        super(json_Dof, self).__init__()
        self.file = arg
        self.json_data = ''

    def json_format(self, data):
        print(json.dumps(data, sort_keys="true", indent=4, separators=(",", ":")))

    # 读取json 文件为字符串
    def read(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            self.json_data = json.dumps(json.load(f))
            return self.json_data

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
                if type(obj) == dict:
                    for key,val in obj.items():
                        load_dict[key] = val
                        # print(key, val)
                elif type(obj) == list:
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


def json_compare(file_1, file_2):
    # print(file_1, file_2)
    f_old = open(file_1, 'r', encoding='utf-8')
    f_new = open(file_2, 'r', encoding='utf-8')

    json_data_old = json.load(f_old)
    json_data_new = json.load(f_new)

    json_data_new_items = json_data_new.items()

    # print(json_data_old_items)
    print(json_data_new_items)

    #  old_items, old_values = json_data_old_items
    # new_items, new_values = json_data_new_items
    # print(old_values, new_values)
    items_key = {}
    for items_new,values_new in json_data_new_items:
        print('-----', items_new)
        item_key = {}
        items_key[items_new] = item_key
        if isinstance(values_new, dict):
            # print(json_data_old[items_new])
            values_old = json_data_old[items_new]

            for item_new,value_new in values_new.items():
                print('\t00000', item_new, value_new)
                ite_key = {}
                item_key[item_new] = ite_key
                try:
                    if item_new in values_old:
                        value_old = values_old[item_new]
                        # print('111111', value_old)
                        for ite_new,valu_new in value_new.items():
                            # print('\t\t22222', ite_new)
                            if ite_new in value_old:
                                if item_new == 'gpon' \
                                        or item_new == 'wlan1' \
                                        or item_new == 'wlan0' \
                                        or 'elements not shown' in item_new:
                                    ite_key[ite_new] = int(valu_new)
                                else:
                                    print('\t\t\t\t', value_old[ite_new], valu_new, end='\t\t\t')
                                    print('\t\t\t', ite_new, int(valu_new) - int(value_old[ite_new]))
                                    ite_vlaue = int(valu_new) - int(value_old[ite_new])
                                    ite_key[ite_new] = ite_vlaue
                            else:
                                if isinstance(valu_new, dict):
                                    ite_key[ite_new] = valu_new
                                else:
                                    ite_key[ite_new] = int(valu_new)

                    else:
                        if isinstance(value_new, dict):
                            item_key[item_new] = value_new
                        else:
                            item_key[item_new] = int(value_new)


                except Exception as e:
                    print(e)



                # if isinstance(value_new, dict):
                #     for ite_new, valu_new in value_new.items():
                #         print('22222', ite_new, valu_new)
                #         print('33333', )
        else:
            print('11111', items_new, values_new)

        j = json_Dof("json_com.json")
        j.add(items_key)





if __name__ == '__main__':

    '''
    # obj字典对象为新增内容
    obj_array = [{"url": 111, "title": "DATEdddd"}]
    obj = {"url": 111, "title": "DATEdddd"}

    print(type(obj))
    if type(obj) == dict:
        print("zzzzz")
    elif type(obj) == list:
        print("list")


    j = json_Dof("labels.json")
    j.add(obj)
    obj = {"url": 111, "title": "DATE"}
    j.add(obj_array)
    # L = j.find("url")
    # J = j.find("title")
    # print(L)
    # print(J)
    
    
    j = json_Dof("main.json")
    L = j.find('options')
    # print(j.read().json_format())
    print(j.find('options'))
    for i in j.find('options'):
        print(i, type(i))
        if isinstance(i, dict):
            print(i)
        elif isinstance(i, list):
            for lists in i:
                print(lists)
    '''

    # old = json_Dof(r'wand_test_record20230302115642.json')
    # new = json_Dof(r'wand_test_record20230302115825.json')
    #
    # # old.show()
    # print(old.read())
    # print(old.json_data)


    # for json_obj in old.json_data:
    #     print(json_obj['bs /b/z'])
    '''
    f_new = open(r'wand_test_record20230302115825.json', 'r', encoding='utf-8')

    with open(r'wand_test_record20230302115642.json', 'r', encoding='utf-8') as f_old:
        json_data_old = json.dumps(json.load(f_old))
        json_data_new = json.dumps(json.load(f_new))

        for items_old,values_old in json.loads(json_data_old).items():
            print("00000", items_old, values_old)
            if isinstance(values_old, dict):
                for item_old,value_old in values_old.items():
                    print('11111', item_old, value_old)
                    if isinstance(value_old, dict):
                        for ite_old,valu_old in value_old.items():
                            print('22222', ite_old, valu_old)
                            if isinstance(int(valu_old), int):
                                print('44444', valu_old)
                    else:
                        print('33333', value_old)

    '''

    json_compare(r'wand_test_record20230307111458.json', r'wand_test_record20230307111607.json')




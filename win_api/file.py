#coding=utf-8

# import os
# import os.path
# print os.name


# print os.path.split('D:\sdf\\sdf\\sdf')  #分离文件
# print os.path.splitext('D:\dfgdf\\dfg.c') #后缀
# print os.path.abspath(".")

# for x in os.listdir("."):
# 	if os.path.isdir(x):
# 		print x
# print '\n'



# for x in os.listdir("D:\python27"):
# 	if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
# 		print x


# #coding:utf8
import os
 
# #判断文件中是否包含关键字，是则将文件路径打印出来
# def is_file_contain_word(file_list, query_word):
#     for _file in file_list:
#         if query_word in open(_file).read():
#             print _file
#     print("Finish searching.")
 
# #返回指定目录的所有文件（包含子目录的文件）               
# def get_all_file(floder_path):
#     file_list = []
#     if floder_path is None:
#         raise Exception("floder_path is None")

#     for dirpath, dirnames, filenames in os.walk(floder_path):
#         for name in filenames:
#             file_list.append(dirpath + '\\' + name)
#     return file_list
    
# query_word = '.py'
# basedir = "D:\\"
 
# is_file_contain_word(get_all_file(basedir), query_word)
# # raw_input("Press Enter to quit.")
print os.walk('D:')
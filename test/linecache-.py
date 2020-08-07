


# import linecache
#
# # line = linecache.getline(r'./123.py',10).split(':')[-1]
# line = linecache.getline(r'./123.py',10)
#
# print('1 ', line)
#
# if 'desc' in line:
# 	print('2',line.split(':')[-1])


def loadDataSet(fileName, splitChar='\t'):
    """
    输入：文件名
    输出：数据集
    描述：从文件读入数据集
    """
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines()[6:]:
            curline = line.strip().split(splitChar)#字符串方法strip():返回去除两侧（不包括）内部空格的字符串；字符串方法spilt:按照制定的字符将字符串分割成序列
            fltline = list(map(float, curline))#list函数将其他类型的序列转换成字符串；map函数将序列curline中的每个元素都转为浮点型
            dataSet.append(fltline)
    return dataSet

# print(loadDataSet(r'123.py', 10))



def getline(file, line):
	f = open(file,'r')
	data = f.readlines()
	# 读取 第一行到第十行内容
	print(data[line-1])
	return data[line-1].split(':')[-1]

desc = getline(r'123.py', 10)
print(desc)
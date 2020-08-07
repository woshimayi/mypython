


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
    ���룺�ļ���
    ��������ݼ�
    ���������ļ��������ݼ�
    """
    dataSet = []
    with open(fileName) as fr:
        for line in fr.readlines()[6:]:
            curline = line.strip().split(splitChar)#�ַ�������strip():����ȥ�����ࣨ���������ڲ��ո���ַ������ַ�������spilt:�����ƶ����ַ����ַ����ָ������
            fltline = list(map(float, curline))#list�������������͵�����ת�����ַ�����map����������curline�е�ÿ��Ԫ�ض�תΪ������
            dataSet.append(fltline)
    return dataSet

# print(loadDataSet(r'123.py', 10))



def getline(file, line):
	f = open(file,'r')
	data = f.readlines()
	# ��ȡ ��һ�е���ʮ������
	print(data[line-1])
	return data[line-1].split(':')[-1]

desc = getline(r'123.py', 10)
print(desc)
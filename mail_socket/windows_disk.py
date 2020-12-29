import psutil,re
disk = str(psutil.disk_partitions())
disk_device = r'device'
for i in re.finditer('device', disk):
	start = i.span()[1] + 2  #盘符字符串起始位置
	end = i.span()[1] + 4    #盘符字符串终止位置
	print(disk[start:end])
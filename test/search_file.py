import os

FindPath = 'D:/'
filename = os.listdir(FindPath)


for file_name in filename:
	fullfilename = os.path.join(FindPath, file_name)
	if fullfilename:
		print(fullfilename)
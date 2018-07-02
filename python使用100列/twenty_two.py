# -*- coding: UTF-8 -*-

# 题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#

h = 0

for i in range(ord('x'), ord('z')+1):
	for j in range(ord('x'), ord('z')+1):
		if i != j:
			for k in range(ord('x'), ord('z')+1):
				if (i != k) and (j != k):
					# print("a\t",chr(i))
					# print("b\t",chr(j))
					# print("c\t",chr(k))
					# print()

					if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
						print("=========")
						print("a\t",chr(i))
						print("b\t",chr(j))
						print("c\t",chr(k))
					h += 1

print(h)
# conding=UTF-8

import os
import sys
L = [34, -54, 45, 54, 32, 78]
print sorted([34, -54, 45, 54, 32, 78])

print sorted([34, -55, 45, 54, 32, 78], key=abs)


print sorted(["asd", "sdf", "dfg", "fgh"])
print sorted(["asd", "sdf", "Dfg", "fgh"])

print sorted(["asd", "sdf", "Dfg", "fgh"], key=str.lower)    

print sorted(["asd", "sdf", "Dfg", "fgh"], key=str.lower, reverse=True) 
print 

def by_sorted(L):
	print L
	
by_sorted(L)

print L
print sorted([34, -54, 45, 54, 32, 78])
print sorted([34, -54, 45, 54, 32, 78], key=by_sorted)
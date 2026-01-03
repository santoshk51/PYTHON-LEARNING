# import array as arr
from array import *

val = array('b',[1,2,3,4,5,6,7,8,9,10])

for i in range(0,len(val)):
	print(val[i], end = " ")

print("\n")

for x in val:
	print(x, end = " ")

print('\n')

print(val.typecode)
print(val.reverse())

for i in range(0, len(val)):
	print(val[i], end = " ")

print('\n')

val.insert(2,50)

for i in range(0, len(val)):
	print(val[i], end = " ")
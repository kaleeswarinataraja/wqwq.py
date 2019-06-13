import math
s1=int(input())
j1=math.log10(s1)/math.log10(2)
if math.ceil(j1)==math.floor(j1):
	print(0)
else:
	mm=(s1-1)//2
	nn=mm*2
	print(s1-nn)

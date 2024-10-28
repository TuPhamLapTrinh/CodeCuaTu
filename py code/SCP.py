# 1 chút về số chính phương
import math
def SCP(x):
	a=int(math.sqrt(x))
	if a*a==x: return True
	return False
def SNT(x):
	if x < 2: 
		return False
	for i in range (2,int(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True
n=int(input("n="))
m=int(input("m="))
if SCP(n) and SNT(m):
	print("YES")
else:
	print("NO")


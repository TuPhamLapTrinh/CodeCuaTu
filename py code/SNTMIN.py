#SNTMIN-LQDCODE
import math
def SNT(x):
	if x < 2 :
		return False
	for i in range(2,int(math.sqrt(x))+1):
		if x % i == 0:
			return False
	return True
n=int(input("Nhập n= "))
j=n+1
while SNT(j)==0: j=j+1
print("Kết quả là: ", j)
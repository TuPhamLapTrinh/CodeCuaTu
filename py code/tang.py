# mảng tăng dần
#giảm dần sử dụng hàm sorted(số cần in ra, reverse = True)
import math
n=int(input("Nhập n: "))
a=[]
for i in range(n):
	a=a+[int(input('Nhập a[%d]= ' %i))]
	a.sort()
print("Mảng đc săp xếp là:",  sorted(a , reverse=True))


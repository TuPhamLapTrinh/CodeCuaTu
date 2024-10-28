# diện tích tam giác 
import math
from math import sqrt
a=int(input("Nhập a= "))
b=int(input("Nhập b= "))
c=int(input("Nhập c= "))
while True:
	if a < 0 and b < 0 and c < 0:
		print("xin mời nhập lại độ dài tại vì độ dài không có âm: ")
		a=int(input("Nhập a= "))
		b=int(input("Nhập b= "))
		c=int(input("Nhập c= "))
	elif a < 0 and b > 0 and c < 0:
		print("xin mời nhập lại độ dài tại vì độ dài không có âm: ")
		a=int(input("Nhập a= "))
		b=int(input("Nhập b= "))
		c=int(input("Nhập c= "))
	elif a > 0 and b < 0 and c > 0:
		print("xin mời nhập lại độ dài tại vì độ dài không có âm: ")
		a=int(input("Nhập a= "))
		b=int(input("Nhập b= "))
		c=int(input("Nhập c= "))
	elif a > 0 and b > 0 and c < 0:
		print("xin mời nhập lại độ dài tại vì độ dài không có âm: ")
		a=int(input("Nhập a= "))
		b=int(input("Nhập b= "))
		c=int(input("Nhập c= "))
	else:
		break
p=(a+b+c)/2
s=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác abc tính bằng công thức heron là:", s)


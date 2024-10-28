# xây dựng một chương trình giải pt bậc 1 bậc 2
# Khai báo hàm giá trị bậc 1
# khai báo hàm giá trị bậc 2
# check hàm bậc 1 và hàm bậc 2
# edit by Pham Anh Tu
# Tú Phạm
# tú phạm lập trình
# test input và output =>> %%111173732889829834822
# test tiếp tục
# nhì vào input ta thấy có xuất hiện các số là : 1 2 3  3 4 5 56 6
#==>> tuwf đây cúng ta suy ra dc các số có cungg phần tử n là: 5 6 7 98
from random import *
import math
def ptb1():
	a=float(input("	Nhap a: "))
	b=float(input("	Nhap b: "))
if a==0:
		if b==0:
			print('phuong trinh vo số nghiem')
		else:	
			print('phuong trinh co vo  nghiem')
else :
		n0=-b/a
		print("phuong trinh co nghiem duy nhat", n0)
return n0
while True:
		print('--------------------------------------------------')
		print(' BANG LUA CHON GIAI PHUONG TRINH BAC 1 VA BAC 2 ')
		print('      1. Giai phuong trinh bac 1       ')
		print('      2. Giai phuong trinh bac 2       ')
		print('      3. Thoat khoi cong viec          ')
		print('--------------------------------------------------')
		chon=input('  Hay chon 1 hoac 2  ')                                                                                                                                                                                                                                         
		if chon=="1":
		 ptb1()	
		elif chon=="2":
			print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")
			# Nhập số a, b và kiểm tra điều kiện khác 0
			a = float(input("Mời bạn nhập hệ số a: "))
			b = float(input("Mời bạn nhập hệ số b: "))
			while True:
				if a == 0 and b == 0:
					print("Một trong hai hệ số a, b phải khác 0: ")
					a = float(input("Mời nhập lại số a: "))
					b = float(input("Mời nhập lại số b: "))
				else:
					break
		# Nhập số c
				c = float(input("Mời bạn nhập hệ số c: "))
		# Tính Delta
				delta = b**2 - 4 * a * c
		# Tìm nghiệm của phương trình
			if delta < 0:
				print("Phương trình vô nghiệm")
			elif delta == 0:
				print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
			else:
				print("Phương trình có hai nghiệm phân biệt:")
				print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
				print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )
else:
	print('	BYE BYE CHÀO TẠM BIỆT BẠN DESIGNER TÚ IT  ')
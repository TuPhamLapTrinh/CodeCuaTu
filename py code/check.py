def  ptb1():
	a=int(input("Nhap a: "))
	b=int(input("Nhap b: "))
	if a!=b:
		print("phuong trinh co nghiem duy nhat", -b/a)
	elif a==b:
		print('phuong trinh co vo so nghiem')
	else :
		print('phuong trinh vo nghiem')
ptb1()
def ptb2():
	a=int(input("Nhap a: "))
	b=int(input("Nhap b: "))
	c=int(input("Nhap c: "))
	d=(b*b)-4*a*c
	if d > 0:
		print("phuong trinh co 2 nghiem" , -b+sqrt(d)/2*a , "va" , -b-sqrt(d)/2*a)
	elif d==0:
		print("phuong trinh co nghiem duy nhat", -b/2*a)
	else :
		print('phuong trinh vo nghiem')
ptb2()
while True:
		print('----------------------------------')
		print('  BANG LUA CHON GIAI PHUONG TRINH BAC 1 VA BAC 2  ')
		print('1. Giai phuong trinh bac 1')
		print('2. Giai phuong trinh bac 2')
		print('3. Thoat khoi cong viec ')
		print('-----------------------------------')
		chon=input(' Hay chon 1 hoac 2 ')
		if chon=="1":
			print('Giai phuong trinh bac 1' )
				ptb1()
		elif chon=="2":
			print('Giai phuong trinh bac 2')
				ptb2()
		else:
			print('Bye')
				break





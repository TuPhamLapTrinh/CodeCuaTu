# tính chỉ số BMI
def BMI (h,w):
	idx=w/(h/100)**2
	print("chỉ số BMI ", idx)
cao=int(input("Nhập chiều cao"))
nang=float(input("Nhap can nặng"))
BMI(cao,nang)

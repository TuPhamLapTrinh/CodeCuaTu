import math
def SCP(n):
	tmp=int(math.sqrt(n))
	if tmp * tmp == n: return True
	return False
st1=int(input('Nhập số tuổi 1:'))
st2=int(input('Nhập số tuổi 2:'))
sn=int(input('Nhập số năm:'))
while True:
	if st1 < 0 or st2 < 0 or sn < 0:
		print('Xin mời bạn nhập lại:')
		st1=int(input('Nhập số tuổi 1:'))
		st2=int(input('Nhập số tuổi 2:'))
		sn=int(input('Nhập số năm:'))
	else:
		break
age1=sn-st1
age2=sn-st2
if SCP(age1) > SCP(age2):
	print("tuổi chính phương của thằng 1 > thằng 2")
elif SCP(age1) < SCP(age2):
	print("tuoi chính phương thằng 1 < thằng 2 ")
else:
	print("2 thằng bằng tuổi nhau")

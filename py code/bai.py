import math
a=[]
dem = 0
dem1 = 0
tong = 0
def SCP(x):
	tmp=int(math.sqrt(x))
	if(tmp*tmp==x): return True
	return False
def SNT(x):
	if x < 2: return False
	for i in range (2,int(math.sqrt(x))+1):    # tại vì sqrt nó định dạng kiểu thực nên nó báo lối interger
		if x % i == 0: return False
	return True
n=int(input('Nhập N='))
for i in range(n):
	a=a+[int(input('Nhập a[%d]=' %i))]
for i in range(n):
	tong=tong+a[i]
for k in range(n):
	if a[k] % 2 ==0:
		dem = dem + 1
for k in range(n):
    if a[k] % 2 !=0:
    	dem1 = dem1 + 1
for i in range(n):
	if(SNT(a[i])): 
		print("Các số nguyên tố trong mảng là:",a[i],"\r")
	else: 
		break
		print("không có số nguyên tô nào") 
		
for i in range(n):
	if(SCP(a[i])): 
		print("Các số chính phương trong mảng là:",a[i],"\r")
	else:
		break
		print("không có số chình phương nào")

print("tổng các phần tử trong mảng là:",tong)
print("số chẵn:",dem)
print("số lẻ:",dem1)



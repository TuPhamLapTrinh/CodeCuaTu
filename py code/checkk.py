#câu 3
n=int(input('N= '))
a=[]
dem=0
for i in range(n):
	a=a+[int(input('Nhap a[%d]=' %i))]
for i in range(n):
	for j in range(i+1):
		if a[i] == a[j]: dem =  dem + 1

print("kết quả là: ", dem)
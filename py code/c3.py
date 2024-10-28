# cùng mình giải câu 3 đề thi chuyên tin tỉnh ninh bình nhé 
# bài này tên là dãy số....
# tên dầu bài ở cuối video
# input nó để là n=4 mảng để lần luot 4,5,6,4
# output in ra là 5
n = int(input("Nhập n: "))
d=0
a=[]
for i in range (n):
	a=a+[int(input('Nhập a[%d]= ' %i))]
for i in range(n):
	for j in range(i+1):
		if a[i]==a[j]:
			d=d+1
print("kết quả là: " , d)

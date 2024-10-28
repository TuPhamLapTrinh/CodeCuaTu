# gà chó
n=int(input("N= "))
m=int(input("M= "))
for i in range(n):
	if i*2+(n-i)*4 == 100:
		print("gà", i)
		print("chó", m-i)
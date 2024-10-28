# bài toán cổ......
n=int(input("Nhập số lượng gà"))
m=int(input("Nhập số lượng chó"))
for i in range (n):
	if i * 2 + ( n - i ) * 4 == 100:
		print("Số gà là : ", i,"\n")
		print("Số chó là: ", (m-i),"\n")
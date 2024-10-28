# bai 16
a=float(input())
b=float(input())
c=float(input())
while True:
	if a < 0 or b < 0 or c < 0:
		print('cú pháp sai')
		a=float(input())
		b=float(input())
		c=float(input())
	else:
		break
if a == b and b == c and c == a:
	print('Tam giác đều')
efif a*a == b and b*b == c and c*c == a:
	print('Tam giác vg cân')
efif a** == b** + c** and b**= a** + c** and c**= a** + b**:
	print("tam giác vuông")
efif a==b or b==c or c==a:
	print('tam giác cân')
efif a > 0 and b > 0 and c > 0:
	print("tam giác thường")
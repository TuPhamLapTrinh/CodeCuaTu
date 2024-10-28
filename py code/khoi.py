n = int(input())
a = n // 10
b = n % 100
if a >= 10:
	print(a,end=' ')
else:
	print('0'+str(a),end=' ')
if b >= 10:
	print(b,end=' ')
else:
	print('0'+str(b),end=' ')
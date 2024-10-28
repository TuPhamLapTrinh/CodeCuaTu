# đếm ước số nguyên...
# cùng học code py với mình nhé ^^
n=int(input("Nhập N :"))
i=2
so_uoc=0
while i <= n/2:
	if n % i ==0: so_uoc=so_uoc+1
	i=i+1
print("số ước: ", so_uoc)

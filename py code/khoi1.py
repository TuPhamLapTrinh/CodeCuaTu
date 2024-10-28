n = int(input())
print(*[n//10 if n//10>=10 else '0'+str(n//10),n%100 if n%100>=10 else '0'+str(n%100)])
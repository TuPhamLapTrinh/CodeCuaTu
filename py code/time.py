# tính thời gian 2 xe gặp nhau
def mtime(d,v1,v2):
	t=v1+v2
	return d/t
d=float(input("nhập d "))
xe1=float(input("nhập vào xe 1 "))
xe2=float(input("nhập vào xe 2 "))
print("thời gian 2 xe găp nhau ",mtime(d,xe1,xe2),"giờ")
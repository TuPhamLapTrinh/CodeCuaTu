# bài tập code python cơ bản
# in ra giai thừa của 1 số n....
def tinhgiaithua(n):
    giai_thua = 1
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua
 
n = int(input("Nhập số nguyên dương n = "))
print(n,"!","=",tinhgiaithua(n))
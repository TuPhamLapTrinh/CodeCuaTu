'''
SNTMIN - Số nguyên tố nhỏ nhất
Dữ liệu vào: standard input
Dữ liệu ra: standard output
Giới hạn thời gian: 1.0 giây
Giới hạn bộ nhớ: 128 megabyte
Đăng bởi: admin
Nhập vào từ bàn phím một số nguyên dương n (n ≤ 108). 
Hãy tìm và in ra màn hình số nguyên tố nhỏ nhất và lớn hơn số n.
nguồn bài : lqdcoder ( cũ )
code python 3.....
'''
# cùng học python với mình nhé : ^^
# bài tập mình đã ghi trên kia ...
import math
def SNT(n):
    if n < 2 :
        return false
    s=math.sqrt(n)
    for i in range (s):
        if s % i == 0 : return false
    return true
n=int(input("Nhập N : "))
j=n+1
while (SNT(j)==0): j=j+1
print("Kết quả là: ", j)
print("---------------------------------------------")
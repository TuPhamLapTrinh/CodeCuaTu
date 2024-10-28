so_nam=int(input("Nhập số năm: "))
Kem=int(input("Nhập số tuổi của kem:"))
Tus=int(input("Nhập số tuổi của tú :"))
so_tuoi_kem=so_nam-Kem
so_tuoi_tu=so_nam-Tus
while True:
   if so_nam < Kem and so_nam < Tus:
      print("Không thể thực hiện Xin Mời")
      Kem=int(input("Nhập lại số tuổi của kem:"))
      Tus=int(input("Nhập lại số tuổi của tú :"))
   else:
      break
if so_tuoi_tu > so_tuoi_kem :
   print("Tu la anh")
elif so_tuoi_tu < so_tuoi_kem:
   print("Kem la anh")
else:
   print("Tú và Kem là 2 anh em sinh cùng năm")
print("-----------------------------------")
print(" kết thúc ")

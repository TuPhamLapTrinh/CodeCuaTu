#bai 22
import math
toan=float(input('Nhập vào điểm toán:'))
van=float(input('Nhập vào điểm văn:'))
anh=float(input('Nhập vào điểm tiếng anh:'))
TBC=(toan+van+anh)/3
if TBC >= 8.0:
	print("Học sinh giỏi")
elif 6.5 <= TBC <= 8.0:
	print("Học sinh khá")
elif 3.5 <= TBC <= 6.5:
	print('Học sinh trung bình')
else:
	print('Học sinh Kém')

# Đọc file JEWELRY.INP
def read_jewelry_input(file_path):
    with open(file_path, 'r') as f:
        x, y = map(int, f.readline().split())  # Đọc x và y
        a = list(map(int, f.readline().split()))  # Đọc mảng a
        b = [list(map(int, line.split())) for line in f]  # Đọc ma trận b
    return x, y, a, b

# Tính tổng giá trị lớn nhất Hiếu có thể thu thập
def max_value(x, y, a, b):
    max_value = 0
    for i in range(len(a)):
        value = a[i]  # Bắt đầu với giá trị từ mảng a
        for j in range(x):
            value += b[i][j]  # Cộng thêm giá trị từ mỗi vòng
        max_value = max(max_value, value)  # Cập nhật giá trị lớn nhất
    return max_value

# Ghi kết quả ra file JEWELRY.OUT
def write_jewelry_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) + '\n')
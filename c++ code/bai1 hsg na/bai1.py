import numpy as np

# Đọc file WAREHOUSE.INP
def read_warehouse_input(file_path):
    with open(file_path, 'r') as f:
        n = int(f.readline().strip())  # Đọc số lượng kho
        cost_matrix = []
        for _ in range(n):
            row = list(map(int, f.readline().strip()))
            cost_matrix.append(row)
        return np.array(cost_matrix)

# Tìm kho có tổng chi phí vận chuyển nhỏ nhất
def find_min_transport_cost(cost_matrix):
    n = len(cost_matrix)
    min_cost = float('inf')
    min_warehouse = -1
    for i in range(n):
        total_cost = np.sum(cost_matrix[i])
        if total_cost < min_cost:
            min_cost = total_cost
            min_warehouse = i + 1  # Vì kho bắt đầu từ 1 (không phải 0)
    return min_warehouse

# Ghi kết quả ra file WAREHOUSE.OUT
def write_warehouse_output(file_path, result):
    with open(file_path, 'w') as f:
        f.write(str(result) + '\n')
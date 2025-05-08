import itertools

# Danh sách ban đầu
lst = [1, 2, 3]

# Tạo tất cả các hoán vị
hoan_vi = list(itertools.permutations(lst))

# In kết quả
print("Tất cả các hoán vị của danh sách [1, 2, 3]:")
for i, p in enumerate(hoan_vi, start=1):
    print(f"{i}: {p}")

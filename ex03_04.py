def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

# Nhập tuples từ người dùng
input_tuple = eval(input("Nhập một tuple (vd: (1, 2, 3)): "))
first, last = truy_cap_phan_tu(input_tuple)

# In ra kết quả
print("Phần tử đầu tiên:", first)
print("Phần tử cuối cùng:", last)
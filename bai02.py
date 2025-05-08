import re

def tinh_tong_so_nguyen(chuoi):
    # Tìm tất cả các số nguyên trong chuỗi (có thể là âm hoặc dương)
    cac_so = re.findall(r'-?\d+', chuoi)

    tong_duong = 0
    tong_am = 0

    for so in cac_so:
        gia_tri = int(so)
        if gia_tri >= 0:
            tong_duong += gia_tri
        else:
            tong_am += gia_tri

    print("Tổng các số dương:", tong_duong)
    print("Tổng các số âm:", tong_am)

# Nhập chuỗi từ người dùng
chuoi_vao = input("Nhập chuỗi chứa các số nguyên: ")
tinh_tong_so_nguyen(chuoi_vao)

def la_so_nguyen_to(n):
    if n <= 1:
        return False  # Các số <= 1 không phải số nguyên tố
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # Nếu chia hết cho i thì không phải nguyên tố
    return True  # Không chia hết cho số nào, là nguyên tố
# Nhập số từ bàn phím
so = int(input("Nhập một số nguyên dương: "))

# Gọi hàm kiểm tra và in kết quả
if la_so_nguyen_to(so):
    print(so, "là số nguyên tố.")
else:
    print(so, "không phải là số nguyên tố.")

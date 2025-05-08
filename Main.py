from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nCHUONG TRINH QUAN LY SINH VIEN")
    print("********************************************************************************")
    print("** 1. Them sinh vien.                                                         **")
    print("** 2. Cap nhat thong tin sinh vien boi ID.                                    **")
    print("** 3. Xoa sinh vien boi ID.                                                   **")
    print("** 4. Tim kiem sinh vien theo ten.                                            **")
    print("** 5. Sap xep sinh vien theo diem trung binh.                                 **")
    print("** 6. Sap xep sinh vien theo ten.                                             **")
    print("** 7. Hien thi danh sach sinh vien.                                           **")
    print("** 0. Thoat                                                                   **")
    print("********************************************************************************")

    try:
        key = int(input("Nhap lua chon: "))
    except ValueError:
        print("Vui long nhap mot so nguyen!")
        continue

    if key == 1:
        print("\n1. Them sinh vien")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong!")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2. Cap nhat thong tin sinh vien.")
            try:
                ID = int(input("Nhap ID: "))
                qlsv.updateSinhVien(ID)
            except ValueError:
                print("ID phai la so nguyen!")
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3. Xoa sinh vien.")
            try:
                ID = int(input("Nhap ID: "))
                if qlsv.deleteById(ID):
                    print(f"\nSinh vien co ID = {ID} da bi xoa!")
                else:
                    print(f"\nSinh vien co ID = {ID} khong ton tai!")
            except ValueError:
                print("ID phai la so nguyen!")
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4. Tim kiem sinh vien theo ten.")
            name = input("Nhap ten sinh vien de tim kiem: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sap xep sinh vien theo diem trung binh (GPA)")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sap xep sinh vien theo ten")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nKhong co sinh vien nao trong danh sach!")

    elif key == 0:
        print("\nBan da chon thoat chuong trinh!")
        break

    else:
        print("\nKhong co chuc nang nay!")

    print("\nHay chon chuc nang trong menu de tiep tuc!")

from SinhVien import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.list_sinh_vien = []

    def generateID(self):
        max_id = 1
        if self.soLuongSinhVien() > 0:
            max_id = max(sv._id for sv in self.list_sinh_vien) + 1
        return max_id

    def soLuongSinhVien(self):
        return len(self.list_sinh_vien)

    def nhapSinhVien(self):
        sv_id = self.generateID()
        name = input("Nhap ten sinh vien: ")
        sex = input("Nhap gioi tinh sinh vien: ")
        major = input("Nhap nganh hoc sinh vien: ")
        diemTB = float(input("Nhap diem trung binh sinh vien: "))
        sv = SinhVien(sv_id, name, sex, major, diemTB)
        self.xepLoaiHocLuc(sv)
        self.list_sinh_vien.append(sv)

    def updateSinhVien(self, ID):
        sv = self.findByID(ID)
        if sv:
            name = input("Nhap ten sinh vien: ")
            sex = input("Nhap gioi tinh sinh vien: ")
            major = input("Nhap nganh hoc sinh vien: ")
            diemTB = float(input("Nhap diem trung binh sinh vien: "))
            sv._name = name
            sv._sex = sex
            sv._major = major
            sv._diemTB = diemTB
            self.xepLoaiHocLuc(sv)
        else:
            print(f"Sinh vien co ID = {ID} khong ton tai.")

    def sortByID(self):
        self.list_sinh_vien.sort(key=lambda x: x._id)

    def sortByName(self):
        self.list_sinh_vien.sort(key=lambda x: x._name)

    def sortByDiemTB(self):
        self.list_sinh_vien.sort(key=lambda x: x._diemTB)

    def findByID(self, ID):
        for sv in self.list_sinh_vien:
            if sv._id == ID:
                return sv
        return None

    def findByName(self, keyword):
        return [sv for sv in self.list_sinh_vien if keyword.upper() in sv._name.upper()]

    def deleteByID(self, ID):
        sv = self.findByID(ID)
        if sv:
            self.list_sinh_vien.remove(sv)
            return True
        return False

    def xepLoaiHocLuc(self, sv: SinhVien):
        if sv._diemTB >= 8:
            sv._hocLuc = "Gioi"
        elif sv._diemTB >= 6.5:
            sv._hocLuc = "Kha"
        elif sv._diemTB >= 5.0:
            sv._hocLuc = "Trung binh"
        else:
            sv._hocLuc = "Yeu"

    def showSinhVien(self, listSV):
        print("{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format("ID", "Name", "Sex", "Major", "Diem TB", "Hoc Luc"))
        for sv in listSV:
            print("{:<8} {:<20} {:<10} {:<15} {:<10} {:<10}".format(sv._id, sv._name, sv._sex, sv._major, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.list_sinh_vien

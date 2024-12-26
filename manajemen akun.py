class Pengguna:
    def __init__(self,nama,email,password):
        self.nama = nama
        self.email = email
        self.password = password
        self.akun = []
            
    def buat_akun(self,email,password):
        self.akun.append({"email":email,"password":password})
        print("akun anda berhasil dibuat")
        
    def login(self):
        print("login untuk melanjutkan sesi berikutnya")
        email = input("masukan email: ")
        password = input("masukan password: ")     
        if {"email":email,"password":password} not in self.akun:
            print(f"email atau password yang anda masukan salah!")
        else:
            print(f"anda berhasil login dengan {self.email}")
                       
class Admin(Pengguna):
    def __init__(self,nama,email,password,jabatan):
        super().__init__(nama,email,password)
        self.jabatan = jabatan
    
    def tambah_akun(self,email,password):
        self.akun.append({"email":email,"password":password})
        print("akun baru berhasil dibuat!")
        
    def hapus_akun(self,email):
        if {"email":email} in self.akun:
            self.akun.remove(email)
    
    def tampilkan_profil(self):
        print(f"nama {self.nama}")
        print(f"email: {self.email}")
        print(f"jabatan: {self.jabatan}")        
            
    def tampilkan_privasi(self):
        for akun in self.akun:
            print(f"email: {akun["email"]}\n password: {akun["password"]}")


def Main():
    print("silahkan buat akun terlebih dahulu")
    nama1 = input("masukan nama kamu: ")
    email1 = input("masukan email kamu: ")
    password1 = input("masukan password kamu: ")
    jabatan1 =  input("masukan jabatan: ")

    objek1 = Admin(nama1,email1,password1,jabatan1)
    objek1.buat_akun(email1,password1)

    
    print(f"selamat Datang Di Database Admin")
    while True:
        print(f"1. Login")
        print(f"2. Tambah akun")
        print(f"3. Hapus akun")
        print(f"4. Tampilkan semua profil")
        print(f"5. Tampilkan privasi akun")
        print(f"6. Exit")
        
        option = input("silahkan pilih menu: ")
        
        if option == "1":
            objek1.login()
        elif option == "2":
            nama2= input("masukan nama kamu: ")
            email2 = input("masukan email kamu: ")
            password2 = input("masukan password kamu: ")
            jabatan2 =  input("masukan jabatan: ")
            objek2 = Admin(nama2,email2,password2,jabatan2)
            objek2.tambah_akun(email2,password2)
        elif option == "3":
            email = input("masukan email untuk dihapus: ")
            objek1.hapus_akun(email)
        elif option == "4":
            objek1.tampilkan_profil()
            objek2.tampilkan_profil()
        elif option == "5":
            objek1.tampilkan_privasi()
            objek2.tampilkan_privasi()
        elif option == "6":
            break
        else:
            print("pilihan tidak sesuai!")
        
    print("anda telah keluar dari Database Admin")
              


Main()        
        


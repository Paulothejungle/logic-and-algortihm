class AkunBank():
    def __init__(self,nomor_rekening,saldo=0):
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo
    
    def deposito(self,jumlah):
        self.jumlah = jumlah
        self.saldo = self.jumlah + self.saldo
        print(f"deposito sebesar: {self.jumlah} berhasil saldo saat ini: {self.saldo}\n")
        
    def penarikan(self,jumlah):
        self.jumlah = jumlah
        if self.jumlah > self.saldo:
            print(f"saldo tidak mencukupi dari penarikan, saldo anda: {self.saldo}")
        else:
            self.saldo -= self.jumlah
            print(f"nama akun: {self.nama}")
            print(f"penarikan berhasil sisa saldo: {self.saldo}\n")
            
    def info_saldo(self):
        print(f"info saldo saat ini: {self.saldo}\n")

class Nasabah(AkunBank):
    def __init__(self,nama,alamat,nomor_rekening,saldo=0):
        super().__init__(nomor_rekening,saldo)
        self.nama = nama
        self.alamat = alamat
        
    def transfer(self,nasabah_tujuan,jumlah):
        if self.saldo < jumlah:
            print(f"transaksi tidak berhasil saldo anda saat ini: {self.saldo}")
        else:
            self.saldo -= jumlah
            nasabah_tujuan.saldo += jumlah
            print(f"saldo berhasil di transfer ke rekening: {nasabah_tujuan.nama}")
            print(f"dengan jumlah: {jumlah}")
            print(f"saldo anda saat ini tersisa: {self.saldo}")
            
    def info_nasabah(self):
        print(f"nama : {self.nama}")
        print(f"alamat : {self.alamat}")
        print(f"nomor rekening: {self.nomor_rekening}")
        print(f"saldo : {self.saldo}\n")
        
def Main():
    print("===== Selamat Datang di Menu BANK MERDEKA =====")
    print("membuat akun nasabah1\n")        
    nama1 = input("masukan nama: ")
    alamat1 = input("masukan alamat: ")
    norek1 = int(input("masukan nomor rekening: "))
    saldo1 = int(input("topup saldo awal anda: "))
    print("\n")

    nasabah1 = Nasabah(nama1,alamat1,norek1,saldo1)
    
    print("membuat akun nasabah2\n")  
    nama2 = input("masukan nama: ")
    alamat2 = input("masukan alamat: ")
    norek2 = int(input("masukan nomor rekening: "))
    saldo2 = int(input("topup saldo awal anda: "))
    print("\n")
    
    nasabah2 = Nasabah(nama2,alamat2,norek2,saldo2)  
    
    
    
    while True:
        print("Silahkan Pilih Menu")
        print("1. informasi")
        print("2. Deposit")
        print("3. Penarikan")
        print("4. Transfer")
        print("5. Keluar Menu\n")
        
        option = input("masukan pilihan: ")
        if option == '1':
            nasabah1.info_nasabah()
            nasabah2.info_nasabah()
        elif option == '2':
            nama = input("\nmasukan nama nasabah untuk deposito: ")
            jumlah = int(input("masukan jumlah deposito: "))
            if nama == nasabah1.nama:
                nasabah1.deposito(jumlah)
            elif nama == nasabah2.nama:
                nasabah2.deposito(jumlah)
            else:
                print("nasabah tidak ditemukan")
        elif option == '3':
            nama = input("\nmasukan nasabah untuk penarikan: ")
            jumlah = int(input("masukan jumlah untuk penarikan: "))
            if nama == nasabah1.nama:
                nasabah1.penarikan(jumlah)    
            elif nama == nasabah2.nama:
                nasabah2.penarikan(jumlah)
            else:
                print("nasabah tidak ditemukan")
        elif option == '4':
            nama_pengirim = input("\nmasukan nama pengirim: ")
            nama_penerima = input("masukan nama penerima: ")
            jumlah = int(input("masukan jumlah yg ditransfer: "))
            if nama_pengirim == nasabah1.nama and nama_penerima == nasabah2.nama:
                nasabah1.transfer(nasabah2,jumlah)
            elif nama_pengirim == nasabah2.nama and nama_penerima == nasabah1.nama:
                nasabah2.transfer(nasabah1,jumlah)
            else:
                print("nama penerima tidak ditemukan")
        elif option == '5':
            print("\nanda telah keluar dari menu BANK")
            break
        else:
            print("input tidak sesuai silahkan input kembali")
    
    
    print("\nterimakasih telah menggunakan layanan kami")
            
    
Main()
                

    


    
    
        
        
        
        
        
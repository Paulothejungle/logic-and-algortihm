class AkunBank():
    def __init__(self,nomor_rekening,saldo=0):
        self.nomor_rekening = nomor_rekening
        self.saldo = saldo
        
    def deposito(self,jumlah):
        
        self.jumlah = jumlah
        self.saldo += self.jumlah
        print(f"saldo anda sekarang: {self.saldo}")
        
    def penarikan(self,jumlah):
        jumlah = int(input("masukan jumlah nominal yang ingin ditarik: "))
        self.jumlah = jumlah
        self.saldo -= self.jumlah
        print(f"sisa saldo anda saat ini: {self.saldo}")
        
    def info_saldo(self):
        print(f"sisa saldo: {self.saldo}")
    
class Nasabah(AkunBank):
    def __init__(self,nama,alamat,nomor_rekening,saldo=0):
        super().__init__(nomor_rekening,saldo)
        self.nama = nama
        self.alamat = alamat
        
    def transfer(self,nasabah_tujuan,jumlah):
        if self.saldo < jumlah:
            print("saldo anda tida mencukupi")
        else:
            self.saldo -= jumlah
            nasabah_tujuan.saldo += jumlah
            print(f"transfer berhasil sisa saldo anda saat ini: {self.saldo}")
            
    def info_nasabah(self):
        print(f"nama: {self.nama}")
        print(f"alamat: {self.alamat}")
        print(f"nomor_rekening: {self.nomor_rekening}")
        print(f"saldo awal: {self.saldo}")
        
nama1 = input("masukan nama: ")
alamat1 = input("masukan alamat: ")
norek1 = int(input("masukan no rekening: "))
saldo1 = int(input("masukan saldo anda: "))

nasabah1 = Nasabah(nama1,alamat1,norek1,saldo1)

nama2 = input("masukan nama: ")
alamat2 = input("masukan alamat: ")
norek2 = int(input("masukan no rekening: "))
saldo2 = int(input("masukan saldo anda: "))
print("\n")

nasabah2 = Nasabah(nama2,alamat2,norek2,saldo2)

nasabah1.info_nasabah()
nasabah2.info_nasabah()
jumlah = int(input("masukan jumlah nominal: "))
nasabah1.deposito(jumlah)
nasabah1.penarikan(jumlah)
jumlah = int(input("masukan nominal yang ingin ditransfer: "))
nasabah1.transfer(nasabah2,jumlah)
nasabah1.info_saldo()
nasabah2.info_saldo()

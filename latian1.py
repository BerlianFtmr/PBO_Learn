class Penyewa:
    def __init__(self, nama, kode_kamar, tipe_kamar, lama_sewa, biaya_listrik):
        self.nama = nama
        self.kode_kamar = kode_kamar
        self.tipe_kamar = tipe_kamar
        self.lama_sewa = lama_sewa
        self.biaya_listrik = biaya_listrik
    
    def hitung_biaya_dasar(self):
        if self.tipe_kamar == 1:
            harga = 2000000
        elif self.tipe_kamar == 2:
            harga = 3500000
        else:
            harga = 5000000

        return harga
    
    def hitung_diskon_loyalitas(self):
        total_diskon = 0
        biaya_dasar = self.hitung_biaya_dasar()
        
        if self.lama_sewa > 6:
            for bulan in range(7, self.lama_sewa + 1):
                if (bulan - 6) % 3 == 0:
                    total_diskon += biaya_dasar * 0.05
        
        return total_diskon
        
    def hitung_total(self):
        total_biaya_sewa = (self.hitung_biaya_dasar() * self.lama_sewa)
        
        return (total_biaya_sewa - self.hitung_diskon_loyalitas()) + self.biaya_listrik

    def cetak_resi(self):
        print("\n========RESI========")
        print(f"Nama Penyewa : {self.nama}")
        print(f"Kode Kamar : {self.kode_kamar}")
        print(f"Tipe Kamar : {self.tipe_kamar}")
        print(f"Lama Sewa : {self.lama_sewa} Bulan")
        print(f"Biaya Listrik : Rp {self.biaya_listrik}")
        print(f"Total Harga : Rp {self.hitung_total()}")

nama, kode_kamar = input("Masukkan Nama penyewa dan Kode kamar: ").split(",")
tipe_kamar = int(input("Masukkan Kode kamar dan Tipe kamar(1/2/3) : "))
lama_sewa = int(input("Masukkan Lama sewa (dalam bulan) : "))
biaya_listrik = int(input("Masukkan Biaya listrik : "))


penyewa = Penyewa(nama, kode_kamar, tipe_kamar, lama_sewa, biaya_listrik)

penyewa.cetak_resi()
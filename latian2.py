class PenyewaanLapangan:
    def __init__(self, jenis_lapangan, durasi_sewa, sewa_sepatu):
        self.jenis_lapangan = jenis_lapangan
        self.durasi_sewa = durasi_sewa
        self.sewa_sepatu = sewa_sepatu
    
    def hitung_tarif_dasar(self):
        if self.jenis_lapangan == "futsal":
            tarif = 150000
        elif self.jenis_lapangan == "basket":
            tarif = 200000
        else:
            tarif = 250000

        return tarif * self.durasi_sewa
    
    def hitung_biaya_sepatu(self):
        tarif_sepatu_normal = 30000
        tarif_sepatu_lembur = 45000

        biaya_sepatu = 0
        if self.sewa_sepatu.lower() == "true":
            if self.durasi_sewa <= 3:
                biaya_sepatu = tarif_sepatu_normal * self.durasi_sewa
            else:
                jam_normal = tarif_sepatu_normal * 3
                jam_lembur = tarif_sepatu_lembur * (self.durasi_sewa - 3)
                biaya_sepatu = jam_normal + jam_lembur
        else:
            biaya_sepatu = 0

        return biaya_sepatu

    def hitung_diskon_member(self):
        tarif_dasar = self.hitung_tarif_dasar()
        diskon = 0

        if self.jenis_lapangan.lower() == "tenis" or self.durasi_sewa > 5:
            diskon = tarif_dasar * 0.15
            
        return diskon
    
    def hitung_total_akhir(self):
        biaya_administrasi = 20000

        total_biaya = self.hitung_tarif_dasar() + self.hitung_biaya_sepatu() + biaya_administrasi - self.hitung_diskon_member()
        return total_biaya

    def cetak_struk(self):
        print("\n========STRUK PENYEWAAN LAPANGAN========")
        print(f"Jenis Lapangan : {self.jenis_lapangan}")
        print(f"Durasi Sewa : {self.durasi_sewa} Jam")
        print(f"Sewa Sepatu : {self.sewa_sepatu}")
        print(f"Tarif Dasar : Rp {self.hitung_tarif_dasar()}")
        print(f"Biaya Sepatu : Rp {self.hitung_biaya_sepatu()}")

        nilai_diskon = self.hitung_diskon_member()

        if nilai_diskon == 0:
            print("Anda belum memenuhi syarat diskon member untuk mendapatkan diskon")
        else:
            print(f"Diskon Member : Rp {nilai_diskon}")
        
        print(f"Biaya Administrasi : Rp {20000}")
        print(f"Total Biaya : Rp {self.hitung_total_akhir():,}")

jenis_lapangan = input("Masukkan jenis lapangan (Futsal/Basket/Tenis) : ")
durasi_sewa = int(input("Masukkan durasi sewa (dalam jam) : "))
sewa_sepatu = input("Apakah Anda ingin menyewa sepatu? (True/False) : ")

penyewaan = PenyewaanLapangan(jenis_lapangan, durasi_sewa, sewa_sepatu)
penyewaan.cetak_struk()
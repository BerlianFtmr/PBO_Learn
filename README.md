# Latihan Soal PBO
## UTS SEMESTER 4
### by IAN

#### Latihan Soal 01

Deskripsi:
Anda diminta membuat program untuk menghitung total tagihan penyewa apartemen. Setiap penyewa memiliki biaya dasar, namun mendapatkan diskon progresif berdasarkan lama mereka menyewa dan tipe kamar yang mereka pilih.

Ketentuan Logika (Class Penyewa):
* Atribut: 
    * nama
    * kode_kamar
    * tipe_kamar (1-3)
    * lama_sewa (bulan)
    * biaya_listrik

Metode hitung_biaya_dasar():
* Tipe 1: Rp 2.000.000
* Tipe 2: Rp 3.500.000
* Tipe 3: Rp 5.000.000

Metode hitung_diskon_loyalitas():
* Diskon hanya diberikan jika lama_sewa > 6 bulan.
* Setiap kelipatan 3 bulan setelah bulan ke-6, penyewa dapat tambahan diskon akumulatif sebesar 5% dari biaya dasar. (Gunakan loop untuk mensimulasikan akumulasi ini).
* Metode hitung_total(): (Biaya Dasar - Total Diskon) + biaya_listrik.
from datetime import datetime as dt
waktu = dt.now()

class Pembayaran:
    def __init__(diri, jl_spp, bulan, nama):
        diri.jl_spp = jl_spp
        diri.bulan = bulan
        diri.nama = nama
        
    def info(diri):
        return f"\nNama Siswa : {diri.nama}\nJumlah Pembayaran SPP : Rp{diri.jl_spp}\nBulan Tagihan : {diri.bulan}\nWaktu Pembayaran : {waktu}"
    
print("=== Program Pembayaran SPP ===")
ulang = int(input("masukkan berapa data yang ingin di masukkan : "))
for i in range(ulang):
    name = input("\nmasukkan nama siswa : ")
    pay = int(input("masukkan jumlah pembayaran : "))
    month = input("masukkan bulan tagihan : ")
    SPP = Pembayaran((pay), (month), (name))

for i in range(ulang):
    print(SPP.info())

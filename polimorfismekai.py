class mobil:
    def suara (self):
        return "mobil membunyikan klakson"
    
class bmw(mobil):
    def suara (self):
        return "tit tit"
    
class porsche(mobil):
    def suara(self):
        return "tot tot"
    
pilih = int(input("masukkan interaksi yang diinginkan\n1 : output\n2 : kosong\npilih : "))
daftar_mobil = [bmw(),porsche(),mobil()]
if pilih == 1:
    for i in daftar_mobil:
        print(i.suara())
    
else:
    pass
class Hewan:
    def suara(self):
        pass
    
class Tio(Hewan):
    def suara(self):
        return "Tio bersuara guk guk"
    
class Ahmad(Hewan):
    def suara(self):
        return "Ahmad bersuara meong"
    
def cetak_suara(objek_hewan):
    print(f"Suara hewan: {objek_hewan.suara()}")
 
while True:
        
    jenis = input("masukkan jenis hewan (tio/ahmad) atau (keluar): ").lower()
    if jenis == "tio":
        hewan = Tio()
        cetak_suara(hewan)
    
    elif jenis == "ahmad":
        hewan = Ahmad()
        cetak_suara(hewan)
    
    elif jenis == "keluar":
        print("program selesai!")
        break
    else:
        print("hewan tidak dikenal")
        continue  

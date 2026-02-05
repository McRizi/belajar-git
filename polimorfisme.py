class Hewan:
    def suara(self):
        return "hewan mengeluarkan suara"
    
class Tio(Hewan):
    def suara(self):
        return "Tio bersuara guk guk"
    
class Ahmad(Hewan):
    def suara(self):
        return "Ahmad bersuara meong"
    
daftar_hewan = [Tio(), Ahmad(), Hewan()]
for i in daftar_hewan:
    print(i.suara())
class Luas:
    def hitung(self, panjang=0, lebar=0):
        if panjang != 0 and lebar != 0 :
            return panjang * lebar
        elif panjang != 0:
            return panjang * panjang
        else:
            return 0
        
l = Luas()
print(l.hitung(5))
print(l.hitung(5, 10))
print(l.hitung())
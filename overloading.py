class Hitung:
    def tambah(self, a=None, b=None, c=None):
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        elif a is not None:
            return a
        else:
            return 0
        
h = Hitung()
print(h.tambah(2, 3))
print(h.tambah(2, 3, 4))
print(h.tambah(10))
print(h.tambah())
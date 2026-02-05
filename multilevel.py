class Orang:
    def __init__(diri, nama, umur):
        diri.nama = nama
        diri.umur = umur
        
    def identitas(diri):
        return f"Nama : {diri.nama}\nUmur : {diri.nama} "
        
class Guru(Orang):
    def __init__(diri, nama, umur, mapel):
        super().__init__(nama, umur)
        diri.mapel = mapel
        
    def ajar(diri):
        return f"{diri.nama} mengajar mata pelajaran {diri.mapel}"
        
class HomeRoom(Guru):
    def __init__(diri, nama, umur, mapel, kelas):
        super().__init__(nama, umur, mapel)
        diri.kelas = kelas
        
    def respon(diri):
        return f"{diri.nama} adalah wali kelas {diri.kelas}"
        
wali_kelas = HomeRoom("pak zen", 27, "dasar dasar PPLG", "X PPLG !")
print(wali_kelas.identitas())
print(wali_kelas.ajar())
print(wali_kelas.respon())
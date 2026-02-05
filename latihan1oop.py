class Siswa:
    def __init__(diri, nama, umur, kelas):
        diri.nama = nama
        diri.umur = umur
        diri.kelas = kelas
        
    def info(diri):
        return f"\n{diri.nama} (umur = {diri.umur} tahun) kelas {diri.kelas}"
    
class Guru:
    def __init__(diri, nama, mapel):
        diri.nama = nama
        diri.mapel = mapel
        
    def info(diri):
        return f"guru yang mengajar mapel {diri.mapel} bernama {diri.nama}"
    
print("=== Data Siswa ===")
name = input("masukkan nama anda : ")
age = input("masukkan umur anda : ")
lass = input("masukkan kelas anda : ")
print("\n=== Data Guru ===")
nameGuru = input("masukkan nama guru yang sedang mengajar : ")
mapel = input("masukkan mapel yang diajarkan : ")

siswa1 = Siswa((name), (age), (lass))
guru1 = Guru((nameGuru), (mapel))
print(siswa1.info())
print(guru1.info())
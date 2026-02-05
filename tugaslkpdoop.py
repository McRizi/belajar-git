class Siswa:
    def __init__(diri, nama, kelas, nilai):
        diri.nama = nama
        diri.kelas = kelas
        diri.nilai = nilai
        
    def tampilkan_data(diri):
        return f"=== Data Siswa ===\nNama : {diri.nama}\nKelas : {diri.kelas}\nNilai : {diri.nilai}"
        
    def status_kelulusan(diri):
        if diri.nilai >= 75 :
            return f"Anda LULUS"
            
        else:
            return "anda belum lulus"
            
siswa1 = Siswa("Faris", "X PPLG 1", 95)
print(siswa1.tampilkan_data())
print(siswa1.status_kelulusan())
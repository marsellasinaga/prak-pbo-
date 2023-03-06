class Mahasiswa:
  def init(self, nama, nim, kelas_siakad, jumlah_sks):
    self.nama = nama
    self.nim = nim
    self.kelas_siakad = kelas_siakad
    self.jumlah_sks = jumlah_sks
    
  def data(self):
    print("Nama: ", self.nama)
    print("NIM: ", self.nim)
    print("Kelas_siakad: ", self.kelas_siakad)
    print("Jumlah_sks: ",self.jumlah_sks)
    
orang = Mahasiswa("marsella", "121140174", "RD", "22")
orang.data()
class NilaiMahasiswa:
    def __init__(self):
        self.data = {}

    def tambah(self, nama, nilai):
        if nama not in self.data:
            self.data[nama] = nilai
            return f"{nama} berhasil ditambahkan dengan nilai {nilai}"
        else:
            return f"{nama} sudah ada"

    def tampilkan(self):
        if len(self.data) == 0:
            return "Belum ada data mahasiswa"
        else:
            output = "Daftar Nilai Mahasiswa:\n"
            for nama, nilai in self.data.items():
                output += f"{nama}: {nilai}\n"
            return output

    def hapus(self, nama):
        if nama in self.data:
            del self.data[nama]
            return f"{nama} berhasil dihapus"
        else:
            return f"{nama} tidak ditemukan"

    def ubah(self, nama, nilai):
        if nama in self.data:
            self.data[nama] = nilai
            return f"{nama} berhasil diubah dengan nilai {nilai}"
        else:
            return f"{nama} tidak ditemukan"


nilai_mahasiswa = NilaiMahasiswa()

# Contoh penggunaan
print(nilai_mahasiswa.tambah("Rusli", 90))
print(nilai_mahasiswa.tambah("Ramfly", 100))
print(nilai_mahasiswa.tambah("Raffli", 100))
print(nilai_mahasiswa.tampilkan())
print(nilai_mahasiswa.ubah("Rusli", 100))
print(nilai_mahasiswa.hapus("Ramfly"))
print(nilai_mahasiswa.tampilkan())
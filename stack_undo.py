class StackUndo:
    def __init__(self):
        self.riwayat_aksi = []

    def simpan_aksi(self, aksi):
        self.riwayat_aksi.append(aksi)
        print(f"Aksi disimpan: '{aksi}'")

    def undo_aksi(self):
        if self.riwayat_aksi:
            aksi_terakhir = self.riwayat_aksi.pop()
            print(f"UNDO BERHASIL: Membatalkan aksi '{aksi_terakhir}'")
        else:
            print("Tidak ada aksi untuk di-undo.")

if __name__ == "__main__":
    sistem = StackUndo()
    sistem.simpan_aksi("Menambah data mahasiswa: Ahya")
    sistem.simpan_aksi("Memasukkan antrean: Mutiara")
    
    sistem.undo_aksi()
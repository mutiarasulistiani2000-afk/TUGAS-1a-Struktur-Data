from collections import deque

class QueueAntrean:
    def __init__(self):
        self.antrean = deque()

    def tambah_antrean(self, tugas):
        self.antrean.append(tugas)
        print(f"Tugas '{tugas}' masuk ke antrean.")

    def proses_antrean(self):
        if self.antrean:
            tugas_diproses = self.antrean.popleft()
            print(f"Sedang memproses antrean: {tugas_diproses}")
        else:
            print("Antrean kosong.")

if __name__ == "__main__":
    sistem = QueueAntrean()
    sistem.tambah_antrean("Verifikasi KRS Ahmad")
    sistem.tambah_antrean("Input Nilai Citra")
    
    sistem.proses_antrean()
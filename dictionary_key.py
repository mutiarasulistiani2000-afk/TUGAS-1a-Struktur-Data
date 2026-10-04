import time

class DictionaryKey:
    def __init__(self):
        self.data_by_key = {}

    def tambah_data(self, nim, nama, prodi, ipk, predikat):
        self.data_by_key[nim] = {
            "NIM": nim,
            "Nama": nama,
            "Prodi": prodi,
            "IPK": ipk,
            "Predikat": predikat
        }

    def cari_data(self, nim_cari):
        print(f"\n=== FIND DATA ===")
        waktu_mulai = time.perf_counter() 
        
        hasil = self.data_by_key.get(nim_cari)
        
        waktu_selesai = time.perf_counter() 
        durasi = waktu_selesai - waktu_mulai
        
        if hasil:
            print(f"Data '{hasil['Nama']}' berada pada NIM: {nim_cari}")
        else:
            print(f"Data dengan NIM {nim_cari} tidak ditemukan.")
            
        print(f"Waktu: {durasi:.8f} detik")

if __name__ == "__main__":
    sistem = DictionaryKey()
    sistem.tambah_data("12450120341", "Mutiara Sulistiani", "Teknik Informatika", "3.50", "")
    
    sistem.cari_data("12450120341")
class ArrayMahasiswa:
    def __init__(self):
        self.data_berurutan = []

    def tambah_data(self, nim, nama, prodi, ipk, predikat):
        data_mhs = {
            "NIM": nim,
            "Nama": nama,
            "Prodi": prodi,
            "IPK": ipk,
            "Predikat": predikat
        }
        self.data_berurutan.append(data_mhs)

    def tampilkan_data(self):
        for index, mhs in enumerate(self.data_berurutan, start=1):
            print("====================")
            print(f"Indeks   : {index}")
            print(f"NIM      : {mhs['NIM']}")
            print(f"Nama     : {mhs['Nama']}")
            print(f"Prodi    : {mhs['Prodi']}")
            print(f"IPK      : {mhs['IPK']}")
            print(f"Predikat : {mhs['Predikat']}")
        print("====================")

if __name__ == "__main__":
    sistem = ArrayMahasiswa()
    sistem.tambah_data("12450120341", "Mutiara Sulistiani", "Teknik Informatika", "3.50", "Memuaskan")
    sistem.tambah_data("12450120192", "Dzikra Ahya Tsabitah", "Sistem Informasi", "3.66", "Sangat Memuaskan")
    sistem.tambah_data("12450278590", "Melisa Amanda", "Teknik Informatika", "3.80", "Cumlaude")
    
    sistem.tampilkan_data()
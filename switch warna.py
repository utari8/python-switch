def warna(pilih):
    def merah():
        return "Bahaya, Gairah, Kegembiraan, & Energi"
    def putih():
        return "Kemurnian, Sederhana, Tidak Bersalah & Minimalisme"
    def biru():
        return "Komunikatif, Dapat Dipercaya, Menenangkan & Depresi"
    def kuning():
        return "Optimistis, Ceria, Menyenangkan dan Bahagia"
    def hitam():
        return "Canggih, Formal, Mewah & Sedih"

    switcher = {
        1:merah(),
        2:putih(),
        3:biru(),
        4:kuning(),
        5:hitam()
    }

    return switcher.get(pilih, "Invalid option")
print("Arti Warna : ")
print("1. Merah")
print("2. Putih")
print("3. Biru")
print("4. Kuning")
print("5. Hitam")

if __name__ == "__main__":
    ino = int(input("Pilih Nomor warna: "))
    
    # ino = 1
    if ino == 1:
        print(warna(1))
    elif ino == 2:
        print(warna(2))
    elif ino == 3:
        print(warna(3))
    elif ino == 4:
        print(warna(4))
    elif ino == 5:
        print(warna(5))
    



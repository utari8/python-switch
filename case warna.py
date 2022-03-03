def warna(pilih):
    match pilih:
        case 0:
            return "merah"
        case 1:
            return "putih"
        case 2:
            return "kuning"
        case 3:
            return "hitam"

if __name__ == "__main__":
    pilih = 2
    print(warna(pilih))
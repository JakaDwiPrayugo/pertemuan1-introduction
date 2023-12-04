def hitung_luas(panjang, lebar, tinggi):
    a = panjang * lebar
    b = panjang * tinggi
    c = lebar * tinggi
    d = a + b + c
    luas = 2 * d
    return luas

def hitung_keliling(panjang, lebar, tinggi):
    keliling = 4 * (panjang + lebar + tinggi)
    return keliling

def hitung_volume(panjang, lebar, tinggi):
    volume = panjang * lebar * tinggi
    return volume

def main():
    panjang = float(input("Masukkan panjang balok: "))
    lebar = float(input("Masukkan lebar balok: "))
    tinggi = float(input("Masukkan tinggi balok: "))

    print("Selamat Datang di Matematika Balok")
    print("Pilih operasi:")
    print("1. Hitung Luas")
    print("2. Hitung Keliling")
    print("3. Hitung Volume")

    pilihan = int(input("Masukkan nomor operasi: "))

    if pilihan == 1:
        hasil = hitung_luas(panjang, lebar, tinggi)
        print("Luas Balok:", hasil)
    elif pilihan == 2:
        hasil = hitung_keliling(panjang, lebar, tinggi)
        print("Keliling Balok:", hasil)
    elif pilihan == 3:
        hasil = hitung_volume(panjang, lebar, tinggi)
        print("Volume Balok:", hasil)
    else:
        print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

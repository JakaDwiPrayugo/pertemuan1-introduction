def total_diskon(total_pesanan):
    if total_pesanan > 100000:
        diskon = min(0.5 * total_pesanan, 50000)
    elif total_pesanan > 30000:
        diskon = min(0.3 * total_pesanan, 30000)
    else:
        diskon = 0
    return diskon

if __name__ == "__main__":
    total_pesanan = float(input("Masukkan total pesanan: "))
    diskon = total_diskon(total_pesanan)
    total_bayar = total_pesanan - diskon

    print(f"Total bayar setelah diskon: {total_bayar:.2f}")

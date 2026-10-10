def generator_suhu(mulai=15.0, akhir=38.0, langkah=1.5):
    """Menghasilkan data suhu satu per satu menggunakan yield."""
    suhu = mulai

    while suhu <= akhir:
        yield round(suhu, 1)
        suhu += langkah


def kategori_suhu(suhu):
    """Menentukan kategori berdasarkan nilai suhu."""
    if suhu < 20:
        return "Dingin"
    elif suhu <= 30:
        return "Normal"
    else:
        return "Panas"


def main():
    # Membuat iterator dari generator suhu
    sensor = generator_suhu()

    print("=== STREAMING DATA SENSOR IoT ===")
    print("Data diproses satu per satu tanpa menyimpan seluruh data ke list.\n")

    nomor = 1

    while True:
        try:
            # Mengambil satu data suhu dari generator
            suhu = next(sensor)

            # Menentukan kategori suhu
            status = kategori_suhu(suhu)

            # Menampilkan hasil pembacaan
            print(
                f"Pembacaan ke-{nomor:02d} | "
                f"Suhu: {suhu:>4.1f} °C | "
                f"Status: {status}"
            )

            nomor += 1

        except StopIteration:
            # Berhenti ketika semua data telah dihasilkan
            break

    print("\nGenerator sudah selesai menghasilkan data.")


if __name__ == "__main__":
    main()
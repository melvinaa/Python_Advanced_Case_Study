data_mahasiswa = [
    {"nama": "Ana", "nim": "240101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Bella", "nim": "240102", "tugas": 70, "uts": 65, "uas": 80},
    {"nama": "Cahaya", "nim": "240103", "tugas": 91, "uts": 85, "uas": 92},
    {"nama": "Doni", "nim": "240104", "tugas": 75, "uts": 82, "uas": 80},
    {"nama": "Ella", "nim": "240105", "tugas": 95, "uts": 85, "uas": 94},
]

# List comprehension: menghitung dan menambahkan nilai akhir.
data_nilai = [
    {
        **mhs,
        "nilai_akhir": round(
            mhs["tugas"] * 0.30 +
            mhs["uts"] * 0.30 +
            mhs["uas"] * 0.40,
            2
        )
    }
    for mhs in data_mahasiswa
]

# Filtering Pythonic: mahasiswa dengan nilai akhir > 80.
berprestasi = [mhs for mhs in data_nilai if mhs["nilai_akhir"] > 80]

# Sorting menggunakan sorted() dan lambda.
ranking = sorted(data_nilai, key=lambda mhs: mhs["nilai_akhir"], reverse=True)

print("=== ANALISIS NILAI MAHASISWA ===")
print("Bobot: Tugas 30% | UTS 30% | UAS 40%\n")

print("Daftar Nilai Akhir:")
for i, mhs in enumerate(data_nilai, start=1):
    print(
        f"{i}. {mhs['nama']} ({mhs['nim']}) - "
        f"Tugas: {mhs['tugas']}, UTS: {mhs['uts']}, UAS: {mhs['uas']} "
        f"=> Nilai Akhir: {mhs['nilai_akhir']}"
    )

print("\nMahasiswa Berprestasi (nilai akhir > 80):")
for mhs in berprestasi:
    print(f"- {mhs['nama']} ({mhs['nim']}) : {mhs['nilai_akhir']}")

print("\n=== RANKING ===")
for posisi, mhs in enumerate(ranking, start=1):
    print(f"{posisi}. {mhs['nama']} - {mhs['nilai_akhir']}")

terbaik = ranking[0]
print("\n=== MAHASISWA TERBAIK ===")
print(f"Nama        : {terbaik['nama']}")
print(f"NIM         : {terbaik['nim']}")
print(f"Tugas       : {terbaik['tugas']}")
print(f"UTS         : {terbaik['uts']}")
print(f"UAS         : {terbaik['uas']}")
print(f"Nilai Akhir : {terbaik['nilai_akhir']}")

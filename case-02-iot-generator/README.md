# Case 02 — Streaming Data Sensor IoT

## Masalah
Program mensimulasikan pembacaan suhu secara bertahap sehingga data tidak perlu disimpan seluruhnya dalam list.

## Konsep
- Iterator pattern.
- Generator function dengan `yield`.
- `next()` untuk mengambil data satu per satu.
- Efisiensi memori dengan menghindari list besar.

## Kategori
- Dingin: < 20°C
- Normal: 20–30°C
- Panas: > 30°C

## Cara menjalankan
```bash
python main.py
```

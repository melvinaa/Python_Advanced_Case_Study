# Case 03 — Sistem Keamanan Akun & Audit Log

## Masalah
Program memvalidasi username dan password dengan RegEx, menggunakan class `User` dengan `@property`, serta mencatat setiap percobaan login melalui decorator.

## Konsep
- RegEx (`re`) untuk validasi.
- `@property` untuk enkapsulasi.
- Decorator untuk audit log.
- Timestamp untuk mencatat waktu percobaan.

## Cara menjalankan
```bash
python main.py
```

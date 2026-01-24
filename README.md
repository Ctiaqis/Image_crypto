# 🔐 Image Crypto

Aplikasi web untuk menyembunyikan pesan rahasia di dalam gambar menggunakan kombinasi **Kriptografi Klasik** dan **Steganografi Modern**.

## ✨ Fitur

- 🔒 **Vigenère Cipher** - Enkripsi teks dengan algoritma klasik
- 🖼️ **LSB Steganography** - Menyembunyikan pesan di dalam piksel gambar
- 📤 **Upload & Download** - Kelola gambar dengan mudah
- 🔍 **Reveal Message** - Ekstrak dan dekripsi pesan tersembunyi
- 💾 **Database MySQL** - Menyimpan riwayat gambar

## 🛠️ Teknologi

| Komponen | Teknologi |
|----------|-----------|
| Backend | Flask (Python) |
| Enkripsi | Vigenère Cipher |
| Steganografi | LSB (Least Significant Bit) |
| Database | MySQL |
| Frontend | Bootstrap 5 |

## 🔬 Cara Kerja

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│  Plaintext  │ -> │   Vigenère   │ -> │ Ciphertext  │
│   "HELLO"   │    │   Encrypt    │    │  "RIJVS"    │
└─────────────┘    └──────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌──────────────┐    ┌─────────────┐
│ Stego Image │ <- │  LSB Hide    │ <- │   Binary    │
│   (PNG)     │    │  in Pixels   │    │ "01010..."  │
└─────────────┘    └──────────────┘    └─────────────┘
```

---

Made with ❤️ for UAS Kriptografi

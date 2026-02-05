# 🔐 Image Crypto

Aplikasi web untuk menyembunyikan pesan rahasia di dalam gambar menggunakan kombinasi **Kriptografi Klasik** dan **Steganografi Modern**.

Proyek ini dibuat untuk mendemonstrasikan teknik pengamanan informasi dengan menggabungkan dua metode keamanan data:

| Metode | Kategori | Fungsi |
|:-------|:---------|:-------|
| **Vigenère Cipher** | Kriptografi Klasik | Mengenkripsi pesan teks menjadi ciphertext yang tidak bisa dibaca |
| **LSB Steganography** | Steganografi Modern | Menyembunyikan pesan terenkripsi ke dalam piksel gambar |

### 🎯 Tujuan Pembuatan
- Memahami implementasi algoritma **Vigenère Cipher** secara praktis
- Mempelajari teknik **LSB (Least Significant Bit)** dalam steganografi
- Membuat aplikasi web yang dapat mengamankan pesan secara **dua lapis** (enkripsi + penyembunyian)

### 💡 Mengapa Kombinasi Ini?
> Dengan menggabungkan kriptografi dan steganografi, pesan tidak hanya **diacak** (encrypted) tetapi juga **disembunyikan** dalam media gambar. Sehingga orang lain tidak akan curiga bahwa ada pesan rahasia di dalam gambar tersebut.

---

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-3.x-green?style=for-the-badge&logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL"/>
  <img src="https://img.shields.io/badge/Bootstrap-5-purple?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap"/>
</p>

<h1 align="center">�️ Preview Aplikasi</h1>

<p align="center">
  <b>Aplikasi Web untuk Menyembunyikan Pesan Rahasia dalam Gambar</b><br>
  <i>Menggunakan Kombinasi Kriptografi Klasik & Steganografi Modern</i>
</p>

<p align="center">
  <a href="#-fitur">Fitur</a> •
  <a href="#-teknologi">Teknologi</a> •
  <a href="#-cara-kerja">Cara Kerja</a> •
  <a href="#-instalasi">Instalasi</a> •
  <a href="#-penggunaan">Penggunaan</a>
</p>

---

## ✨ Fitur

| Fitur | Deskripsi |
|:------|:----------|
| 🔒 **Vigenère Cipher** | Enkripsi teks dengan algoritma kriptografi klasik |
| 🖼️ **LSB Steganography** | Menyembunyikan pesan di dalam piksel gambar secara tak terlihat |
| 📤 **Upload & Download** | Kelola gambar dengan antarmuka yang mudah digunakan |
| 🔍 **Reveal Message** | Ekstrak dan dekripsi pesan tersembunyi dari gambar |
| 💾 **Database MySQL** | Menyimpan riwayat gambar yang telah diproses |

---

## 🛠️ Teknologi

<table>
  <tr>
    <td align="center"><b>🐍 Backend</b></td>
    <td align="center"><b>🔐 Enkripsi</b></td>
    <td align="center"><b>🎨 Steganografi</b></td>
    <td align="center"><b>🗄️ Database</b></td>
    <td align="center"><b>💅 Frontend</b></td>
  </tr>
  <tr>
    <td align="center">Flask (Python)</td>
    <td align="center">Vigenère Cipher</td>
    <td align="center">LSB (Least Significant Bit)</td>
    <td align="center">MySQL</td>
    <td align="center">Bootstrap 5</td>
  </tr>
</table>

---

## 🔬 Cara Kerja

### Proses Enkripsi & Penyembunyian Pesan

```
┌───────────────────────────────────────────────────────────────────────────┐
│                            PROSES ENCODE                                   │
├───────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│   📝 Plaintext          🔑 Vigenère           🔤 Ciphertext               │
│   ┌─────────────┐      ┌──────────────┐      ┌─────────────┐            │
│   │   "HELLO"   │  ──▶ │   Encrypt    │  ──▶ │  "RIJVS"    │            │
│   └─────────────┘      └──────────────┘      └─────────────┘            │
│                                                     │                     │
│                                                     ▼                     │
│   🖼️ Stego Image        💾 LSB Hide           📊 Binary                  │
│   ┌─────────────┐      ┌──────────────┐      ┌─────────────┐            │
│   │  (PNG)      │  ◀── │  in Pixels   │  ◀── │ "01010..."  │            │
│   └─────────────┘      └──────────────┘      └─────────────┘            │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

### Penjelasan Algoritma

1. **Vigenère Cipher** - Pesan asli (plaintext) dienkripsi menggunakan kunci rahasia
2. **Konversi Binary** - Hasil enkripsi diubah menjadi format biner (0 dan 1)
3. **LSB Embedding** - Bit-bit pesan disisipkan ke dalam bit terakhir (LSB) setiap channel warna piksel
4. **Output PNG** - Gambar disimpan dalam format PNG (lossless) untuk menjaga integritas data

---

##  Struktur Proyek

```
📦 Image_crypto
├── 📄 app.py              # Main Flask application
├── 📄 database.sql        # Database schema
├── 📄 README.md           # Documentation
├── 📁 static/
│   └── 📁 uploads/        # Uploaded images storage
└── 📁 templates/
    ├── 📄 index.html      # Homepage
    ├── 📄 upload.html     # Upload form
    └── 📄 reveal.html     # Reveal message page
```

---

## ⚠️ Catatan Penting

> **🔐 Keamanan Kunci:** Simpan kunci enkripsi dengan aman. Tanpa kunci yang benar, pesan tidak dapat didekripsi.

> **🖼️ Format Gambar:** Gambar output selalu dalam format PNG untuk menjaga kualitas dan integritas data steganografi.

> **📏 Kapasitas Pesan:** Panjang pesan yang dapat disembunyikan tergantung pada ukuran gambar (lebih besar = lebih banyak kapasitas).

---

## 📜 Lisensi

Proyek ini dibuat untuk keperluan **UAS Kriptografi**.

---

<p align="center">
  Made with ❤️ for UAS Kriptografi
</p>

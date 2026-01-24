from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os
from werkzeug.utils import secure_filename
from PIL import Image  # untuk manipulasi piksel manual

app = Flask(__name__)
app.secret_key = "kuncirahasiaaplikasi"

# --- KONFIGURASI ---
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# ==========================================
# BAGIAN 1: METODE KLASIK (Vigenère Cipher)
# ==========================================
def vigenere_encrypt(plaintext, key):
    key = key.upper()
    plaintext = plaintext.upper()
    ciphertext = []
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            ciphertext.append(encrypted_char)
            key_index += 1
        else:
            ciphertext.append(char)
    return "".join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    ciphertext = ciphertext.upper()
    plaintext = []
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 65
            decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            plaintext.append(decrypted_char)
            key_index += 1
        else:
            plaintext.append(char)
    return "".join(plaintext)

# ==========================================
# BAGIAN 2: METODE MODERN MANUAL (LSB)
# ==========================================

# Helper: Ubah Teks jadi Deretan Bit (010101...)
def text_to_bits(text):
    bits = bin(int.from_bytes(text.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

# Helper: Ubah Deretan Bit balik jadi Teks
def text_from_bits(bits):
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
    except:
        return ""

# FUNGSI MANUAL: Menyembunyikan Pesan ke Piksel
def manual_hide(image_path, secret_text, output_path):
    img = Image.open(image_path)
    # Penting: Tambahkan 'DELIMITER' (tanda berhenti) unik di akhir pesan
    # Supaya nanti program tau kapan harus berhenti membaca bit.
    full_message = secret_text + "#####" 
    
    bits = text_to_bits(full_message)
    data_index = 0
    
    # Ambil data semua piksel
    img = img.convert("RGB") # Pastikan format RGB
    pixels = list(img.getdata())
    new_pixels = []

    for pixel in pixels:
        new_pixel = list(pixel) # Contoh: [200, 150, 50] (R, G, B)
        
        # Loop R, G, B (3 channel warna)
        for i in range(3): 
            if data_index < len(bits):
                # Logika Bitwise:
                # 1. pixel[i] & ~1  -> Mematikan bit terakhir (jadi 0)
                # 2. | int(bits...) -> Mengisi bit terakhir dengan bit pesan kita
                new_pixel[i] = (new_pixel[i] & ~1) | int(bits[data_index])
                data_index += 1
        
        new_pixels.append(tuple(new_pixel))

    # Simpan gambar baru
    new_img = Image.new("RGB", img.size)
    new_img.putdata(new_pixels)
    new_img.save(output_path, "PNG") # Wajib PNG agar lossless

# FUNGSI MANUAL: Membaca Pesan dari Piksel
def manual_reveal(image_path):
    img = Image.open(image_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())
    
    bits = ""
    for pixel in pixels:
        for i in range(3): # Cek R, G, B
            # Ambil sisa bagi 2 (0 atau 1) -> itulah bit LSB
            bits += str(pixel[i] % 2)

    # Coba konversi bit ke teks setiap 8 bit (1 byte)
    # Kita cari tanda "#####"
    found_text = ""
    # Loop per 8 karakter biner
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        # Jika sisa bit kurang dari 8, break
        if len(byte) < 8: break
        
        char = text_from_bits(byte)
        found_text += char
        
        # Cek apakah tanda berhenti ketemu?
        if found_text.endswith("#####"):
            return found_text[:-5] # Hapus tanda ##### dan kembalikan pesan
            
    return None # Gagal menemukan pesan

# ==========================================
# ROUTES & DATABASE
# ==========================================
def get_db_connection():
    return mysql.connector.connect(
        host="localhost", user="root", password="", database="stego_db"
    )

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM images ORDER BY upload_time DESC")
    images = cursor.fetchall()
    conn.close()
    return render_template('index.html', images=images)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files: return redirect(request.url)
        file = request.files['file']
        message = request.form['message']
        key = request.form['key']
        desc = request.form['description']

        if file.filename == '' or not file: return redirect(request.url)

        filename = secure_filename(file.filename)
        temp_path = os.path.join(app.config['UPLOAD_FOLDER'], "temp_" + filename)
        file.save(temp_path)

        try:
            # 1. Enkripsi Vigenere (Klasik)
            encrypted_msg = vigenere_encrypt(message, key)

            # 2. Steganografi Manual (Modern)
            final_filename = "secret_" + os.path.splitext(filename)[0] + ".png"
            final_path = os.path.join(app.config['UPLOAD_FOLDER'], final_filename)
            
            # Panggil fungsi manual kita
            manual_hide(temp_path, encrypted_msg, final_path)
            
            os.remove(temp_path) # Hapus file temp
            
            # Simpan ke DB
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO images (filename, description) VALUES (%s, %s)", (final_filename, desc))
            conn.commit()
            conn.close()
            
            flash('Berhasil! Pesan disisipkan dengan metode Manual LSB.', 'success')
            return redirect(url_for('index'))
        
        except Exception as e:
            flash(f'Gagal: {e}', 'error')
            return redirect(request.url)

    return render_template('upload.html')

@app.route('/reveal/<int:image_id>', methods=['GET', 'POST'])
def reveal(image_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM images WHERE id = %s", (image_id,))
    image_data = cursor.fetchone()
    conn.close()

    decrypted = None
    raw_data = None

    if request.method == 'POST':
        key = request.form['key']
        path = os.path.join(app.config['UPLOAD_FOLDER'], image_data['filename'])

        try:
            # 1. Ekstrak Manual LSB
            raw_data = manual_reveal(path)
            
            if raw_data:
                # 2. Dekripsi Vigenere
                decrypted = vigenere_decrypt(raw_data, key)
            else:
                flash("Pesan tidak ditemukan atau file rusak.", "warning")
        
        except Exception as e:
            flash(f"Error: {e}", "error")

    return render_template('reveal.html', image=image_data, message=decrypted, raw=raw_data)

if __name__ == '__main__':
    app.run(debug=True)
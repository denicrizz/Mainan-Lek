# Permainan Batu Gunting Kertas Menggunakan OpenCV dan CVZone

Permainan ini adalah implementasi sederhana dari game **Batu Gunting Kertas** menggunakan kamera komputer, **OpenCV**, dan **CVZone** untuk mendeteksi gestur tangan pemain.

---

## Fitur Utama
- Menggunakan kamera untuk menangkap gerakan tangan pemain.
- AI memilih gerakan secara acak (Batu, Gunting, Kertas).
- Menampilkan skor pemain dan AI secara real-time.
- Deteksi jari menggunakan **HandTrackingModule** dari **CVZone**.
- Waktu hitung mundur untuk setiap putaran permainan.

---

## Prasyarat
Sebelum menjalankan permainan, pastikan Anda telah menginstall pustaka Python berikut:

- **OpenCV**
- **CVZone**
- **Mediapipe**

Anda dapat menginstall semua pustaka ini menggunakan file `requirements.txt` berikut:

```plaintext
opencv-python
cvzone
mediapipe
```

Jalankan perintah berikut untuk menginstall pustaka:

```bash
pip install -r requirements.txt
```

---

## Struktur Direktori
Pastikan struktur direktori Anda terlihat seperti ini:

```
.
├── app.py                # File Python utama
├── Resources             # Folder untuk menyimpan gambar
│   ├── BG.png            # Latar belakang permainan
│   ├── 1.png             # Gambar AI untuk "Batu"
│   ├── 2.png             # Gambar AI untuk "Kertas"
│   ├── 3.png             # Gambar AI untuk "Gunting"
└── requirements.txt      # File untuk menginstall pustaka
```

**Keterangan:**
- **BG.png**: Gambar latar belakang permainan.
- **1.png**, **2.png**, **3.png**: Gambar yang digunakan AI untuk menunjukkan gerakannya (Batu, Kertas, Gunting).

---

## Cara Menjalankan
1. Pastikan kamera Anda aktif dan dapat digunakan.
2. Simpan file `app.py` di direktori utama proyek Anda.
3. Jalankan file Python menggunakan perintah berikut:
   ```bash
   python app.py
   ```

---

## Instruksi Bermain
1. Setelah program dimulai, jendela permainan akan muncul.
2. Tekan tombol **'S'** pada keyboard untuk memulai permainan.
3. Letakkan tangan Anda di depan kamera dan lakukan salah satu gestur berikut:
   - **Batu**: Tidak ada jari yang terbuka.
   - **Kertas**: Semua jari terbuka.
   - **Gunting**: Hanya dua jari tengah yang terbuka (seperti simbol peace ✌️).
4. AI akan memilih gerakannya secara acak (Batu, Gunting, atau Kertas).
5. Skor pemain dan AI akan ditampilkan pada layar.
6. Tekan tombol **'Q'** pada keyboard untuk keluar dari permainan.

---

## Penjelasan Logika Permainan
1. **Deteksi Tangan**:
   - Menggunakan **CVZone HandTrackingModule** untuk mendeteksi jumlah jari yang terbuka.
   - **Gerakan pemain** ditentukan berdasarkan pola jari yang terdeteksi:
     - **[0, 0, 0, 0, 0]**: Batu
     - **[1, 1, 1, 1, 1]**: Kertas
     - **[0, 1, 1, 0, 0]**: Gunting
2. **Gerakan AI**:
   - AI memilih gerakan secara acak menggunakan fungsi `random.randint(1, 3)`:
     - 1: Batu
     - 2: Kertas
     - 3: Gunting
3. **Penentuan Pemenang**:
   - Logika menang/kalah berdasarkan aturan klasik:
     - **Batu menang melawan Gunting**
     - **Kertas menang melawan Batu**
     - **Gunting menang melawan Kertas**
   - Skor diperbarui sesuai hasil putaran.
4. **Tampilan Layar**:
   - Skor pemain dan AI ditampilkan secara real-time di layar.
   - Gambar AI (Batu, Kertas, atau Gunting) ditampilkan di sebelah gestur pemain.

---

## Masalah yang Sering Terjadi
1. **Kamera Tidak Terdeteksi**:
   - Pastikan kamera Anda aktif dan tidak digunakan oleh aplikasi lain.
   - Jika kamera tetap tidak terdeteksi, coba restart program atau komputer Anda.

2. **File Gambar Tidak Ditemukan**:
   - Pastikan folder **Resources/** berisi file gambar seperti **BG.png**, **1.png**, **2.png**, dan **3.png**.
   - Periksa kembali jalur direktori file gambar.

3. **Deteksi Tangan Tidak Akurat**:
   - Pastikan tangan Anda terlihat jelas di depan kamera.
   - Gunakan pencahayaan yang baik untuk hasil deteksi yang optimal.

---

## Kontrol Keyboard
| Tombol | Fungsi                |
|--------|-----------------------|
| **S**  | Memulai permainan     |
| **Q**  | Keluar dari permainan |

---

## Penutup
Proyek ini adalah implementasi sederhana dari permainan Batu Gunting Kertas menggunakan OpenCV dan CVZone. Anda dapat mengembangkan proyek ini lebih lanjut, seperti menambahkan animasi, menyimpan skor pemain, atau meningkatkan antarmuka.

Jika Anda memiliki pertanyaan atau masalah, jangan ragu untuk menghubungi saya! 😊

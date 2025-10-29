
# Program

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Deskripsi

Repository ini berisi implementasi program Python canggih untuk tugas mata kuliah **Desain dan Analisis Algoritma**. Program ini mencakup operasi dasar matriks (penjumlahan dan perkalian), algoritma pengurutan **Selection Sort** dan **Bubble Sort**, serta pencarian **Sequential Search**. Versi ini ditingkatkan dengan fitur interaktif seperti menu CLI, pengukuran performa (waktu eksekusi), visualisasi proses sorting menggunakan Matplotlib, error handling, dan penyimpanan hasil ke file CSV.

Program dirancang untuk mudah digunakan, edukatif, dan skalabel. Cocok untuk mahasiswa yang ingin memahami desain algoritma dasar sambil melihat analisis kompleksitas Big O secara otomatis.

### Fitur Utama
- **Interaktif**: Menu berbasis console untuk memilih operasi (matriks, sorting, search).
- **Input Dinamis**: Masukkan data matriks/array langsung dari user.
- **Performa**: Ukur waktu eksekusi setiap algoritma.
- **Visualisasi**: Plot grafik perubahan array selama proses sorting (opsional).
- **Output**: Simpan hasil ke CSV untuk analisis lebih lanjut.
- **Robust**: Error handling untuk input tidak valid (misal, ukuran matriks tidak cocok).
- **Kompleksitas**: Tampilkan Big O secara otomatis (O(n²) untuk sorting, O(n) untuk search, O(m*n) untuk matriks).

## Requirements

- Python 3.8 atau lebih tinggi.
- Library eksternal (install via pip):
  ```
  pip install numpy matplotlib
  ```

## Instalasi

1. Clone repository ini ke lokal machine Anda:
   ```
   git clone https://github.com/Izhar2005/program.git
   cd program
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   *(Buat file `requirements.txt` dengan isi: `numpy` dan `matplotlib` jika belum ada.)*

## Cara Menjalankan

1. Jalankan file utama:
   ```
   python program.py
   ```

2. Pilih menu dari console:
   - **1**: Operasi Matriks (tambah/kali dua matriks).
   - **2**: Selection Sort dengan visualisasi.
   - **3**: Bubble Sort dengan visualisasi.
   - **4**: Sequential Search.
   - **5**: Keluar.

Contoh output untuk Selection Sort:
```
Array asli: [64, 34, 25, 12, 22, 11, 90]
Array terurut: [11, 12, 22, 25, 34, 64, 90]
Waktu eksekusi: 0.0001 detik
Kompleksitas Selection Sort: O(n²) waktu, O(1) space
```

- Visualisasi akan muncul sebagai plot bar chart jika dipilih (y/n).
- Hasil disimpan otomatis ke file seperti `hasil_selection.csv`.

## Struktur File
- `program.py`: File utama program (mengandung semua fungsi: `tambah_matriks_np`, `kali_matriks_np`, `selection_sort`, `bubble_sort`, `sequential_search`, dll.).
- `requirements.txt`: Daftar dependencies (opsional, buat sendiri jika perlu).
- `README.md`: Dokumen ini.
- Folder `output/` (otomatis dibuat): Berisi file CSV hasil eksekusi.

## Analisis Algoritma
| Algoritma          | Kompleksitas Waktu | Kompleksitas Space | Keterangan |
|--------------------|--------------------|--------------------|------------|
| **Matriks Tambah/Kali** | O(m*n)            | O(m*n)            | Skalabel dengan NumPy. |
| **Selection Sort** | O(n²)             | O(1)              | Pilih min secara berurutan. |
| **Bubble Sort**    | O(n²)             | O(1)              | Swap adjacent berulang. |
| **Sequential Search** | O(n)            | O(1)              | Pencarian linier. |

## Kontribusi
Silakan fork repository ini dan buat pull request untuk perbaikan atau fitur baru (misal, tambah QuickSort atau GUI Tkinter). Pastikan kode clean dan tested.

1. Fork repo.
2. Buat branch baru: `git checkout -b feature-baru`.
3. Commit changes: `git commit -m "Deskripsi perubahan"`.
4. Push: `git push origin feature-baru`.
5. Buat Pull Request.

## Lisensi
Distribusi di bawah [MIT License](LICENSE). Lihat file `LICENSE` untuk detail.

## Author
- **Izhar**  
  GitHub: [Izhar2005](https://github.com/Izhar2005)  
  Email: [izhardulgom@gmail.com](mailto:izhardulgom@gmail.com)  
  Dibuat untuk tugas kuliah Desain dan Analisis Algoritma, 2025.

Terima kasih! Jika ada issue, buka ticket di repo. 🚀

# Aplikasi Metode Numerik

Aplikasi interaktif berbasis Jupyter Notebook untuk menyelesaikan persamaan non-linear menggunakan berbagai metode numerik.

## Fitur Utama

- **Metode Regula-Falsi**: Menentukan akar persamaan dengan metode posisi palsu berdasarkan dua titik batas awal.
- **Metode Newton-Raphson**: Menentukan akar persamaan menggunakan pendekatan turunan fungsi dengan konvergensi yang cepat.
- **Metode Iterasi Sederhana**: Menentukan akar persamaan melalui bentuk formulasi iterasi titik tetap $x = g(x)$.
- **Menu Interaktif**: Memudahkan eksekusi dan pengujian seluruh metode secara langsung dalam notebook.

## Prasyarat

- Python 3.8 atau versi yang lebih baru.

## Panduan Instalasi & Persiapan

1. **Clone repositori ini:**
   ```bash
   git clone https://github.com/Ghofurm/project-metode-numerik.git
   cd project-metode-numerik
   ```

2. **Buat dan aktifkan Virtual Environment (opsional namun disarankan):**
   - **Linux / macOS:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
   - **Windows:**
     ```cmd
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install Dependensi:**
   ```bash
   pip install sympy notebook
   ```
   *(Opsional: `pip install tabulate` jika ingin tampilan tabel hasil iterasi yang lebih rapi).*

## Cara Menjalankan Aplikasi

1. Jalankan Jupyter Notebook di terminal:
   ```bash
   jupyter notebook main.ipynb
   ```
2. Jalankan sel kode pada notebook `main.ipynb` untuk membuka menu interaktif.
3. Pilih metode yang ingin digunakan dan masukkan fungsi sesuai petunjuk layar.

## Contoh Input Pengujian

### 1. Regula-Falsi
- **Fungsi `f(x)`**: `x**2 - 4`
- **Batas bawah (`a`)**: `0`
- **Batas atas (`b`)**: `3`

### 2. Newton-Raphson
- **Fungsi `f(x)`**: `x**2 - 4`
- **Turunan `f'(x)`**: `2*x`
- **Tebakan awal (`x0`)**: `3`

### 3. Iterasi Sederhana
- **Fungsi `g(x)`** (bentuk $x = g(x)$): `(x + 4/x) / 2`
- **Tebakan awal (`x0`)**: `1`

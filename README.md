# Uji Akurasi Prediksi TSI

Repositori ini berisi skrip untuk menghitung akurasi hasil prediksi Trophic State Index (TSI) menggunakan metrik MAE, RMSE, dan R-squared.

## Cara Menjalankan

1. Install dependensi:
   pip install -r requirements.txt

2. Pastikan file CSV berisi dua kolom:

- `observed`: nilai TSI pengamatan
- `predicted`: nilai TSI prediksi

3. Jalankan skrip:
   python uji_akurasi_tsi.py

## Dependensi

- pandas
- numpy
- scikit-learn
- matplotlib

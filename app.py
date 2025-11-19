import streamlit as st

# Judul Aplikasi
st.title("📐 Kalkulator Luas Persegi Panjang")
st.markdown("Masukkan nilai panjang dan lebar untuk menghitung luasnya.")

# 1. Definisikan Fungsi (Tidak Berubah)
def hitung_luas(panjang, lebar):
    """Menghitung Luas = Panjang * Lebar"""
    luas = panjang * lebar
    return luas

# 2. Input Menggunakan Widget Streamlit
# Widget untuk input Panjang
panjang = st.number_input(
    "Masukkan nilai Panjang:",
    min_value=0.0,      # Nilai minimum 0
    value=10.0,         # Nilai default
    step=0.1,           # Langkah desimal
    format="%.2f"       # Format tampilan desimal
)

# Widget untuk input Lebar
lebar = st.number_input(
    "Masukkan nilai Lebar:",
    min_value=0.0,
    value=5.0,
    step=0.1,
    format="%.2f"
)

# 3. Panggil Fungsi dan Tampilkan Hasil
# Kita menggunakan tombol agar perhitungan hanya dilakukan saat tombol ditekan
if st.button("Hitung Luas"):
    
    # Validasi input
    if panjang <= 0 or lebar <= 0:
        st.error("Panjang dan Lebar harus lebih besar dari 0.")
    else:
        # Panggil fungsi
        hasil_luas = hitung_luas(panjang, lebar)
    
        # Tampilkan Output
        st.success(f"**Luas Persegi Panjang** dengan Panjang **{panjang}** dan Lebar **{lebar}** adalah:")
        # Menampilkan hasil dengan ukuran font yang lebih besar
        st.metric(label="Hasil Luas", value=f"{hasil_luas:.2f} satuan persegi")
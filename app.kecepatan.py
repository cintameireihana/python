import streamlit as st

# Judul Aplikasi
st.title("🚀 Kalkulator Kecepatan Rata-Rata")
st.markdown("Hitung kecepatan rata-rata perjalanan Anda (dalam km/jam).")

# 1. Definisikan Fungsi (Tidak Berubah)
def hitung_kecepatan(jarak_km, waktu_jam):
    """Menghitung kecepatan rata-rata (km/jam)."""
    # Menghindari pembagian dengan nol
    if waktu_jam == 0:
        return 0 
    
    kecepatan = jarak_km / waktu_jam
    return kecepatan

# 2. Input Menggunakan Widget Streamlit
# Widget untuk input Jarak (km)
jarak = st.number_input(
    "Masukkan Jarak yang ditempuh (km):",
    min_value=0.0,      # Nilai minimum 0
    value=100.0,        # Nilai default
    step=1.0,           # Langkah input
    format="%.2f"       # Format tampilan desimal
)

# Widget untuk input Waktu (jam)
waktu = st.number_input(
    "Masukkan Waktu tempuh (jam):",
    min_value=0.0,
    value=2.0,
    step=0.1,
    format="%.2f"
)

# 3. Panggil Fungsi dan Tampilkan Hasil
# Tombol untuk memicu perhitungan
if st.button("Hitung Kecepatan"):
    
    # Validasi input
    if waktu <= 0:
        # Menampilkan pesan error jika waktu 0 atau negatif
        st.error("Waktu tempuh harus lebih besar dari 0 jam untuk menghitung kecepatan rata-rata.")
    elif jarak < 0:
        st.error("Jarak tidak boleh bernilai negatif.")
    else:
        # Panggil fungsi
        hasil_kecepatan = hitung_kecepatan(jarak, waktu)
    
        # Tampilkan Output
        st.success(f"**Kecepatan rata-rata Anda** adalah:")
        # Menggunakan st.metric untuk tampilan hasil yang menarik
        st.metric(
            label="Kecepatan Rata-Rata", 
            value=f"{hasil_kecepatan:.2f} km/jam"
        )
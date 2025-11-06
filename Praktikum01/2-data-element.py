import streamlit as st
import pandas as pd     # untuk mengelola data dalam bentuk tabel
import numpy as np      # untuk membuat data numerik acak
import altair as alt    # untuk membuat chart interaktif

st.title("Praktikum 1 Visualisasi Data")
st.subheader("Bagian 1 : Text Element")
st.markdown("""
Kelompok 12 :
1. ROZA KURNIAWAN NUR WAKID - 0110222124
2. PRAMANA RAHMANSAH PUTRA - 0110122051
3. IMAD HASAN AQIL - 0110221166
""")

# DataFrame : struktur data berbentuk tabel (baris dan kolom) yang disediakan oleh library pandas
st.subheader("DataFrame")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

# menampilkan DataFrame
st.dataframe(df)

# highlight nilai minimum
st.subheader("Highlight Minimum Value di DataFrame")

# highlight nilai terkecil disetiap kolom dataframe
#axis=0 bekerja perkolom
st.dataframe(df.style.highlight_min(axis=0))

# tabel statis
st.subheader("Tabel Statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)
#menampilkan tabel statis
st.table(df)

#metrics : komponen tampilan angka penting
st.subheader("Metrics")
# metrics tunggal
st.metric(label="Temperature", value="31 C", delta="1.2 C") # kenaikan 1.2 C

# metrics sesuai delta_color
# delta_color digunakan untuk memberi warna sesuai arah perubahan :
# - "normal" (default): naik hijau, turun merah
# - "inverse" : kebalikannya naik merah
# - "off" : tidak menampilkan warna perubahan

#definisikan variabel metrics
col1, col2, col3 = st.columns(3)

#menampilkan indikator data
col1.metric("curah hujan", "100cm", "10cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar", delta_color="inverse") # naik tapi buruk
col3.metric(label="Pelanggan", value=100, delta=10, delta_color="off") #netral (tidak baik, tidak burul)

#menampilkan metrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #Kosong naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") # penurunan
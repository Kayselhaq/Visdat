import streamlit as st

st.title("Columns")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057  
""")

col1, col2 = st.columns(2)

col1.write("Ini adalah kolom pertama")
col1.image("../assets/bulat1.jpeg")
col2.write("Ini adalah kolom kedua")
col2.image("../assets/bulat2.png")
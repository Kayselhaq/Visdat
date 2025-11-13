import streamlit as st 
from PIL import Image
img = Image.open("../assets/bulat1.jpeg")

st.title("Padding")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057   
""")

col1, padding, col2 = st.columns((10,2,10))
with col1:
    col1.image(img)
with col2:
    col2.image(img)
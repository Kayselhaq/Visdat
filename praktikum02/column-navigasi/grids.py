import streamlit as st
from PIL import Image
img= Image.open("../assets/bulat2.png")


st.title("Grid")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057   
""")

for a in range(4):
    cols = st.columns((1, 1, 1, 1))
    cols[0].image(img)
    cols[1].image(img)
    cols[2].image(img)
    cols[3].image(img)
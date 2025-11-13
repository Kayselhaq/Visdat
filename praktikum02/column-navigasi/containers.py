import streamlit as st 
import numpy as np

st.title("Containers")
st.write("Kelompok: 19")
st.markdown("""
            1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057  
""")

with st.container():
    st.write("Element Inside Container")
    st.line_chart(np.random.randn(40, 4))
    st.write("Element Outside Container")
import streamlit as st
import time

st.title("Empety Containers")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057  
""")

with st.empty():
    for seconds in range(5):
        st.write(f" {seconds} seconds have passed")
        time.sleep(1)
        st.write("Timer up!")
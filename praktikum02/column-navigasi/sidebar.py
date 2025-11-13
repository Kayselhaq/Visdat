import streamlit as st

st.title("Sidebar")
st.write("Kelompok: 19")
st.markdown("""
            1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057  
""")

st.sidebar.title("Sidebar")
st.sidebar.radio("Are you a New User", ["Yes", "No"])
st.sidebar.slider("Select a Number", 0,10)
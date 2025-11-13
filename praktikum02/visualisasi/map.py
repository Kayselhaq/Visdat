import streamlit as st
import pandas as pd
import numpy as np

st.title("Map")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057   
             """)

df= pd.DataFrame(
    np.random.randn(50, 2) / [10,10] + [15.4589, 75.0078],
    columns=["latitude", "longitude"]
)

st.map(df)
import streamlit as st
import graphviz as graphviz

st.title("Graphviz Chart")
st.write("Kelompok: 19")
st.markdown("""
             1. Kays Elhaq Rabbani - 0110222218
            2. Ahmad Fauzi Nugroho – 0110222293 
            3. Muhammad Al Faruq – 0110122057   """)

st.graphviz_chart("""
    digraph{
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"}
                  """)
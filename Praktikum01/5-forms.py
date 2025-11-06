import streamlit as st
import datetime
import pandas as pd

#buat text box
st.title("Text Box")
name = st.text_input("Enter your Name")
st.write("Your Name is ", name)

#buat text area
input_text = st.text_area("Enter your Review")
st.write("""You entered: \n""", input_text)

#buat number input
st.number_input("Enter your Number")
num = st.number_input("Enter your Number", 0, 10, 5, 2)
st.write("Min. Value is 0, Max. Value is 10")
st.write("Default Value is 5, Step Size value is 2")
st.write("Total value after adding Number entered with step value is:", num)

#buat time
st.title("Time")
st.time_input("Select Your Time")

#buat date
st.title("Date")
st.date_input("Select Date")

st.title("Date")
st.date_input(
    "Select Your Date",
    value=datetime.date(1989, 12, 25),
    min_value=datetime.date(1987, 1, 1),
    max_value=datetime.date(2005, 12, 1)
)


#buat warna
st.title("Select Color")
color_code = st.color_picker("Select your Color")
st.header(color_code)

st.title("CSV Data")

# File uploader for CSV files
data_file = st.file_uploader("Upload CSV", type=["csv"])
details = st.button("Check Details")

if details:
    if data_file is not None:
        file_details = {
            "file_name": data_file.name,
            "file_type": data_file.type,
            "file_size": data_file.size
        }
        st.write(file_details)

        # Read CSV file
        df = pd.read_csv(data_file)
        st.dataframe(df)
    else:
        st.write("No CSV file is uploaded")


my_form = st.form(key='form')
a = my_form.text_input(label='Enter any text')

# Defining submit button
submit_button = my_form.form_submit_button(label='Submit')

st.write(a)
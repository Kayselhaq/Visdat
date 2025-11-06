import streamlit as st  
import time

#buat button
st.title('Creating a Button')
button = st.button('Click Here')
if button:
    st.write('You have clicked the button')
else:
    st.write('You have not clicked the button')

#buat raido buttpn
st.title('Creating Radio Button')
gender = st.radio(
"Select your Gender",
('Male', 'Female', 'Others'))
if gender == 'Male' :
    st.write('You have selected Male')
elif gender == 'Female' :
    st.write('You have selected Female')
else:
    st.write('You have selected Others')

#buat checkbox
st.title('Creating Checkboxes')
st.write('Select your Hobies:')

check_1 = st.checkbox('Books')
check_2 = st.checkbox('Movies')
check_3 = st.checkbox('Sports')

#buat dropdown
st.title('Creating Dropdown')
hobby = st.selectbox('Choose your hobby: ',
('Books', 'Movies', 'Sports'))


#buat multi select
st.title('Multi-Select')
hobbies = st.multiselect(
    'What are your Hobbies',
    ['Reading', 'Cooking', 'Watching Movies/TV Series', 'Playing', 'Drawing', 'Hiking'],
    ['Reading', 'Playing']
)

#buat download button
st.title("Download Button")
down_btn = st.download_button(
    label="Download Image",
    data=open("assets/black.jpg", "rb"),
    file_name="tiger.jpg",
    mime="image/jpg"
)

#buat progres bar
st.title('Progress Bar')
download = st.progress(0)
for percentage in range(100):
    time.sleep(0.1)
    download.progress(percentage + 1)
st.write('Download Complete')

#buat spinner
st.title('Spinner')
with st.spinner('Loading...'):
    time.sleep(5)
st.write('Hello Data Scientists')
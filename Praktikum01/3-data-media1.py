import streamlit as st
import base64
from PIL import Image

st.write("Displaying an Image")
st.image("E:\mazda-rx-7-thumb.jpg")
st.write("Image Countesy: Unplash")

st.write("Displaying Multiple Image")
car_images = [
'E:\m4.jpg',
'E:\supra.jpg',
'E:\mitsubisi.jpg',
]
st.image(car_images, width=150)
st.write("Image Countesy: Unplash")

def add_local_background_image_(image):
    with open(image, "rb") as image:
        encoded_string = base64.b64encode(image.read())
    st.write("Image Countesy: Unplash")
    st.markdown(
    f"""
    <style>
    .stApp {{
    background-image: url(data:file/{"jpg"};base64,{encoded_string.decode()});
    bacground-size: cover
    }}
    """,
    unsafe_allow_html=True
    )
st.write("Background Image")
add_local_background_image_('E:\html.jpg')

original_image = Image.open("E:\mazda-rx-7-thumb.jpg")
st.title("Original Image")
st.image(original_image)
resized_image = original_image.resize((600, 400))
st.title("Resized Image")
st.image(resized_image)
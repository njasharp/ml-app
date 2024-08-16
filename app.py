import streamlit as st
from PIL import Image
import os

# Path to the folder where images are stored
image_folder = "./store"

# List of image filenames
image_files = [
    'eg-and.PNG',
    'eg-ios.PNG',
    'iq-and.PNG',
    'ir-ios.PNG',
    'mo-and.PNG',
    'mo-ios.PNG',
    'sa-and.PNG',
    'sa-ios.PNG',
    'uae-and.PNG',
    'UAE-ios.PNG'
]

# Load and display the custom header image
header_image_path = "./store/image.png"
header_image = Image.open(header_image_path)

st.image(header_image, use_column_width=True)

# Streamlit app title with custom styling
st.title("IOS & ANDROID")



# Display images
for image_file in image_files:
    # Construct full image path
    image_path = os.path.join(image_folder, image_file)
    
    # Open image
    image = Image.open(image_path)
    
    # Display image with caption
    st.image(image, caption=image_file, use_column_width=True)

st.info("Build by DW 8-15-23")
# Display the build signature

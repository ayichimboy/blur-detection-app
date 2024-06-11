import cv2
import numpy as np
import streamlit as st
from PIL import Image

def is_image_blurry(image_path, threshold=100.0):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise ValueError("Image not found or unable to load.")
        laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
        return laplacian_var < threshold
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def main():
    st.title("Blurry Image Detector")
    st.write("Upload an image to check if it is blurry.")

    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        try:
            # Read the image file to a temporary location
            image = Image.open(uploaded_file)
            image_path = "temp_image.jpg"
            image.save(image_path)

            # Set a default threshold value
            threshold = st.slider("Blurriness threshold", 0.0, 300.0, 100.0)

            # Check if the image is blurry
            if is_image_blurry(image_path, threshold):
                st.write("The image is blurry.")
            else:
                st.write("The image is not blurry.")

            # Display the uploaded image
            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        except Exception as e:
            st.error(f"An error occurred while processing the image: {e}")

if __name__ == "__main__":
    main()

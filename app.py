import os
import streamlit as st
import replicate
from PIL import Image
import tempfile
import base64
import io

st.title("GIF Generator")
st.subheader("Convert any image into a GIF")

os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]

# Create image uploader in Streamlit
uploaded_file = st.file_uploader("Choose an image:", type=["png", "jpg", "jpeg"])

# Save the image file and get its path
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.')

    # Convert the image to a data URI
    buffer = io.BytesIO()
    image.save(buffer, format='PNG')
    img_str = base64.b64encode(buffer.getvalue()).decode()
    image_uri = f"data:image/png;base64,{img_str}"

# Run API when button is clicked
if st.button("Generate the GIF"):
    output = replicate.run(
        "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
        input={
            "cond_aug": 0.02,
            "decoding_t": 7,
            "input_image": image_uri,
            "video_length": "14_frames_with_svd",
            "sizing_strategy": "maintain_aspect_ratio",
            "motion_bucket_id": 127,
            "frames_per_second": 6
        }
    )
    st.video(output)

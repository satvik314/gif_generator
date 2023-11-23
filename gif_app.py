import os
import streamlit as st
import replicate
from PIL import Image
import tempfile
import base64
import io

st.title("🤖🔧 GIF Generator ")
st.subheader("💥 Create Mind-Blowing GIFs in Minutes! 💥")
st.write("♥️ Powered by DALLE-3 and Stable Video Diffusion ")

os.environ["REPLICATE_API_TOKEN"] = st.secrets["REPLICATE_API_TOKEN"]
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Create image uploader in Streamlit
prompt = st.text_input(label= "your idea here", placeholder= "🤔 your GIF idea here.", label_visibility="hidden")

from openai import OpenAI
client = OpenAI()

# Run API when button is clicked
if st.button("blow my mind"):

    if prompt:
        with st.spinner('cooking your GIF...'):
            response = client.images.generate(
            model="dall-e-3",
            prompt= "generate an image of " + prompt,
            size="1024x1024",
            quality="standard",
            n=1,
            )
            
            image_url = response.data[0].url

            output = replicate.run(
                "stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438",
                input={
                    "cond_aug": 0.02,
                    "decoding_t": 7,
                    "input_image": image_url,
                    "video_length": "14_frames_with_svd",
                    "sizing_strategy": "maintain_aspect_ratio",
                    "motion_bucket_id": 127,
                    "frames_per_second": 6
                }
            )
        st.success("Your GIF is ready!")
        st.video(output)


# clip = VideoFileClip("https://replicate.delivery/pbxt/dHfZMwKXBfrCEkR1JIefLoSnkiLJCZdvM9KYsix7GxyIsPtHB/000209.mp4")
# gif_path = "output.gif"
# clip.write_gif(gif_path)

# st.success('GIF generated successfully!')
# st.image(gif_path)
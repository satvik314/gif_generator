# GIF Generator

This repository contains a Streamlit application that allows you to convert images into GIFs using the Replicate API. The app accepts image files (PNG, JPG, JPEG), converts them into a base64 encoded string, and then sends it to the Replicate API for GIF generation.

## Getting Started

Follow these instructions to get the Streamlit app running on your local machine:

### 1. Clone the repository
```bash
git clone https://github.com/satvik314/gif_generator
```

### 2. Navigate to the cloned repository
```bash
cd gif_generator
```

### 3. Add Replicate Key to ```secrets.toml```
```bash
REPLICATE_API_TOKEN = "<your_token>"
```

### 4. Install required Python libraries
```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit App
```bash
streamlit run app.py
```

In the app, upload an image using the file uploader. Once the image is uploaded, it's displayed on the app. Click the "Convert to GIF" button to generate a GIF from the uploaded image. The GIF is displayed in the app.

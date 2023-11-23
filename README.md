# GIF Generator

This repository contains a Streamlit application that allows you to convert images into GIFs using the Replicate API. The app accepts image files (PNG, JPG, JPEG), converts them into a base64 encoded string, and then sends it to the Replicate API for GIF generation.

## Getting Started

Follow these instructions to get the Streamlit app running on your local machine:

### Clone the repository
```bash
git clone https://github.com/satvik314/gif_generator
```

### Navigate to the cloned repository
```bash
cd gif_generator
```

### Add Replicate Key to ```secrets.toml```
```bash
REPLICATE_API_TOKEN = "<your_token>"
```

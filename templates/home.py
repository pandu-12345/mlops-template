import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Upload & Predict", layout="centered")

st.title("🧠 Smart Predictor")

# Instructions
st.markdown("""
Upload a **text** or **image** file, or **type your own sentence**, then click **Predict** to get a result from the API.
""")

# API endpoint (change to your real one)
API_URL = "http://40.81.226.190:8000/predict"

# --- Input Section ---

# 1. File Upload
uploaded_file = st.file_uploader("📤 Upload a file (Text or Image)", type=["txt", "png", "jpg", "jpeg"])

# 2. Typed Text
typed_text = st.text_area("✍️ Or write something here", placeholder="Type your sentence here...")

# --- Preview Section ---
file_type = None
file_content = None
image_obj = None

if uploaded_file:
    file_type = uploaded_file.type

    if file_type.startswith("text"):
        file_content = uploaded_file.read().decode("utf-8")
        st.subheader("📄 Uploaded Text File Preview")
        st.code(file_content, language="text")

    elif file_type.startswith("image"):
        image_obj = Image.open(uploaded_file)
        st.subheader("🖼️ Uploaded Image")
        st.image(image_obj, caption="Uploaded Image", use_container_width=True)
        file_content = uploaded_file  

# --- Predict Button ---
if st.button("🔍 Predict"):
    if uploaded_file:
        try:
            st.info("Sending uploaded file to the API...")
            if file_type.startswith("text"):
                response = requests.post(API_URL, json={"text": file_content})
            elif file_type.startswith("image"):
                files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
                response = requests.post(API_URL, files=files)
            else:
                st.error("Unsupported file type.")
                response = None
        except Exception as e:
            st.error(f"API request failed: {e}")
            response = None

    elif typed_text.strip() != "":
        try:
            st.info("Sending typed text to the API...")
            response = requests.post(API_URL, json={"text": typed_text})
        except Exception as e:
            st.error(f"API request failed: {e}")
            response = None
    else:
        st.warning("Please upload a file or type something to predict.")
        response = None

    if response and response.status_code == 200:
        result = response.json()

        st.success("✅ Prediction Result:")
        st.markdown(f"**Prediction:** `{result.get('prediction', 'N/A')}`")


        if "confidence" in result:
            st.markdown(f"**Confidence:** `{result['confidence'] * 100:.2f}%`")

        with st.expander("📦 Full API Response"):
            st.json(result)

    elif response:
        st.error(f"❌ API Error {response.status_code}: {response.text}")

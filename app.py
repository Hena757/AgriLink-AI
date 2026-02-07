import streamlit as st
from PIL import Image

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="AgriLink AI",
    page_icon="🌱",
    layout="wide"
)

# ---------- LOAD IMAGES ----------
farm_img = Image.open("assets/field.jpg")
crop_img = Image.open("assets/crop.png")
weather_img = Image.open("assets/cloud.png")

# ---------- HERO SECTION ----------
st.markdown(
    """
    <style>
    .hero {
        background-color: #f0fdf4;
        padding: 40px;
        border-radius: 15px;
    }
    .card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="hero">', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])

with col1:
    st.title("🌱 AgriLink AI")
    st.subheader("Smart Digital Companion for Farmers")
    st.write(
        """
        AgriLink AI empowers farmers with **AI-driven crop guidance,
        disease detection, and weather-based recommendations** —
        anytime, anywhere.
        """
    )
    st.success("🚜 Prototype for Online Hackathon")

with col2:
    st.image(field_img, use_column_width=True)

st.markdown('</div>', unsafe_allow_html=True)

st.write("")

# ---------- FEATURES ----------
st.header("🔍 Key Features")

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(crop_img, use_column_width=True)
    st.subheader("🌿 Disease Detection")
    st.write("Upload crop images and get instant disease insights.")
    st.markdown('</div>', unsafe_allow_html=True)

with f2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image(cloude_img, use_column_width=True)
    st.subheader("🌦 Weather Alerts")
    st.write("Weather-aware farming recommendations to reduce risk.")
    st.markdown('</div>', unsafe_allow_html=True)

with f3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🤖 AI Assistance")
    st.write("Ask farming questions via text or voice (prototype).")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- PROTOTYPE DEMO ----------
st.header("🧪 Live Prototype Demo")

option = st.selectbox(
    "Choose a service",
    ["Ask AI", "Crop Disease Detection", "Weather Alerts"]
)

if option == "Ask AI":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    question = st.text_input("Ask your farming question")
    if st.button("Get AI Advice"):
        st.info("🤖 AI Suggestion: Ensure proper irrigation and monitor pests regularly.")
    st.markdown('</div>', unsafe_allow_html=True)

elif option == "Crop Disease Detection":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    file = st.file_uploader("Upload crop image", type=["jpg", "png"])
    if st.button("Analyze Crop"):
        st.success("🌿 Disease Detected: Leaf Blight")
        st.write("✅ Recommendation: Apply fungicide and reduce moisture.")
    st.markdown('</div>', unsafe_allow_html=True)

elif option == "Weather Alerts":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.warning("🌧 Heavy rainfall expected in next 24 hours")
    st.write("⚠ Recommendation: Avoid pesticide spraying today.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- FOOTER ----------
st.write("---")
st.markdown(
    "👩‍🌾 **Team:** Hena Pandit | Annapurna KB | Arpitha Poojari  \n"
    "🌍 *Empowering Farmers Through AI Innovation*"
)


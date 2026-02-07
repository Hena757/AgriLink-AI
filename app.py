import streamlit as st

st.set_page_config(page_title="AgriLink AI", layout="centered")

st.title("🌱 AgriLink AI")
st.subheader("Smart Digital Companion for Farmers")

menu = st.selectbox(
    "Choose a service",
    ["Ask AI", "Crop Disease Detection", "Weather Alerts"]
)

if menu == "Ask AI":
    st.text_input("Ask your farming question")
    st.button("Get AI Advice")
    st.info("🤖 AI response will appear here (prototype)")

elif menu == "Crop Disease Detection":
    st.file_uploader("Upload crop image", type=["jpg", "png"])
    st.button("Analyze Crop")
    st.success("🌿 Disease Detected: Leaf Blight (Sample Result)")
    st.write("Recommended Action: Use fungicide and avoid excess watering.")

elif menu == "Weather Alerts":
    st.warning("🌧 Heavy rainfall expected tomorrow")
    st.write("⚠ Avoid pesticide spraying")

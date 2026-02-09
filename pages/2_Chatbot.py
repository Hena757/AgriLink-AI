import streamlit as st

st.title("🤖 AgriLink AI Assistant")

tab1, tab2, tab3 = st.tabs(["💬 Chat", "📷 Upload Image", "🎤 Voice"])

with tab1:
    q = st.text_input("Ask your question")
    if st.button("Send"):
        st.info("AI: Maintain proper irrigation and monitor crop health.")

with tab2:
    img = st.file_uploader("Upload crop image", type=["jpg","png"])
    if st.button("Analyze"):
        st.success("Disease Detected: Leaf Blight")
        st.write("Recommended cure: Apply fungicide")

with tab3:
    st.info("🎤 Voice chat coming soon (prototype)")


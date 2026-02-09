import streamlit as st

st.title("🔍 Search Crops & Diseases")

query = st.text_input("Search plant / disease / cure")

if query:
    st.write(f"Results for **{query}**")
    st.info("• Disease: Leaf Blight")
    st.success("• Cure: Use copper-based fungicide")


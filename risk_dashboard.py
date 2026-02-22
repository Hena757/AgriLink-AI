import streamlit as st
import random

def show_risk_dashboard():

    st.header("📊 Farm Risk Analysis Dashboard")

    st.write("This dashboard evaluates overall farm risk based on disease probability, weather conditions, and crop sensitivity.")

    # Simulated risk values (can later connect to real outputs)
    disease_risk = random.randint(20, 80)
    weather_risk = random.randint(10, 70)
    crop_sensitivity = random.randint(15, 60)

    total_risk = int((disease_risk + weather_risk + crop_sensitivity) / 3)

    st.subheader(f"Overall Farm Risk Score: {total_risk}/100")

    if total_risk < 40:
        st.success("Low Risk – Farm conditions are stable.")
    elif total_risk < 70:
        st.warning("Medium Risk – Monitor crops closely.")
    else:
        st.error("High Risk – Immediate preventive action recommended.")

    st.markdown("### Risk Breakdown")

    st.bar_chart({
        "Disease Risk": disease_risk,
        "Weather Risk": weather_risk,
        "Crop Sensitivity": crop_sensitivity
    })
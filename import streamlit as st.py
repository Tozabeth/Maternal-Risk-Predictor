import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load("maternal_model.pkl")

st.set_page_config(page_title="MamaCare AI", layout="centered")

st.title("🤰 MamaCare AI – Maternal Risk Predictor")
st.subheader("An AI-powered early screening tool for safer pregnancies")

st.markdown("---")

# 2-column layout
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 15, 45, 25)
    headache = st.selectbox("Severe Headache", ["No", "Yes"])
    blurred_vision = st.selectbox("Blurred Vision", ["No", "Yes"])
    swelling = st.selectbox("Swelling of hands or face", ["No", "Yes"])
    bleeding = st.selectbox("Vaginal Bleeding", ["No", "Yes"])
    pain = st.selectbox("Severe Abdominal Pain", ["No", "Yes"])

with col2:
    dizziness = st.selectbox("Dizziness", ["No", "Yes"])
    movement = st.selectbox("Low Fetal Movement", ["No", "Yes"])
    stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
    visit = st.selectbox("Antenatal Visits (Last Month)", [1, 2, 3])
    nutrition = st.selectbox("Nutrition Quality", ["Poor", "Average", "Good"])

# Mapping for binary values
binary_map = {"No": 0, "Yes": 1}
stress_map = {"Low": 0, "Moderate": 1, "High": 2}
nutrition_map = {"Poor": 0, "Average": 1, "Good": 2}

# Apply mapping
input_data = pd.DataFrame([{
    "Age": age,
    "severe headache": binary_map[headache],
    "blurred vision": binary_map[blurred_vision],
    "swelling hands/face": binary_map[swelling],
    "vaginal bleeding": binary_map[bleeding],
    "severe abdominal pain": binary_map[pain],
    "dizziness or fainting": binary_map[dizziness],
    "low fetal movement": binary_map[movement],
    "high stress": stress_map[stress],
    "visited antenal last month": visit,
    "nutrition quality": nutrition_map[nutrition],
}])

# Predict
if st.button("Predict Risk Level"):
    prediction = model.predict(input_data)[0]
    risk_labels = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}
    risk_texts = {
        0: "✅ You are at **low risk**. Keep up with regular antenatal visits, maintain good nutrition, and monitor any changes.",
        1: "⚠️ You are at **moderate risk**. Please consult your healthcare provider for further evaluation and monitoring.",
        2: "🚨 You are at **high risk**. Immediate medical attention is advised. Please visit your nearest health facility as soon as possible."
    }

    st.success(f"🩺 Predicted Maternal Risk Level: **{risk_labels[prediction]}**")
    st.markdown(risk_texts[prediction])


import streamlit as st
import joblib
import pandas as pd
model = joblib.load(maternal_model.pkl) # type: ignore
st.set_page_config(page_title="MamaCare AI", layout="centered")

st.title("🤰 MamaCare AI – Maternal Risk Predictor")
st.subheader("An AI-powered early screening tool for safer pregnancies")

# User Inputs
age = st.slider("Age", 15, 45, 25)
headache = st.selectbox("Severe Headache", ["No", "Yes"])
blurred_vision = st.selectbox("Blurred Vision", ["No", "Yes"])
swelling = st.selectbox("Swelling of hands or face", ["No", "Yes"])
bleeding = st.selectbox("Vaginal bleeding", ["No", "Yes"])
pain = st.selectbox("Severe abdominal pain", ["No", "Yes"])
dizziness = st.selectbox("Dizziness", ["No", "Yes"])
movement = st.selectbox("Low fetal movement", ["No", "Yes"])
stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
visit = st.selectbox("How many times did you visit antenatal last month?", [1,2,3])
nutrition = st.selectbox("Nutrition quality", ["Poor", "Average","Good"])




# Mapping inputs
input_data = pd.DataFrame({
    "Age": [age],
    "Fever": [{"None": 0, "Mild": 1, "High": 2}[fever]],
    "Nausea": [ {"None": 0, "Mild": 1, "Severe": 2}[nausea]],
    "Headache": [ {"None": 0, "Mild": 1, "Severe": 2}[headache]],
    "Blurred_Vision": [1 if blurred_vision == "Yes" else 0],
    "Dizziness": [1 if dizziness == "Yes" else 0],
    "Swelling": [1 if swelling == "Yes" else 0],
    "Bleeding": [1 if bleeding == "Yes" else 0],
})

if st.button("Check Risk"):
    prediction = model.predict(input_data)[0]
    label_map = {0: "Low Risk", 1: "Moderate Risk", 2: "High Risk"}
    st.success(f"Predicted Risk Level: **{label_map[prediction]}**")

                    
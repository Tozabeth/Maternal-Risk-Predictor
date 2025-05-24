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
    headache = st.selectbox("Severe Headache", ["No", "Yes"])
    blurred_vision = st.selectbox("Blurred Vision", ["No", "Yes"])
    swelling = st.selectbox("Swelling of hands or face", ["No", "Yes"])
    bleeding = st.selectbox("Vaginal Bleeding", ["No", "Yes"])
    pain = st.selectbox("Severe Abdominal Pain", ["No", "Yes"])

with col2:
    dizziness = st.selectbox("Dizziness", ["No", "Yes"])
    movement = st.selectbox("Low Fetal Movement", ["No", "Yes"])
    stress = st.selectbox("Stress Level", ["Low", "Moderate", "High"])
    visit = st.selectbox("Antenatal Visits (Last Month)", ["0", "1", "2 or more"])
    visit_map = {"0": 0, "1": 1, "2 or more": 2}
    nutrition = st.selectbox("Nutrition Quality", ["Poor", "Average", "Good"])

# Mapping for binary values
binary_map = {"No": 0, "Yes": 1}
stress_map = {"Low": 0, "Moderate": 1, "High": 2}
nutrition_map = {"Poor": 0, "Average": 1, "Good": 2}

# Apply mapping
input_data = pd.DataFrame([{
    "severe headache": binary_map[headache],
    "blurred vision": binary_map[blurred_vision],
    "swelling hands/face": binary_map[swelling],
    "vaginal bleeding": binary_map[bleeding],
    "severe abdominal pain": binary_map[pain],
    "dizziness or fainting": binary_map[dizziness],
    "low fetal movement": binary_map[movement],
    "high stress": stress_map[stress],
    "visited antenatal last month": visit_map[visit],
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

    # ---------------------------
# 💬 MamaCare Chatbot Assistant (Styled)
# ---------------------------

st.markdown("---")
st.markdown("## 🤖 MamaCare Chat Assistant")
st.caption("Get quick answers to common pregnancy-related concerns. This assistant is trained with trusted health tips and FAQ knowledge.")

st.markdown("### ❓ Ask a Question")
user_input = st.text_input("Example: *What is high risk?*", placeholder="Type your question here...")

# Dictionary of smart FAQ responses
responses = {
    "what is low risk": "🟢 **Low Risk** means no concerning symptoms. Keep up with antenatal care and healthy living.",
    "what is medium risk": "🟡 **Medium Risk** indicates warning signs. Monitor symptoms and consult a health worker if they persist.",
    "what is high risk": "🔴 **High Risk** suggests serious danger signs. Please seek **urgent medical attention**.",
    "how often should i visit the clinic": "📅 Antenatal visits should occur **at least once a month**. Later in pregnancy, go more frequently.",
    "what are danger signs": "⚠️ Danger signs include: *severe headache, swelling, blurred vision, bleeding, fainting, or low fetal movement.*",
    "what should i eat": "🥗 Eat **balanced meals**: veggies, fruits, proteins, and iron-rich food. Stay hydrated and avoid processed junk.",
    "can i exercise": "🏃‍♀️ Yes, light activities like **walking, stretching, or yoga** are okay unless your doctor says otherwise.",
    "is stress harmful": "🧘‍♀️ Yes, **chronic stress** affects both mother and baby. Relax, rest, and get support when needed."
}

# Respond to input
if user_input:
    question = user_input.lower().strip()
    reply = responses.get(question, "🤔 I’m not sure how to answer that. Please contact your health provider.")
    st.success(reply)

# Quick-access question buttons
st.markdown("### 💡 Quick Tips")
b1, b2, b3 = st.columns(3)

with b1:
    if st.button("What is low risk?"):
        st.info(responses["what is low risk"])
    if st.button("What should I eat?"):
        st.info(responses["what should i eat"])

with b2:
    if st.button("What is high risk?"):
        st.info(responses["what is high risk"])
    if st.button("Can I exercise?"):
        st.info(responses["can i exercise"])

with b3:
    if st.button("Danger signs?"):
        st.info(responses["what are danger signs"])
    if st.button("Clinic visits?"):
        st.info(responses["how often should i visit the clinic"])

# Add disclaimer at the bottom
st.markdown("---")
st.caption("🩺 *This is not medical advice. For serious symptoms, always consult a qualified health professional.*")

st.markdown("---")
st.markdown("© 2025 Created by Elizabeth")



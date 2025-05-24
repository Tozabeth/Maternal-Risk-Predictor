# 🤰 Maternal Risk Predictor

A machine learning-powered web application that predicts the level of maternal health risk — **Low**, **Moderate**, or **High** — based on vital health indicators. Built with **Streamlit**, this tool aims to assist healthcare professionals and expectant mothers in early detection of potential complications, especially in resource-limited settings.

---

## 🚀 Live Demo

👉 [Click to Launch the App](https://maternal-risk-predictor.streamlit.app/)  
---

## 📌 Project Overview

In Nigeria, maternal mortality remains alarmingly high. According to the World Health Organization, the country accounted for approximately 28.5% of global maternal deaths in 2020, with a maternal mortality ratio of 1,047 per 100,000 live births . Many of these deaths are preventable and occur due to lack of timely medical intervention, particularly in rural and low-income areas where access to healthcare is limited.
This application leverages machine learning to provide an accessible tool for early risk assessment, enabling prompt medical attention and potentially saving lives.



### 🔍 Problem Statement

Maternal mortality remains a serious concern globally.Every day, over 700 women globally die from preventable causes related to pregnancy and childbirth . In Nigeria, the situation is particularly dire, with a significant number of maternal deaths Early risk prediction can support health workers in providing better interventions.What if a simple AI-powered web app could screen for high-risk pregnancies using just a few clicks—accessible even in remote areas with limited internet connectivity? This project seeks to bridge the gap in maternal healthcare by providing a tool that assists in early detection of potential risks, empowering healthcare workers and expectant mothers alike.

## 🛠️ Features
- User-Friendly Interface: Built with Streamlit for ease of use.

- Risk Prediction: Classifies maternal risk levels into Low, Moderate, or High.

- Symptom-Based Assessment: Utilizes user-inputted symptoms for evaluation.

- Model Performance Metrics: Displays accuracy, F1 score, and recall score.

- Accessible Design: Optimized for use in low-resource settings.

---

## 📊 Dataset Features
The model was trained on a dataset comprising the following features:

- Severe Headache
- Blurred Vision
- Swelling Hands/Face
- Vaginal Bleeding
- Severe Abdominal Pain
- Dizziness or Fainting
- Low Fetal Movement
- High Stress
- Visited Antenatal Last Month
- Nutrition Quality
Risk Level: Target variable indicating the severity of maternal risk.

## 🧪 Model Training & Evaluation

Five models were trained and evaluated:

- ✅ **Logistic Regression**
- ✅ **Random Forest**
- ✅ **Support Vector Classifier (SVC)**
- ✅ **Decision Tree**
- ✅ **Gradient Boosting**

The **Support Vector Classifier** classifier achieved the highest performance and was selected for deployment.

After thorough evaluation using accuracy, F1 score, and recall score, the Random Forest Classifier demonstrated the highest performance and was selected for deployment.

## 📊 How It Works

1. The user enters vital health indicators.
2. The pre-trained machine learning model processes the inputs.
3. The app displays the predicted maternal risk level and the corresponding probability.

---

## 🧠 Machine Learning Model

- **Model Used**: Support Vector Classifier (SVC)
- **Training Environment**: Google Colab
- **Evaluation Metric**: Accuracy Score,precision score,f1 score, recall score, Confusion Matrix
- **Serialized with**: `joblib`
- **Model File**: `maternal_model.pkl`

---

## 📁 Files in this Repository

| File/Folder             | Description |
|-------------------------|-------------|
| `app.py`                | Main Streamlit application script |
| `maternal_model.pkl`    | Trained machine learning model |
| `requirements.txt`      | List of dependencies |
| `maternal.ipynb`        | Google Colab notebook for model training & EDA |
| `README.md`             | Project documentation |

---

## 📦 Installation & Usage

### 🔧 Prerequisites

- Python 3.7+
- pip

### 📥 Clone the Repository

```bash
git clone https://github.com/Tozabeth/Maternal-Risk-Predictor.git
cd Maternal-Risk-Predictor


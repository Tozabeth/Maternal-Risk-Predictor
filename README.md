# 🤰 Maternal Risk Predictor

A machine learning-powered web application that predicts the level of maternal health risk — **Low**, **Moderate**, or **High** — based on vital health indicators. Built with **Streamlit**, this tool aims to assist healthcare professionals in early diagnosis and decision-making for maternal care.

---

## 🚀 Live Demo

👉 [Click to Launch the App](https://your-deployment-link.com)  
*(Replace with your Streamlit Cloud or deployment link)*

---

## 📌 Project Overview

This application was built for a data science competition aimed at using technology to solve real-world problems. The app uses a pre-trained machine learning model to assess maternal risk levels based on user-provided health metrics.

### 🔍 Problem Statement

Maternal mortality remains a serious concern globally. Early risk prediction can support health workers in providing better interventions. This app leverages data science to help predict risk using patient metrics such as:

- Age
- Systolic Blood Pressure (SBP)
- Diastolic Blood Pressure (DBP)
- Blood Sugar Levels (BSL)
- Body Temperature
- Heart Rate

---

## 🛠️ Features

- ✅ User-friendly interface with **Streamlit**
- ✅ Real-time prediction of **maternal risk level**
- ✅ Displays model **confidence score** for each prediction
- ✅ Includes a **simple chatbot** for answering FAQs
- ✅ Automatically categorized risk into **Low**, **Moderate**, and **High**
- ✅ Built-in **educational tooltips** to assist users

---

## 📊 How It Works

1. The user enters vital health indicators.
2. The pre-trained machine learning model processes the inputs.
3. The app displays the predicted maternal risk level and the corresponding probability.

---

## 🧠 Machine Learning Model

- **Model Used**: Logistic Regression (or specify the actual one used)
- **Training Environment**: Google Colab
- **Evaluation Metric**: Accuracy Score, Confusion Matrix
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


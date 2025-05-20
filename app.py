import streamlit as st
import joblib
import pandas as pd

# Load the model
model = joblib.load("mentalhealth_model")

# Streamlit UI
st.title("Student Depression Prediction App")

# Collect input features
gender_input = st.selectbox("Gender", ["Male", "Female"])
gender_numeric = 1 if gender_input == "Male" else 0
age = st.slider("Age", min_value=18, max_value=24)
year_input = st.selectbox("What year are you in?", ["Year 1", "Year 2", "Year 3", "Year 4"])
yr_mapping = {'Year 1': 1, 'Year 2': 2, 'Year 3': 3, 'Year 4': 4}
year_numeric = yr_mapping[year_input]

grade_input = st.selectbox(
    "What is your current CGPA range?",
    ['0 - 1.99', '2.00 - 2.49', '2.50 - 2.99', '3.00 - 3.49', '3.50 - 4.00']
)
grade_mapping = {
    '0 - 1.99': 1,
    '2.00 - 2.49': 2,
    '2.50 - 2.99': 3,
    '3.00 - 3.49': 4,
    '3.50 - 4.00': 5
}
grade_numeric = grade_mapping[grade_input]
marital_status = st.radio("Are you married?", ['Yes', 'No'])
marital_status_numeric = 1 if marital_status == 'Yes' else 0

anxiety = st.radio("Do you experience anxiety?", ['Yes', 'No'])
anxiety_numeric = 1 if anxiety == 'Yes' else 0
panic_attack = st.radio("Do you experience panic attacks?", ['Yes', 'No'])
panic_attack_numeric = 1 if panic_attack == 'Yes' else 0
treatment = st.radio("Have you ever sought help or seen a specialist for mental health concerns?", ['Yes', 'No'])
treatment_numeric = 1 if treatment == 'Yes' else 0

course_corrections = {
    'Engineering': 'Engineering',
    'engin': 'Engineering',
    'Engine': 'Engineering',
    'KOE': 'Engineering',
    'koe': 'Engineering',
    'Koe': 'Engineering',
    'Islamic education': 'Islamic Education',
    'Islamic Education': 'Islamic Education',
    'Pendidikan islam': 'Islamic Education',
    'Pendidikan Islam': 'Islamic Education',
    'Pendidikan Islam ': 'Islamic Education',
    'BIT': 'Information Technology',
    'bit': 'Information Technology',
    'Bit': 'Information Technology',
    'IT': 'Information Technology',
    'Benl': 'English and Literature',
    'BENL': 'English and Literature',
    'Kirkhs': 'Human Sciences',
    'KIRKHS': 'Human Sciences',
    'Irkhs': 'Human Sciences',
    'Laws': 'Law',
    'Law': 'Law',
    'Psychology': 'Psychology',
    'psychology': 'Psychology',
    'KENMS': 'Economics and Management',
    'Accounting ': 'Accounting',
    'ENM': 'Economics and Management',
    'Marine science': 'Marine Science',
    'Banking Studies': 'Banking Studies',
    'Business Administration': 'Business Administration',
    'ALA': 'Arabic Language and Literature',
    'Biomedical science': 'Biomedical Science',
    'CTS': 'Communication and Technology Studies',
    'Econs': 'Economics',
    'MHSC': 'Medical and Health Sciences',
    'Malcom': 'Mass Communication',
    'Kop': 'Pharmacy',
    'Human Sciences ': 'Human Sciences',
    'Communication ': 'Communication',
    'Diploma Nursing': 'Nursing',
    'Nursing ': 'Nursing',
    'BCS': 'Computer Science',
    'Radiography': 'Radiography',
    'Fiqh fatwa ': 'Law',
    'Fiqh': 'Law',
    'DIPLOMA TESL': 'English and Literature',
    'Usuluddin ': 'Religious studies',
    'TAASL': 'Theology'
}

course_columns =[
    'Course_Arabic Language and Literature', 'Course_Banking Studies',
    'Course_Biomedical Science', 'Course_Biotechnology', 'Course_Business Administration',
    'Course_Communication', 'Course_Communication and Technology Studies',
    'Course_Computer Science', 'Course_Economics', 'Course_Economics and Management',
    'Course_Engineering', 'Course_English and Literature', 'Course_Human Resources',
    'Course_Human Sciences', 'Course_Islamic Education', 'Course_Information Technology',
    'Course_Law', 'Course_Marine Science', 'Course_Mass Communication',
    'Course_Mathemathics', 'Course_Medical and Health Sciences', 'Course_Nursing',
    'Course_Pharmacy', 'Course_Psychology', 'Course_Radiography',
    'Course_Religious studies', 'Course_Theology'
]# Initialize all course inputs to 0
#course_input = {col: 0 for col in course_columns}

# Standardize input
raw_course = st.selectbox("Select your course", sorted(course_corrections.keys()))
cleaned_course = course_corrections.get(raw_course, raw_course)
course_input = {col: 0 for col in course_columns}

# Set 1 in the right dummy column
dummy_col = f'Course_{cleaned_course}'
if dummy_col in course_input:
    course_input[dummy_col] = 1


#course_options = sorted([
    #'Accounting', 'Arabic Language and Literature', 'Banking Studies',
    #'Biomedical Science', 'Biotechnology', 'Business Administration',
    #'Communication', 'Communication and Technology Studies', 'Computer Science',
    #'Economics', 'Economics and Management', 'Engineering',
    #'English and Literature', 'Human Resources', 'Human Sciences',
    #'Islamic Education', 'Information Technology', 'Law',
    #'Marine Science', 'Mass Communication', 'Mathemathics',
    #'Medical and Health Sciences', 'Nursing', 'Pharmacy',
    #'Psychology', 'Radiography', 'Religious studies', 'Theology'
#])
#selected_course = st.selectbox("Select Your Course", course_options)
#course_input = dict.fromkeys(course_columns, 0)

##course_key = f"Course_{selected_course}"
#if course_key in course_input:
    #course_input[course_key] = 1

features = {
    'Gender': gender_numeric,
    'Age': age,
    'Year': year_numeric,
    'CGPA': grade_numeric,
    'Marital Status': marital_status_numeric,
    'Anxiety': anxiety_numeric,
    'Panic Attack': panic_attack_numeric,
    'Treatment': treatment_numeric,
    **course_input
}
input_df = pd.DataFrame([features])
input_df = input_df.reindex(columns=features, fill_value=0)
if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("The student is likely experiencing depression.")
    else:
        st.success("The student is not likely experiencing depression.")
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("best_rf_model.joblib")

# Title
st.title("Student Dropout Prediction")

# Input fields
curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem Approved", min_value=0, max_value=100, value=0)
curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem Grade", min_value=0.0, max_value=20.0, value=0.0)
curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem Approved", min_value=0, max_value=100, value=0)
curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem Grade", min_value=0.0, max_value=20.0, value=0.0)
tuition_fees_up_to_date = st.selectbox("Tuition Fees Up-to-date(1 = Yes, 0 = No)", [0, 1])

# Predict button
if st.button("Predict"):
    features = np.array([[curricular_units_1st_sem_approved, 
                          curricular_units_1st_sem_grade,
                          curricular_units_2nd_sem_approved, 
                          curricular_units_2nd_sem_grade, 
                          tuition_fees_up_to_date]])
    
    prediction = model.predict(features)
    prediction_proba = model.predict_proba(features)

    if prediction[0] == 1:
        st.success(f"The student is likely to graduate with a probability of {prediction_proba[0][1]*100:.2f}%")
    else:
        st.error(f"The student is likely to drop out with a probability of {prediction_proba[0][0]*100:.2f}%")

# Import necessary libraries
import pandas as pd
import streamlit as st
import pickle
<<<<<<< HEAD
from Logger import BaseLogger
=======
from Utils.Logger import BaseLogger
>>>>>>> origin/master

# Initialize logger
logger = BaseLogger(name='StreamlitLogger')

# Load the pre-trained model
@st.cache(allow_output_mutation=True)
def load_model():
<<<<<<< HEAD
    with open('model.pkl', 'rb') as model_file:
=======
    with open('D:\machineLearning\heart_attack_analysis\src\Experiments\model.pkl', 'rb') as model_file:
>>>>>>> origin/master
        model = pickle.load(model_file)
    return model

# Main function
def main():
    # Create UI
    st.title("Heart Attack Classification")

    # Load the pre-trained model
    model = load_model()

    # Display form for user input
    st.write("Fill in the following details to predict heart attack probability:")
    age = st.slider("Age", min_value=1, max_value=100, value=50)
    sex = st.radio("Sex", ["Male", "Female"])
    cp_type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
    resting_bp = st.slider("Resting Blood Pressure (mm Hg)", min_value=90, max_value=200, value=120)
    cholesterol = st.slider("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
    fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", ["False", "True"])
    resting_ecg = st.selectbox("Resting Electrocardiographic Results", ["Normal", "ST-T wave abnormality", "Probable left ventricular hypertrophy"])
    max_hr = st.slider("Maximum Heart Rate Achieved (bpm)", min_value=50, max_value=250, value=150)
    exercise_angina = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
    oldpeak = st.slider("ST Depression induced by exercise relative to rest", min_value=0.0, max_value=10.0, value=2.0)
    st_slope = st.selectbox("Slope of the peak exercise ST segment", ["Upsloping", "Flat", "Downsloping"])

    # Convert categorical input to numerical
    sex = 1 if sex == "Male" else 0
    cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-anginal Pain": 2, "Asymptomatic": 3}
    cp_type = cp_map[cp_type]
    fasting_bs = 1 if fasting_bs == "True" else 0
    resting_ecg_map = {"Normal": 0, "ST-T wave abnormality": 1, "Probable left ventricular hypertrophy": 2}
    resting_ecg = resting_ecg_map[resting_ecg]
    exercise_angina = 1 if exercise_angina == "Yes" else 0
    st_slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
    st_slope = st_slope_map[st_slope]

    # Make prediction
    prediction = model.predict([[age, sex, cp_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])
    prediction_prob = model.predict_proba([[age, sex, cp_type, resting_bp, cholesterol, fasting_bs, resting_ecg, max_hr, exercise_angina, oldpeak, st_slope]])[0][1]

    # Display prediction
    if prediction[0] == 0:
        st.write("Prediction: No Heart Attack")
    else:
        st.write("Prediction: Heart Attack")
    st.write("Probability of Heart Attack:", prediction_prob)

# Execute the main function
if __name__ == '__main__':
    main()

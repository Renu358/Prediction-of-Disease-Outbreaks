import os
import pickle # pre trained model loading
import streamlit as st    # web app
# from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
diabetes_model = pickle.load(open('saved_models/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('saved_models/heart_model.sav', 'rb'))
parkinsons_model = pickle.load(open('saved_models/parkinsons_model.sav', 'rb'))

# Create sidebar for navigation
st.sidebar.title("Prediction of Disease Outbreaks")

disease_selected = st.sidebar.selectbox("Select a Disease Prediction Model:",
                                       ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
                                       index=0)

# Diabetes Prediction
st.title(disease_selected + " using ML")
if disease_selected == 'Diabetes Prediction':
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        Bloodpressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the person')
    
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])
        diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
    st.success(diab_diagnosis)


# Heart Disease Prediction
if disease_selected == 'Heart Disease Prediction':
    col1, col2, col3 = st.columns(3)
    with col1:
        Age = st.text_input('Age')
    with col2:
        Sex = st.text_input('Sex (1 for Male, 0 for Female)')
    with col3:
        ChestPainType = st.text_input('Chest Pain Type (0-3)')
    with col1:
        RestingBloodPressure = st.text_input('Resting Blood Pressure')
    with col2:
        Cholesterol = st.text_input('Serum Cholesterol')
    with col3:
        FastingBloodSugar = st.text_input('Fasting Blood Sugar')
    with col1:
        RestingECG = st.text_input('Resting Electrocardiographic Results (0-2)')
    with col2:
        MaxHeartRateAchieved = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        ExerciseInducedAngina = st.text_input('Exercise Induced Angina (1 for Yes, 0 for No)')
    with col1:
        STDepression = st.text_input('ST Depression')
    with col2:
        SlopeOfPeakExerciseST = st.text_input('Slope of Peak Exercise ST')
    with col3:
        MajorVesselsColoredByFluoroscopy = st.text_input('Major Vessels Colored by Fluoroscopy (0-3)')
    with col1:
        Thalassemia = st.text_input('Thalassemia (0-3)')
    
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [Age, Sex, ChestPainType, RestingBloodPressure, Cholesterol, FastingBloodSugar, RestingECG,
                      MaxHeartRateAchieved, ExerciseInducedAngina, STDepression, SlopeOfPeakExerciseST,
                      MajorVesselsColoredByFluoroscopy, Thalassemia]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
    st.success(heart_diagnosis)

# Parkinson's Prediction
if disease_selected == 'Parkinsons Prediction':
    col1, col2, col3 = st.columns(3)

    with col1:
        FoM = st.text_input('MDVP:Fo(Hz)', key='FoM')
        Jitter_percent = st.text_input('MDVP:Jitter(%)', key='Jitter_percent')
        Jitter_DDP = st.text_input('Jitter:DDP', key='Jitter_DDP')
        HNR = st.text_input('HNR', key='HNR')
        spread1 = st.text_input('spread1', key='spread1')
        D2 = st.text_input('D2', key='D2')

    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)', key='MDVP_Fhi')
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)', key='Jitter_Abs')
        Shimmer = st.text_input('MDVP:Shimmer', key='Shimmer')
        RPDE = st.text_input('RPDE', key='RPDE')
        spread2 = st.text_input('spread2', key='spread2')
        PPE = st.text_input('PPE', key='PPE')

    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)', key='MDVP_Flo')
        RAP = st.text_input('MDVP:RAP', key='MDVP_RAP')
        Shimmer_APQ = st.text_input('MDVP:APQ', key='Shimmer_APQ')
        DFA = st.text_input('DFA', key='DFA')
        NHR = st.text_input('NHR', key='NHR')

    # Remaining features
    with col1:
        PPQ = st.text_input('MDVP:PPQ', key='MDVP_PPQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA', key='Shimmer_DDA')
    with col3:
        MDVP_Fp = st.text_input('MDVP:PPQ', key='MDVP_Fp')
    with col1:
        MDVP_Fy = st.text_input('MDVP:Fy', key='MDVP_Fy')
    with col2:
        MDVP_Fs = st.text_input('MDVP:Fs', key='MDVP_Fs')

    parkinsons_diagnosis = ''

    if st.button('Parkinsons Test Result'):
        user_input = [
            FoM, MDVP_Fhi, MDVP_Flo, Jitter_percent, Jitter_Abs,
            RAP, PPQ, Jitter_DDP, Shimmer, Shimmer_APQ, Shimmer_DDA,
            NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE,
            MDVP_Fp, MDVP_Fy, MDVP_Fs
        ]

        if len(user_input) != 22:
            st.error(f"Error: Expected 22 features but got {len(user_input)}. Please enter all fields.")
        else:
            user_input = [float(x) for x in user_input]  # Convert inputs to float
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = 'The person has Parkinsons disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinsons disease'

    st.success(parkinsons_diagnosis)

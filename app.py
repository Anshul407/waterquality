# -*- coding: utf-8 -*-

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

finalmodel = pickle.load(open('finalmodel.sav', 'rb'))


# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Water Quality prediction BY- Anshul Kunwar',
                          
                          ['Water Quality'],
                          icons=['activity'],
                          default_index=0)
    
    
if (selected == 'Water Quality'):
    
    # page title
    st.title('Water Quality Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Index')
        
    with col2:
        Glucose = st.text_input('pH')
    
    with col3:
        BloodPressure = st.text_input('Iron')
    
    with col1:
        SkinThickness = st.text_input('Nitrate')
    
    with col2:
        Insulin = st.text_input('Chloride')
    
    with col3:
        BMI = st.text_input('Lead')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Zinc')
    
    with col2:
        Age = st.text_input('Turbudity')
    with col3:
        a = st.text_input('Fluoride')
    
    with col1:
        b = st.text_input('Copper')
    
    with col2:
        c = st.text_input('Odor')
    
    with col3:
        d = st.text_input('Sulfate')
    
    with col1:
        e = st.text_input('Conductivity')
    
    with col2:
        f= st.text_input('Chlorine')
    with col3:
        g= st.text_input('Maganese')
    
    with col1:
        h = st.text_input('Total Dissolved solids')
    
    with col2:
        i= st.text_input('Water Temperature')
        
    with col3:
        j= st.text_input('Air Temperature')
    
    
    
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Water Quality Result'):
        diab_prediction = finalmodel.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,a,b,c,d,e,f,g,h,i,j]])
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'Quality is Good'
        else:
          diab_diagnosis = 'Quality is Bad'

        
    st.success(diab_diagnosis)
















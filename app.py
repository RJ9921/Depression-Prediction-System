import streamlit as st
import joblib
import pandas as pd 
from streamlit_option_menu import option_menu
from PIL import Image
import seaborn as sns
import base64
import pickle
import numpy as np


with st.sidebar:
    selected=option_menu(
    menu_title="Main Menu",
        options=['Home','Depression Prediction'],
        icons=['house','book'],
        styles={
            "container":{"background-color":"#c6be9a"},
            "nav-link":{
                "font-size":"21px",
                "--hover-color":"#ad8b32",
                "color":"317202A"
            },
            "nav-link-selected":{
                "background-color":"#937460"
            },
            "icon":{
                "font-size":"20px"
            },
        },
    )

if selected == 'Home':
    st.markdown("""
    <style>
    .big-font1{
    font-size:50px !important;
    color:#8c5b7b;
    text-align:center;
    font-weight:bold;
    
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font1"> WELCOME TO THE DEPRESSION PREDICTION SYSTEM </p>',unsafe_allow_html=True)
    st.markdown(' <p class="paragraph"> Depression is known as a mood disorder. It is described as feelings of sadness, loss, or anger that interfere with a person’s everyday activities. People experience depression in different ways. It may interfere with your daily work, resulting in lost time and lower productivity. It can also influence relationships and some chronic health conditions. </p>',
    unsafe_allow_html=True)
    file_=open("depression2.png","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="depression2">',
        unsafe_allow_html=True, )

    

if selected=='Depression Prediction':
    file_=open("depression-sad.gif","rb")
    contents=file_.read()
    data_url=base64.b64encode(contents).decode("utf-8")
    file_.close()

    st.markdown(
        f'<img src="data:image/gif;base64,{data_url}" width="700" image-align="center"  alt="Depression gif">',
        unsafe_allow_html=True, )

    st.markdown("""
    <style>
        .big-font1{
            font-size:50px !important;
            color:red;
            text-align:center;
            font-weight:bold;
    </style>
    """,unsafe_allow_html=True)
    loaded_model=pickle.load(open('depression.sav','rb'))

    def depression_prediction(input_data):
    

        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if (prediction[0] == 0):
            return 'Person is Not Depressed'
        else:
            return 'Person is Depressed'
    def main(): 


        st.markdown("<h1 style='text-align: center; color: #4b3c5d ;'>DEPRESSION PREDICTION SYSTEM</h1>", unsafe_allow_html=True)
        #getting the input data from the user
        co1,col2,=st.columns(2)


        with co1:
            Cant_Work=st.selectbox('Are you Not Able to Work  No:0 Yes:1',(0,1),index=0)
            Memory_Problems=st.selectbox('Do you Have Memory Problems No:0 Yes:1',(0,1),index=0)

        with col2:
            Limited_Work=st.selectbox('Do you Have Limited Work No:0 Yes:1',(0,1),index=0)
            Trouble_Sleeping_History=st.selectbox('Are You Facing Trouble To Sleep No:0 Yes:1',(0,1),index=0)
            Health_Problem_Back_Or_Neck=st.selectbox('Do you Have Health Problem of Back Or Neck No:0 Yes:1',(0,1),index=0)
            

        #code for the prediction 
        diagnosis=''
        #creating a button for prediction 
        if st.button('Depression Prediction Result'):
            diagnosis = depression_prediction([Cant_Work,Memory_Problems,Limited_Work,Trouble_Sleeping_History,Health_Problem_Back_Or_Neck])
            st.success(diagnosis)
        

    
    if __name__ =='__main__':
        main()











import streamlit as st
import pickle
import numpy as np

# Load model
loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

st.title("Sonar Rock vs Mine Prediction")

st.write("Enter 60 sonar values separated by commas")

input_data = st.text_area("Input")

if st.button("Predict"):
    try:
        values = [float(x) for x in input_data.split(',')]

        if len(values) != 60:
            st.error("Please enter exactly 60 values.")
        else:
            input_array = np.asarray(values).reshape(1, -1)

            prediction = loaded_model.predict(input_array)

            if prediction[0] == 'R':
                st.success("The object is a Rock")
            else:
                st.success("The object is a Mine")

    except:
        st.error("Please enter valid numeric values.")
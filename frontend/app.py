import streamlit as st
import pandas as pd
import requests

st.title("Tip Prediction App")
st.write("Please enter the details to get tip amount")

# input data
total_bill = st.number_input("Total Bill", min_value=0)
sex = st.selectbox ("sex", options = ["Male", "Female"])
smoker = st.selectbox ("smoker", options = ["Yes", "No"])
day = st.selectbox ("day", options = ["Thur", "Fri", "Sat", "Sun"])
time = st.selectbox ("time", options = ["Lunch", "Dinner"])
size = st.number_input("size", min_value=1, max_value=10)
# when the button is clicked
if st.button("Predict Tip"):
    # prepare the data to send to the backend
    input_data = {"total_bill": total_bill,
                  "sex": sex,
                  "smoker": smoker,
                   "day": day,
                   "time": time,
                   "size": size}
        
    response = requests.post("http://127.0.0.1:5000/predict", json=input_data)
    # response = requests.post("http://127.0.0.1:5000/predict", json=input_data)

    # if response.status_code == 200:
    #     prediction = response.json()["prediction"]
    #     st.success(f"Predicted Tip: ${prediction:.2f}")
    if response.status_code == 200:
        prediction = response.json().get("prediction")
        st.write ("The tip value is", prediction)
    else:
        st.error("Error in prediction. Please try again.")
        
        
# http://127.0.0.1:5000/predict
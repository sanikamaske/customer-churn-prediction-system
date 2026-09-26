import streamlit as st
import joblib
import pandas as pd

model = joblib.load("customer_churn_model.pkl")

st.title("Customer Churn Prediction")

gender = st.selectbox("Gender", [0, 1])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", [0, 1])
dependents = st.selectbox("Dependents", [0, 1], key="dependents")
tenure = st.number_input("Tenure Months", min_value=0) 
phone = st.selectbox("Phone Service", [0 , 1],key="phone")
multiple = st.selectbox("Multiple Lines", [0, 1])
internet = st.selectbox("Internet Service", [0, 1])
online_security = st.selectbox("Online Security", [0, 1])
online_backup = st.selectbox("Online Backup", [0, 1])
device_protection = st.selectbox("Device Protection", [0, 1])
tech_support = st.selectbox("Tech Support", [0, 1])
streaming_tv = st.selectbox("Streaming TV", [0, 1])
streaming_movies = st.selectbox("Streaming Movies", [0, 1])
contract = st.selectbox("Contract", [0, 1, 2])
paperless = st.selectbox("Paperless Billing", [0, 1])
payment = st.selectbox("Payment Method", [0, 1, 2, 3])
monthly = st.number_input("Monthly Charges")
total = st.number_input("Total Charges")

if st.button("Predict"):
   data = pd.DataFrame([[
    gender,
    senior,
    partner,
    dependents,
    tenure,
    phone,
    multiple,
    internet,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies,
    contract,
    paperless,
    payment,
    monthly,
    total
   ]] ,
    columns=[
    "Gender",
    "Senior Citizen",
    "Partner",
    "Dependents",
    "Tenure Months",
    "Phone Service",
    "Multiple Lines",
    "Internet Service",
    "Online Security",
    "Online Backup",
    "Device Protection",
    "Tech Support",
    "Streaming TV",
    "Streaming Movies",
    "Contract",
    "Paperless Billing",
    "Payment Method",
    "Monthly Charges",
    "Total Charges"
])
   

prediction = model.predict(data)        
if prediction[0] == 1:
    st.error("Customer is likely to Churn")
else:
    st.success("Customer is likely to Stay")
        

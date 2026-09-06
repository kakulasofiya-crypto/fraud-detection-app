import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Page title
st.title("Fraud Detection")
st.write("Enter the transaction details below.")

# Input features
amount_usd = st.number_input("Amount (USD)", min_value=0.0)

merchant_category = st.number_input("Merchant Category", min_value=0)
card_type = st.number_input("Card Type", min_value=0)
auth_method = st.number_input("Authentication Method", min_value=0)
channel = st.number_input("Channel", min_value=0)
device_type = st.number_input("Device Type", min_value=0)

is_foreign_transaction = st.number_input(
    "Is Foreign Transaction", min_value=0, max_value=1, step=1
)

hours_since_last_txn = st.number_input(
    "Hours Since Last Transaction", min_value=0.0
)

txn_count_last_24h = st.number_input(
    "Transaction Count Last 24 Hours", min_value=0, step=1
)

distance_from_home_km = st.number_input(
    "Distance From Home (km)", min_value=0.0
)

card_age_months = st.number_input(
    "Card Age (Months)", min_value=0, step=1
)

customer_age = st.number_input(
    "Customer Age", min_value=0, step=1
)

account_balance_usd = st.number_input(
    "Account Balance (USD)", min_value=0.0
)

is_new_merchant = st.number_input(
    "Is New Merchant", min_value=0, max_value=1, step=1
)

used_vpn = st.number_input(
    "Used VPN", min_value=0, max_value=1, step=1
)

ip_country_mismatch = st.number_input(
    "IP Country Mismatch", min_value=0, max_value=1, step=1
)

billing_shipping_mismatch = st.number_input(
    "Billing Shipping Mismatch", min_value=0, max_value=1, step=1
)

cvv_retry_count = st.number_input(
    "CVV Retry Count", min_value=0, step=1
)

velocity_score = st.number_input(
    "Velocity Score", min_value=0.0
)

time_of_day_hour = st.number_input(
    "Time of Day Hour", min_value=0, max_value=23, step=1
)

day_of_week = st.number_input(
    "Day of Week", min_value=0, max_value=6, step=1
)

is_ai_generated_scam_attempt = st.number_input(
    "Is AI Generated Scam Attempt", min_value=0, max_value=1, step=1
)

merchant_risk_score = st.number_input(
    "Merchant Risk Score", min_value=0.0
)

prior_disputes = st.number_input(
    "Prior Disputes", min_value=0, step=1
)

# Prediction button
if st.button("Predict"):

    input_data = pd.DataFrame([[
        amount_usd,
        merchant_category,
        card_type,
        auth_method,
        channel,
        device_type,
        is_foreign_transaction,
        hours_since_last_txn,
        txn_count_last_24h,
        distance_from_home_km,
        card_age_months,
        customer_age,
        account_balance_usd,
        is_new_merchant,
        used_vpn,
        ip_country_mismatch,
        billing_shipping_mismatch,
        cvv_retry_count,
        velocity_score,
        time_of_day_hour,
        day_of_week,
        is_ai_generated_scam_attempt,
        merchant_risk_score,
        prior_disputes
    ]], columns=[
        "amount_usd",
        "merchant_category",
        "card_type",
        "auth_method",
        "channel",
        "device_type",
        "is_foreign_transaction",
        "hours_since_last_txn",
        "txn_count_last_24h",
        "distance_from_home_km",
        "card_age_months",
        "customer_age",
        "account_balance_usd",
        "is_new_merchant",
        "used_vpn",
        "ip_country_mismatch",
        "billing_shipping_mismatch",
        "cvv_retry_count",
        "velocity_score",
        "time_of_day_hour",
        "day_of_week",
        "is_ai_generated_scam_attempt",
        "merchant_risk_score",
        "prior_disputes"
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠️ Fraudulent Transaction")
    else:
        st.success("✅ Legitimate Transaction")
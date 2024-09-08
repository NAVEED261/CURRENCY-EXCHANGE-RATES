import streamlit as st
import requests

# Function to get exchange rate
def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if data['result'] == 'success':
        return data['conversion_rates'].get(target_currency, None)
    else:
        st.error("Error fetching exchange rate.")
        return None

# Streamlit interface
st.title("Currency Exchange Rate App")

# API key
api_key = "c782b92bab38e39510a9e1a1"  # Your actual API key

# User input for currencies
base_currency = st.text_input("Enter base currency (e.g., USD):", "USD").upper()
target_currency = st.text_input("Enter target currency (e.g., PKR):", "PKR").upper()
amount = st.number_input("Enter the amount to convert:", min_value=1)

# Get exchange rate on button click
if st.button("Convert"):
    exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        st.success(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")
    else:
        st.error(f"Exchange rate not available for {base_currency} to {target_currency}")

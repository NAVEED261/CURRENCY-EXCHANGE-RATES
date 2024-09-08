import streamlit as st
import requests

# Function to get exchange rate
def get_exchange_rate(base_currency, target_currency, api_key):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    
    if data["result"] == "success":
        return data["conversion_rates"].get(target_currency, None)
    else:
        return None

# Streamlit App Interface
st.title("🌍 Currency Exchange Rate App")

# Add styling for input fields and buttons
st.markdown(
    """
    <style>
    .stTextInput, .stNumberInput {
        width: 50%;
        margin: 0 auto;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        margin-top: 20px;
        border-radius: 8px;
        border: none;
        font-size: 16px;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h2 {
        color: #2b83ba;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# API key
api_key = "c782b92bab38e39510a9e1a1"

# Dropdown for currency selection
base_currency = st.selectbox("Select base currency:", ["USD", "EUR", "PKR", "INR", "GBP", "CAD"])
target_currency = st.selectbox("Select target currency:", ["USD", "EUR", "PKR", "INR", "GBP", "CAD"])

# Amount input field
amount = st.number_input("Enter the amount to convert:", min_value=1, value=1000)

# Convert Button
if st.button("Convert"):
    exchange_rate = get_exchange_rate(base_currency, target_currency, api_key)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        st.success(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        st.error("Error fetching exchange rate. Please try again.")

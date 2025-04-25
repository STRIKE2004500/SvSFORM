import streamlit as st
import gspread
from google.oauth2 import service_account

# Disable certificate verification
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Main app structure
st.title("Google Sheets Connector")

# Google Sheets connection setup
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(credentials)

# Connection confirmation
st.success("Successfully connected to Google Sheets")

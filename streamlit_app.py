import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account

# Disable certificate verification
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Main app
st.title("Google Sheets Data Viewer")

# Connect to Google Sheets
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(credentials)

# Load and display data
sheet = gc.open_by_key("1mH33jpMV6bUq0FO2Cz1MtzZh026yopfP5yYZEr3Nunk").worksheet("SvS battle")
st.dataframe(pd.DataFrame(sheet.get_all_records()))

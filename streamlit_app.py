import streamlit as st
import pandas as pd
from gspread_pandas import Client, Spread

# Authenticate with Google Sheets (using service account)
@st.cache_resource
def get_gsheets_client():
    return Client()

# Read data from worksheet
def get_sheet_data():
    client = get_gsheets_client()
    spread = Spread("WOS battle")  # Replace with your Sheet ID
    return spread.sheet_to_df(sheet="SvS battle")

# Main app
df = get_sheet_data()
st.dataframe(df)

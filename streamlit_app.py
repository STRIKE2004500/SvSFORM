import streamlit as st
import pandas as pd
import gspread
from google.oauth2 import service_account

# Disable certificate verification (helps with some SSL issues)
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Create connection function with better error handling
@st.cache_resource(show_spinner="Connecting to Google Sheets...")
def get_gsheets_connection():
    try:
        if not st.secrets.get("gcp_service_account"):
            raise Exception("No Google Cloud credentials found in secrets!")

        credentials = service_account.Credentials.from_service_account_info(
            st.secrets["gcp_service_account"],
            scopes=["https://www.googleapis.com/auth/spreadsheets"]
        )
        return gspread.authorize(credentials)
    except Exception as e:
        st.error(f"Connection failed: {str(e)}")
        return None

def load_sheet_data():
    try:
        # Replace with your actual Sheet ID
        SHEET_ID = "1mH33jpMV6bUq0FO2Cz1MtzZh026yopfP5yYZEr3Nunk"  
        SHEET_NAME = "SvS battle"
        
        gc = get_gsheets_connection()
        if not gc:
            return pd.DataFrame()
            
        sheet = gc.open_by_key(SHEET_ID).worksheet(SHEET_NAME)
        records = sheet.get_all_records()
        return pd.DataFrame(records)
        
    except gspread.exceptions.APIError as e:
        st.error(f"Google API Error: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error: {str(e)}")
    return pd.DataFrame()

# Main app
st.title("Google Sheets Data Viewer")

if st.button("Refresh Data"):
    st.cache_resource.clear()
    
df = load_sheet_data()

if not df.empty:
    st.dataframe(df)
else:
    st.warning("No data loaded. Please check your connection settings.")

import streamlit as st
import gspread
from google.oauth2 import service_account

# Disable certificate verification
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Main app structure
st.title("SvS Battle Registration")

# Google Sheets connection setup
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=["https://www.googleapis.com/auth/spreadsheets"]
)
gc = gspread.authorize(credentials)

# Registration Form
with st.form("registration_form"):
    # Player Information
    player_name = st.text_input("Enter your in-game name")
    
    # Alliance Selection
    alliance = st.selectbox(
        "What is Your Alliance?",
        ["TCW", "MRA", "RFA", "SHR"],
        index=0
    )
    
    # FC Level
    fc_level = st.selectbox(
        "What is Your FC level?",
        ["F30", "FC1", "FC2", "FC3", "FC4", "FC5"],
        index=0
    )
    
    # Troop Levels
    infantry_level = st.selectbox(
        "What is your Infantry Troops level?",
        ["T10", "FC1", "FC2", "FC3", "FC4", "FC5"],
        index=0
    )
    
    lancer_level = st.selectbox(
        "What is your Lancer Troops level?",
        ["T10", "FC1", "FC2", "FC3", "FC4", "FC5"],
        index=0
    )
    
    marksman_level = st.selectbox(
        "What is your Marksman Troops level?",
        ["T10", "FC1", "FC2", "FC3", "FC4", "FC5"],
        index=0
    )
    
    # Submit Button
    submitted = st.form_submit_button("Submit Registration")

# Connection confirmation
st.success("Successfully connected to Google Sheets")

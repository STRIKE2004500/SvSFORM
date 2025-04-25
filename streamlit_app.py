import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Connect to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# Read from a worksheet
df = conn.read(worksheet="SvS battle")

# Display the dataframe
st.dataframe(df)

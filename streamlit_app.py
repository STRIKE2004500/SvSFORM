import streamlit as st
from streamlit.connections import ExperimentalBaseConnection
import pandas as pd

# Create a connection (using Streamlit's built-in GSheets connector)
conn = st.connection("gsheets", type="google_sheets")

# Read data from the worksheet
df = conn.read(worksheet="SvS battle")  # Ensure worksheet name matches exactly

# Display the dataframe
st.dataframe(df)

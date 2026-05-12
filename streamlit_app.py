import streamlit as st
import pandas as pd
import glob
import os

st.title(" Real-Time Crypto Dashboard")

# Path to output CSV files
files = glob.glob(r"dags/output/*.csv")

if files:

    latest_file = max(files, key=os.path.getctime)

    df = pd.read_csv(latest_file)

    st.subheader("Latest Crypto Data")

    st.dataframe(df)

    st.subheader("Price Chart")

    st.bar_chart(df.set_index("coin")["price_usd"])

else:

    st.warning("No CSV files found.")
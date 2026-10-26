import streamlit as st
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(page_title="Customer Analytics Dashboard", page_icon="📊", layout="wide")

# Connect to PostgreSQL (replace 'your_password' with your actual password)
@st.cache_resource
def get_engine():
    return create_engine('postgresql://postgres:your_password@localhost:5432/customer_analytics_db')

try:
    engine = get_engine()
    query = "SELECT * FROM customers;"
    df = pd.read_sql(query, engine)
except Exception as e:
    st.error(f"Database connection error: {e}. Make sure PostgreSQL is running and credentials are correct.")
    st.stop()

st.title("📊 Enterprise Customer Analytics Dashboard")
st.write("End-to-end data pipeline powered by Python, PostgreSQL, and Streamlit.")

# Sidebar Filters
st.sidebar.header("Filter Options")
if 'country' in df.columns:
    country_filter = st.sidebar.selectbox("Select Country", options=['All'] + list(df['country'].dropna().unique()))
    if country_filter != 'All':
        filtered_df = df[df['country'] == country_filter]
    else:
        filtered_df = df
else:
    filtered_df = df

# Metrics Display
col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Records Displayed", value=len(filtered_df))
with col2:
    if 'country' in df.columns:
        st.metric(label="Unique Countries", value=filtered_df['country'].nunique())

# Data Table View
st.subheader("Customer Data View")
st.dataframe(filtered_df, use_container_width=True)

# Visualizations
if 'country' in df.columns:
    st.subheader("Customer Distribution by Country")
    country_counts = filtered_df['country'].value_counts().reset_index()
    country_counts.columns = ['Country', 'Count']
    st.bar_chart(country_counts.set_index('Country'))
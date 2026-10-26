import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Enterprise Customer Intelligence Platform", page_icon="📈", layout="wide")

@st.cache_resource
def get_engine():
    user = os.getenv("DB_USER", "postgres")
    password = os.getenv("DB_PASSWORD")
    host = os.getenv("DB_HOST", "localhost")
    port = os.getenv("DB_PORT", "5432")
    dbname = os.getenv("DB_NAME", "customer_analytics_db")
    return create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{dbname}")

try:
    engine = get_engine()
    query = "SELECT * FROM customers;"
    df = pd.read_sql(query, engine)
except Exception as e:
    st.error(f"Database connection error: {e}. Check your .env file configuration.")
    st.stop()

st.title("📈 Enterprise Customer Intelligence Platform")
st.markdown("End-to-end data analytics and engineering pipeline optimized for performance and scalability.")

# Navigation Tabs
tab1, tab2, tab3 = st.tabs(["📊 Executive Overview", "🔍 Segment Analysis", "📁 Data Explorer & Export"])

with tab1:
    st.subheader("Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customer Base", f"{len(df):,}")
    if 'country' in df.columns:
        col2.metric("Active Regions", df['country'].nunique())
    if 'industry' in df.columns:
        col3.metric("Monitored Industries", df['industry'].nunique())
        
    st.divider()
    if 'country' in df.columns:
        st.subheader("Regional Distribution Analysis")
        country_counts = df['country'].value_counts().reset_index()
        country_counts.columns = ['Country', 'Customer Count']
        st.bar_chart(country_counts.set_index('Country'))

with tab2:
    st.subheader("Advanced Segment Filtering")
    if 'country' in df.columns:
        selected_country = st.selectbox("Filter by Country", options=['All'] + list(df['country'].dropna().unique()))
        filtered_df = df if selected_country == 'All' else df[df['country'] == selected_country]
    else:
        filtered_df = df
        
    st.dataframe(filtered_df.head(100), use_container_width=True)
    st.caption("Showing preview of first 100 rows matching filter criteria.")

with tab3:
    st.subheader("Full Dataset Explorer & Export")
    st.dataframe(df, use_container_width=True)
    
    csv_data = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download Processed Dataset as CSV",
        data=csv_data,
        file_name="processed_customer_analytics.csv",
        mime="text/csv",
    )
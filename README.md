# 🚀 Enterprise Customer Analytics Pipeline

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-Data%20Warehouse-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-BI%20Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-ORM-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white" />
</p>

An end-to-end, production-grade data engineering and business intelligence solution designed to ingest, clean, index, persist, and visualize **100,000+ enterprise customer records** with high-performance reliability.

---

## 🏗️ Architecture & Data Flow

```text
[Raw CSV Dataset] 
       │
       ▼ (Python ETL & Production Logging)
[Pandas Preprocessing Engine] 
       │
       ▼ (SQLAlchemy & Psycopg2 Drivers)
[PostgreSQL Data Warehouse (Indexed for Performance)]
       │
       ▼ (Multi-Tab App UI & Cached Queries)
[Streamlit Enterprise Intelligence Dashboard]



✨ Key Engineering Highlights
🔒 Secure Configuration: Decouples sensitive database credentials using environment variables (.env).
🧹 Automated Data Quality & Logging: Standardizes schemas to snake_case, handles missing parameters, and tracks telemetry via Python's built-in logging module.
⚡ Database Indexing: Implements automated SQL indexing (CREATE INDEX) to guarantee sub-second analytical query performance on large datasets.
📊 Interactive Multi-Tab BI Interface: Features a responsive multi-tab Streamlit web application complete with executive KPIs, dynamic segment filtering, and on-demand CSV dataset export.
📈 Verifiable Development History: Built using a strict multi-commit architectural workflow demonstrating modular software design practices.



📂 Project Directory Structure
customer-analytics-pipeline/
├── data/
│   ├── customers.csv             # Raw input dataset (100k records)
│   └── cleaned_customers.csv     # Preprocessed data artifact
├── notebooks/
│   └── 01_data_cleaning.ipynb    # Exploratory data analysis & validation
├── scripts/
│   ├── clean_data.py             # Automated ETL preprocessing script
│   └── load_postgres.py          # Database ingestion and indexing pipeline
├── sql/
│   └── analytics_queries.sql     # Warehouse aggregation queries
├── .env                          # Local environment credentials (git-ignored)
├── app.py                        # Streamlit multi-tab web application
├── requirements.txt              # Project dependency manifest
└── README.md                     # Project documentation



⚙️ Local Installation & Execution Guide
1. Clone Repository & Install Dependencies

git clone [https://github.com/YourUsername/customer-analytics-pipeline.git](https://github.com/YourUsername/customer-analytics-pipeline.git)
cd customer-analytics-pipeline
pip install -r requirements.txt



2. Configure Environment Variables
Create a .env file in the root directory and configure your PostgreSQL connection:

DB_USER=postgres
DB_PASSWORD=your_actual_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=customer_analytics_db



3. Run the ETL & Database Ingestion Pipeline
Execute the cleaning script to format data, then load it into PostgreSQL:

python scripts/clean_data.py
python scripts/load_postgres.py



4. Launch the Enterprise Dashboard

python -m streamlit run app.py



👤 Author & Credits
Developed by: Abhay Panchal
Email: abhaypanchal095@gmail.com
Role: Full-Stack & Data Engineer

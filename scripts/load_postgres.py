import pandas as pd
import os
import logging
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load_to_postgres():
    cleaned_path = os.path.join('data', 'cleaned_customers.csv')
    if not os.path.exists(cleaned_path):
        logging.error("Cleaned dataset missing.")
        return

    logging.info("Reading preprocessed data...")
    df = pd.read_csv(cleaned_path)
    
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")
    
    connection_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(connection_url)
    
    logging.info("Ingesting records into PostgreSQL table 'customers'...")
    df.to_sql('customers', engine, if_exists='replace', index=False)
    
    # Create index for query optimization on large datasets
    with engine.connect() as connection:
        logging.info("Creating database index for performance optimization...")
        connection.execute(text("CREATE INDEX IF NOT EXISTS idx_customer_country ON customers (country);"))
        connection.commit()
        
    logging.info("✅ Database ingestion and indexing completed successfully!")

if __name__ == "__main__":
    load_to_postgres()
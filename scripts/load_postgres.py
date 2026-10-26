import pandas as pd
import os
from sqlalchemy import create_engine

def load_to_postgres():
    cleaned_path = os.path.join('data', 'cleaned_customers.csv')
    
    if not os.path.exists(cleaned_path):
        print(f"❌ Error: {cleaned_path} not found. Please run scripts/clean_data.py first.")
        return

    print("Loading cleaned dataset...")
    df = pd.read_csv(cleaned_path)
    
    # Connect to PostgreSQL (replace 'your_password' with your actual pgAdmin password)
    print("Connecting to PostgreSQL database...")
    engine = create_engine('postgresql://postgres:your_password@localhost:5432/customer_analytics_db')
    
    # Automated table creation and data insertion
    df.to_sql('customers', engine, if_exists='replace', index=False)
    print("✅ Successfully loaded cleaned dataset into PostgreSQL table: 'customers'!")

if __name__ == "__main__":
    load_to_postgres()
    
    
    
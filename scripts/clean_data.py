import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def clean_data():
    os.makedirs('data', exist_ok=True)
    raw_path = os.path.join('data', 'customers.csv')
    output_path = os.path.join('data', 'cleaned_customers.csv')
    
    if not os.path.exists(raw_path):
        logging.error(f"Raw dataset not found at {raw_path}")
        return

    logging.info("Loading raw customer dataset...")
    df = pd.read_csv(raw_path)
    
    # Standardize schema
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    initial_shape = df.shape
    
    # Data Quality & Cleaning
    df = df.dropna(how='all')
    df.fillna('Unknown', inplace=True)
    
    df.to_csv(output_path, index=False)
    logging.info(f"Data successfully cleaned. Shape transformed from {initial_shape} to {df.shape}")

if __name__ == "__main__":
    clean_data()
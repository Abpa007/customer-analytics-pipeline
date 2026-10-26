import pandas as pd
import os

def clean_data():
    raw_path = os.path.join('data', 'customers.csv')
    output_path = os.path.join('data', 'cleaned_customers.csv')
    
    # Check if raw file exists
    if not os.path.exists(raw_path):
        print(f"❌ Error: {raw_path} not found. Please place your raw CSV inside the 'data/' folder.")
        return

    print("Loading raw customer dataset...")
    df = pd.read_csv(raw_path)
    
    # Standardize column names: lowercase, strip spaces, use underscores
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    
    # Drop completely empty rows
    df = df.dropna(how='all')
    
    # Fill missing string/categorical values to prevent downstream database or dashboard errors
    df.fillna('Unknown', inplace=True)
    
    # Save cleaned data to the data folder
    df.to_csv(output_path, index=False)
    print(f"✅ Data successfully cleaned and saved to {output_path}!\nFinal Dataset Shape: {df.shape}")

if __name__ == "__main__":
    clean_data()
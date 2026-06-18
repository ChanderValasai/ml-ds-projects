import pandas as pd
import os

def clean_data(input_path, output_path):
    print(f"Loading raw data from: {input_path}")
    df = pd.read_csv(input_path)

    # 1. Drop useless identifier column
    if 'customerID' in df.columns:
        df.drop('customerID', axis=1, inplace=True)
        print("Dropped 'customerID' column.")

    # 2. Fix the TotalCharges data type trap
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
    missing_count = df['TotalCharges'].isnull().sum()
    
    # 3. Drop the rows with missing TotalCharges
    df.dropna(subset=['TotalCharges'], inplace=True)
    print(f"Forced TotalCharges to numeric. Dropped {missing_count} rows with missing values.")

    # 4. Save the clean dataset to the processed folder
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\n✅ Clean data saved successfully to: {output_path}")
    print(f"Final Dataset Shape: {df.shape}")

if __name__ == "__main__":
    # Define relative paths based on running from the repository root
    RAW_DATA_PATH = "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    PROCESSED_DATA_PATH = "data/processed/cleaned_churn_data.csv"
    
    clean_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)
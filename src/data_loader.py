import pandas as pd
from pathlib import Path

# project root
PROJECT_DIR = Path(__file__).parent.parent
# raw data
RAW_DIR = PROJECT_DIR / "data" / "raw"

def load_retail_data() -> pd.DataFrame:

    excel_path = RAW_DIR / "online_retail.xlsx"
    df = pd.read_excel(
        excel_path,
        parse_dates=["InvoiceDate"],
        engine="openpyxl"
    )
    return df

if __name__ == "__main__":
    print("🔄 Lading data...")
    df = load_retail_data()
    print(f"✅ Data loaded: {len(df)} lines and {len(df.columns)} columns")
    print(df.head())

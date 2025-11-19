import pandas as pd
import numpy as np

# 1) Load raw data
df = pd.read_csv("raw_sales_data.csv", low_memory=False)

# -------------------------------
# 2) CLEAN COLUMN FORMATS
# -------------------------------

# Strip spaces
df.columns = df.columns.str.strip()

# Fix Region formatting
df["Region"] = (
    df["Region"]
    .astype(str)
    .str.replace("S0uth", "South", regex=False)
    .str.replace(" north", "North", regex=False)
    .str.replace("EAST", "East", regex=False)
    .str.replace(" West ", "West", regex=False)
    .str.strip()
)

# -------------------------------
# 3) FIX PRODUCT NAMES
# -------------------------------
product_clean = {
    "mobile": "Mobile",
    "MOBILE": "Mobile",
    " Mobile ": "Mobile",
    "@@Mobile": "Mobile",
    "Mobille": "Mobile",

    "tablet": "Tablet",
    "TABLET": "Tablet",
    "TABLET ": "Tablet",
    "Tabllet": "Tablet",
    " Tablet": "Tablet",

    "headphone": "Headphones",
    "Head Phones": "Headphones",
    "HeadPhones ": "Headphones",
    "head-phone": "Headphones",

    "LAPTOP": "Laptop",
    " laptoop": "Laptop",
    "LAP-TOP": "Laptop",
    "Laptop###": "Laptop",
}

df["Product"] = (
    df["Product"]
    .astype(str)
    .str.strip()
    .map(lambda x: product_clean[x] if x in product_clean else x)
)

# -------------------------------
# 4) FIX DATE FORMAT
# -------------------------------
def clean_date(val):
    try:
        return pd.to_datetime(val, errors="coerce")
    except:
        return pd.NaT

df["Order_Date"] = df["Order_Date"].apply(clean_date)

# Remove rows where date could not be fixed
df = df.dropna(subset=["Order_Date"])

# -------------------------------
# 5) FIX NUMERIC COLUMNS
# -------------------------------
numeric_cols = ["Quantity", "Unit_Price", "Sales", "Profit"]

for col in numeric_cols:
    df[col] = (
        df[col]
        .astype(str)
        .str.replace(",", "")
        .str.replace("Rs", "")
        .str.replace(" ", "")
        .str.replace("units", "")
        .str.replace("unit", "")
        .str.extract(r"(\d+\.?\d*)")  # extract numbers
    )

    df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows with missing numbers
df = df.dropna(subset=numeric_cols)

# -------------------------------
# 6) REMOVE DUPLICATES
# -------------------------------
df = df.drop_duplicates()

# -------------------------------
# 7) REMOVE OUTLIERS (optional)
# -------------------------------
df = df[df["Quantity"] < 50]
df = df[df["Sales"] < 500000]
df = df[df["Profit"] > -1000]

# -------------------------------
# 8) SAVE CLEANED DATA
# -------------------------------
df.to_csv("cleaned_sales_data_python.csv", index=False)

print("Cleaning complete! Saved as cleaned_sales_data_python.csv")

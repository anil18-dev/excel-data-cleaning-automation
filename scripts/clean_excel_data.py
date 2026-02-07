# Author: Anil Dangi
# Client Data Cleaning – Large Dataset (Robust Version)

import pandas as pd
import re
from pathlib import Path

INPUT_FILE = "data/raw_client_data.csv"
OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "cleaned_client_data.xlsx"

OUTPUT_DIR.mkdir(exist_ok=True)

# Read raw CSV
df = pd.read_csv(INPUT_FILE)

print("Raw rows:", len(df))
print("Raw columns:", df.shape[1])

raw_col = df.columns[0]

pattern = re.compile(
    r"(?P<Product>[A-Za-z ]+)"
    r"(?P<Region>Mid-west|West|East|North|South)"
    r"(?P<Agent_ID>AID_\d+)"
    r"(?P<Customer>Individual|SME|Large Corporate|Non-profit)"
    r"(?P<Call_Duration>\d+)"
    r"(?P<Resolved>Yes|No)"
    r"#(?P<Satisfaction>\d+\.\d+)"
    r":(?P<Upsell_Amount>\d+)"
)

def parse_row(text):
    match = pattern.search(str(text))
    if match:
        return match.groupdict()
    return None

# Apply parsing
parsed = df[raw_col].apply(parse_row)

# 🚀 DROP FAILED ROWS
parsed_clean = parsed.dropna()

print("Parsed rows:", len(parsed_clean))
print("Dropped rows:", len(parsed) - len(parsed_clean))

# Build DataFrame
clean_df = pd.DataFrame(list(parsed_clean))

# Convert numeric columns
clean_df["Call_Duration"] = pd.to_numeric(clean_df["Call_Duration"])
clean_df["Satisfaction"] = pd.to_numeric(clean_df["Satisfaction"])
clean_df["Upsell_Amount"] = pd.to_numeric(clean_df["Upsell_Amount"])

# Save output
clean_df.to_excel(OUTPUT_FILE, index=False)

print("✅ CLEANING DONE")
print("Final rows:", len(clean_df))
print("Saved to:", OUTPUT_FILE)
print("Author: Anil Dangi")

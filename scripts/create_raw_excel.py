import pandas as pd

raw_data = {
    "Data": [
        "Desktop Mid-west AID_001 Individual 94 Yes 3.2 170",
        "Laptop West AID_002 SME 83 Yes 2.4 250",
        "Misc North AID_003 Individual 76 Yes 2.7 160",
    ]
}

df = pd.DataFrame(raw_data)
df.to_excel("data/raw_client_data.xlsx", index=False)

print("Raw Excel file created")

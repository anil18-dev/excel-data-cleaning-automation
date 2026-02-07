# Excel Data Cleaning Automation using Python

## 📌 Project Overview
This project demonstrates a real-world **Excel/CSV data cleaning automation workflow** using Python.  
It simulates a **client-provided messy dataset**, applies robust parsing and validation logic, and produces a **clean, structured Excel output** ready for analysis or reporting.

This project is designed as a **portfolio example for Fiverr and freelance clients**.

---

## 🧩 Problem Statement (Client Requirement)
The client provided a large Excel/CSV file where:
- All information was merged into a single column
- Data was inconsistent and difficult to analyze
- Manual cleaning was time-consuming and error-prone

### Client wanted:
- Properly separated columns
- Clean, structured Excel output
- Automated solution for large datasets

---

## 🗂️ Project Structure
excel-data-cleaning-automation/ │ ├── data/ │   └── raw/ │       └── raw_client_data.csv │ ├── scripts/ │   ├── create_raw_excel.py │   └── clean_excel_data.py │ ├── output/ │   └── cleaned_client_data.xlsx │ ├── docs/ │ ├── venv/ ├── .gitignore └── README.md

---

## ⚙️ Technologies Used
- Python
- Pandas
- Regular Expressions (Regex)
- Excel / CSV Processing
- Git & GitHub

---

## 🧠 Data Cleaning Logic
- Reads raw CSV data from client
- Extracts structured fields using **Regex parsing**
- Drops invalid or corrupted rows
- Converts numeric columns safely
- Exports cleaned data to Excel format

---

## 🧪 Sample Output Columns
- Product  
- Region  
- Agent_ID  
- Customer Type  
- Call Duration  
- Resolved Status  
- Satisfaction Score  
- Upsell Amount  

---

## 🚀 How to Run the Project
```bash
pip install pandas
python scripts/clean_excel_data.py

Result
Raw messy data → Clean structured Excel file
Fully automated workflow
Suitable for large datasets
Ready for business reporting or analysis

👨‍💻 Author
Anil Dangi

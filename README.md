# 📊 Top 10 Largest Banks by Market Capitalization – ETL Project

This project extracts, transforms, and loads data on the **top 10 largest banks in the world by market capitalization (USD)**. The data is scraped from a Wikipedia snapshot and processed to include values in **GBP, EUR, and INR** using an external exchange rate file.

---

## 🔧 Project Structure

- **ETL Script:** `banks_project.py`  
- **Log File:** `code_log.txt`  
- **CSV Output:** `Largest_banks_data.csv`  
- **Database:** `Banks.db`  
- **Table Name:** `Largest_banks`  
- **Exchange Rate File:** [`exchange_rate.csv`](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv)

---

## 🚀 Steps Performed

### 1. Extract
- Data scraped from [Wikipedia (Archived)](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks)
- Top 10 banks ranked by market capitalization in USD

### 2. Transform
- Read exchange rates from CSV
- Converted market cap to:
  - `MC_GBP_Billion`
  - `MC_EUR_Billion`
  - `MC_INR_Billion`
- Rounded to 2 decimal places

### 3. Load
- Saved transformed data to CSV: `Largest_banks_data.csv`
- Loaded into SQLite database: `Banks.db`, table: `Largest_banks`

### 4. Query
- Selected:
  - All rows from the table
  - Average market cap in GBP
  - Top 5 banks by name

---

## 📁 Files Included

| File Name              | Description                           |
|------------------------|---------------------------------------|
| `banks_project.py`     | Main ETL script                       |
| `code_log.txt`         | Execution log with timestamps         |
| `Largest_banks_data.csv` | Output CSV file                    |
| `Banks.db`             | SQLite database file                  |
| `exchange_rate.csv`    | Input file for currency exchange rates|

---

## 🛠️ How to Run

### 1. Install Dependencies

Make sure you have **Python 3.11** installed. Then install the required libraries using:

```bash
python3.11 -m pip install requests pandas beautifulsoup4 numpy
```
### 2. Download Exchange Rate CSV
Use wget to download the exchange rate file required for currency conversion:
```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv
```
### 3. Run the ETL Script
```bash
python3.11 banks_project.py
```
After running, the following files will be generated:

Largest_banks_data.csv — the processed data

Banks.db — SQLite database containing the Largest_banks table

code_log.txt — a timestamped log of all ETL step



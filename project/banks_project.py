import sqlite3
import datetime 
import pandas as pd
import requests 
from bs4 import BeautifulSoup
import numpy as np

# Constants
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"]
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './Largest_banks_data.csv'
exchange_rate_csv = 'exchange_rate.csv'

# Task 1: Logging function
def log_progress(message):  
    timestamp_format = '%Y-%m-%d %H:%M:%S'
    now = datetime.datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("code_log.txt","a") as f:
        f.write(f"{timestamp}: {message}\n")

# Task 2: Extraction function
def extract(url , table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page , 'html.parser')
    tables = data.find_all('table', class_='wikitable')
    rows = tables[0].find_all('tr')

    df = pd.DataFrame(columns=table_attribs)

    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            try:
                name = cols[1].text.strip()
                market_cap = cols[2].text.strip().replace(',', '')
                market_cap = float(market_cap)
                df_c = pd.DataFrame({'Name':[name], 'MC_USD_Billion' : [market_cap]})
                df = pd.concat([df , df_c] , ignore_index=True)
            except:
                continue
    return df.head(10)

# Task 3: Transformation function
def transform(df, exchange_csv_path):
    exchange_df  = pd.read_csv(exchange_csv_path)
    exchange_rate  = exchange_df.set_index('Currency').to_dict()['Rate']

    df['MC_GBP_Billion'] = [np.round(x * exchange_rate['GBP'], 2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x * exchange_rate['EUR'], 2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x * exchange_rate['INR'], 2) for x in df['MC_USD_Billion']]

    return df
def load_to_csv(df , csv_path):
    df.to_csv(csv_path , index = False)

def load_to_db(df , sql_connection , table_name):
    df.to_sql(table_name , sql_connection , if_exists = 'replace' , index = False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement , sql_connection)
    print(query_output)
log_progress("Preliminaries complete. Initiating ETL process")

# Extraction
df = extract(url, table_attribs)
log_progress("Data extraction complete. Initiating Transformation process")

# Transformation
df = transform(df, exchange_rate_csv)
log_progress("Data transformation complete. Initiating Loading process")

# Save to CSV
load_to_csv(df, csv_path)
log_progress("Data saved to CSV file")

# Save to SQLite Database
sql_connection = sqlite3.connect(db_name)
log_progress("SQL Connection initiated")

load_to_db(df, sql_connection, table_name)
log_progress("Data loaded to Database as a table, Executing queries")

# Run Queries
run_query("SELECT * FROM Largest_banks", sql_connection)
run_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks", sql_connection)
run_query("SELECT Name FROM Largest_banks LIMIT 5", sql_connection)
log_progress("Process Complete")

# Close connection
sql_connection.close()
log_progress("Server Connection closed")
# Python ETL Pipeline — MySQL to Google Sheets

## Project Overview

An automated ETL pipeline built with Python to extract data from MySQL, transform the data into a Google Sheets-compatible format, and load the result into Google Sheets.

**Flow:**

```text
MySQL → Python → Transform → Google Sheets → BI Dashboard
```

## Tools & Technologies

* Python
* MySQL
* MySQL Connector/Python
* Google Cloud
* Google Sheets API
* Google Drive API
* gspread
* VS Code

## Project Process

The pipeline was developed step-by-step, starting from the Python environment and MySQL connection, followed by data extraction, transformation, Google authentication, testing, and finally loading the processed data into Google Sheets.

Detailed development steps are documented in:

`development_steps.py`

The final implementation is available in:

`pipeline.py`

## Key Python Implementation

### MySQL Connection

```python
db = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="sql_case_study",
    user="root",
    password="YOUR_PASSWORD"
)

cursor = db.cursor()
```

### Extract Data

```python
cursor.execute("""
    SELECT *
    FROM view_summary_master
""")

rows = cursor.fetchall()
```

### Transform Data

MySQL data types such as `date`, `datetime`, and `Decimal` are converted into formats that can be processed by Google Sheets.

```python
if isinstance(value, (date, datetime)):
    new_row.append(value.isoformat())

elif isinstance(value, Decimal):
    new_row.append(float(value))
```

### Load to Google Sheets

```python
worksheet.update(
    range_name="A1",
    values=[headers]
)

worksheet.update(
    range_name="A2",
    values=data
)
```

## Evidence & Results

The pipeline was successfully tested from MySQL extraction through Google Sheets loading.
1. Python Check
<img width="1477" height="752" alt="1  python check" src="https://github.com/user-attachments/assets/5c6a8178-f299-4f56-9829-4edccda7822b" />

2. Check Connector Mysql
   <img width="1471" height="751" alt="2  check connector mysql" src="https://github.com/user-attachments/assets/b15ca787-8457-48c5-b6b0-4ae862332e49" />

3. Make Folder in VS Code
   <img width="307" height="195" alt="3  buat folder di vscode" src="https://github.com/user-attachments/assets/4b6544a1-b260-4184-9d8b-a227796ded30" />

4. Test Connetion
    <img width="906" height="391" alt="4  test connection" src="https://github.com/user-attachments/assets/71201533-a15e-4d9b-8624-a0cd66646a8f" />

5.1 Make Project Google Cloud
    <img width="1037" height="746" alt="5 1 buat projct google cloud" src="https://github.com/user-attachments/assets/4ba3a11a-96b0-4910-8b6c-53be94f1cf17" />

5.2 Google Sheet API
    <img width="757" height="471" alt="5 2 google sheets api" src="https://github.com/user-attachments/assets/4178720c-1343-494d-8f9c-0bad498329e7" />

5.3 Google Drive API
    <img width="657" height="376" alt="5 3 google drive api" src="https://github.com/user-attachments/assets/71f417f0-bc50-4da1-b508-799360375a9f" />

5.4 Service Account
    <img width="786" height="732" alt="5 4 service_account" src="https://github.com/user-attachments/assets/e837475e-7b2c-4881-9505-a0ccd07fb896" />

6. Data Gsheet
   <img width="1812" height="880" alt="6  data gsheet" src="https://github.com/user-attachments/assets/e1d503b0-56e9-4ccd-be95-4af722ac6915" />

### Final Result

The processed MySQL data was successfully loaded into the `SUMMARY MASTER` worksheet in Google Sheets.

## Project Structure

```text
Python-MySQL-GSheets-ETL/
│
├── README.md
├── pipeline.py
├── development_steps.py
├── screenshots/
└── .gitignore
```

## Notes

`service_account.json` contains sensitive Google credentials and is intentionally excluded from the repository.

The complete working pipeline is available in `pipeline.py`.

| Looker Studio          | BI dashboard and data visualization |
| Visual Studio Code     | Development environment             |




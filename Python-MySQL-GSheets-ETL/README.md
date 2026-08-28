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

Screenshots of the development and execution process are available in the [`screenshots`](screenshots/) folder.

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




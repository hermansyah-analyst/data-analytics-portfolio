```python
# ==========================================
# PYTHON MYSQL TO GOOGLE SHEETS ETL PIPELINE
# ==========================================

import mysql.connector
import gspread

from google.oauth2.service_account import Credentials
from datetime import date, datetime
from decimal import Decimal


# ==========================================
# 1. CONNECT TO MYSQL
# ==========================================

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    database="sql_case_study",
    user="root",
    password="YOUR_MYSQL_PASSWORD"
)

cursor = db.cursor()

print("MySQL berhasil terhubung")


# ==========================================
# 2. EXTRACT DATA FROM MYSQL
# ==========================================

cursor.execute("""
    SELECT *
    FROM view_summary_master
""")

rows = cursor.fetchall()

columns = cursor.description
headers = [column[0] for column in columns]


# ==========================================
# 3. GOOGLE AUTHENTICATION
# ==========================================

credentials = Credentials.from_service_account_file(
    "service_account.json",
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]
)

gc = gspread.authorize(credentials)

print("Google authentication berhasil")


# ==========================================
# 4. OPEN GOOGLE SHEETS
# ==========================================

sheet = gc.open("BNETFIT MASTER DATA")

print("Spreadsheet berhasil dibuka")

worksheet = sheet.worksheet("SUMMARY MASTER")

print("Worksheet berhasil dibuka")


# ==========================================
# 5. TRANSFORM DATA
# ==========================================

data = []

for row in rows:

    new_row = []

    for value in row:

        if isinstance(value, (date, datetime)):
            new_row.append(value.isoformat())

        elif isinstance(value, Decimal):
            new_row.append(float(value))

        else:
            new_row.append(value)

    data.append(new_row)


# ==========================================
# 6. LOAD DATA TO GOOGLE SHEETS
# ==========================================

worksheet.clear()

worksheet.update(
    range_name="A1",
    values=[headers]
)

worksheet.update(
    range_name="A2",
    values=data
)

print("Data berhasil dikirim ke Google Sheets")


# ==========================================
# 7. CLOSE MYSQL CONNECTION
# ==========================================

cursor.close()
db.close()

print("Koneksi MySQL ditutup")
```

# Python MySQL to Google Sheets ETL Pipeline

## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline built with Python.

The pipeline extracts data from a MySQL database, transforms selected data types to ensure compatibility with Google Sheets, and loads the processed data into a Google Sheets worksheet.

The resulting dataset can then be used as a data source for BI dashboard development.

### Pipeline

**MySQL → Python → Google Sheets → BI Dashboard**

### Objective

The objective of this project is to demonstrate a practical data pipeline that connects a relational database with a cloud-based spreadsheet for reporting and business intelligence purposes.

The project covers:

* Connecting Python to MySQL
* Extracting data using SQL
* Processing and transforming data with Python
* Handling database data types such as `date`, `datetime`, and `Decimal`
* Connecting Python to Google Sheets using a Service Account
* Loading processed data into Google Sheets
* Preparing the dataset for BI visualization


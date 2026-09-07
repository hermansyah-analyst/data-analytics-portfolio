# Sales Performance Analysis

## Project Overview

Sales Performance Analysis is an end-to-end reporting and analytics project developed 
to help management monitor sales performance across multiple regions.
The project started from a manual Excel reporting process and was gradually improved 
into a more structured and automated workflow using SQL, Python, Google Sheets, Power BI, and Looker Studio.

---

## Situation

Initially, the company needed a centralized reporting system to combine sales information from multiple regions into one management report.
At that time, the company had 5 regions, and each region provided its own data. The challenge was that there was no standard reporting system yet, and management needed a clearer view of overall sales performance.

I started by building the reporting structure from scratch, including deciding what information should be displayed and how the data should be prepared based on management needs.

The first version of the report was built using Excel. I processed raw data, performed data cleaning, created summary tables, and designed a master report 
containing sales performance, revenue, vendor performance, and manpower information.

As the business grew, the number of regions increased from 5 to 15 regions, with more than 500 salespeople. The increasing amount of data made 
the manual Excel process less efficient and created a higher risk of errors.

---

## Task

My responsibility was to develop a reporting system that could:

* Combine data from multiple regions into one centralized report
* Create a consistent reporting format across regions
* Reduce repetitive manual work
* Provide management with easier access to sales information
* Build a reporting process that could support business growth

---

## Action

### 1. Building the Initial Reporting System Using Excel

I started by creating the first reporting system using Excel.

The process included:
* Cleaning raw data
* Creating standardized summary tables
* Building a master report structure

I used Excel tools such as:
* Pivot Table
* SUMIFS
* COUNTIFS
* VLOOKUP

The summary master became the main reference for reporting across all regions.
However, as the business expanded, the manual process of preparing and combining reports became inefficient. The reporting process that initially required approximately 6 hours of work needed to be improved.

---

### 2. Moving Data Processing to SQL

To handle larger amounts of data and reduce manual processing, I moved the data preparation process from Excel to SQL.
Since the company did not have a database server at that time, I built the process locally using SQL and DBeaver.
I created a structured data flow:

Raw Data
↓
Cleaning Process
↓
Reporting Ready Data
↓
Summary Master

By moving the data processing logic into SQL:
* Data cleaning became more consistent
* Summary tables could be generated more efficiently
* Manual copy-paste work was reduced

The reporting process became faster and more reliable.

---

### 3. Developing Online Reporting with Google Sheets and BI Dashboard

As management needs grew, the requirement changed from simply having reports to having reports that could be accessed anytime and anywhere.

At this stage, I moved the reporting layer from Excel to Google Sheets. The purpose was not to change the reporting structure, but to make the existing summary reports easier to access, share, and monitor without depending on local Excel files.

The summary format remained similar to the previous Excel report, containing sales performance, revenue, vendor performance, and other business summaries.

After the reporting became available online, management started to require a more concise and interactive way to understand the information. Instead of reviewing multiple summary tables, they needed a dashboard that could present key information faster.

I started developing interactive dashboards using BI tools.

I initially used Power BI to create visual dashboards and improve report readability. However, publishing and sharing Power BI dashboards required additional costs, which became a consideration for the company.

To provide a more practical and cost-efficient solution, I explored Looker Studio.

The final dashboard workflow became:

SQL Processing
↓
Google Sheets
↓
Looker Studio Dashboard

---

### 4. Automating Reporting Process Using Python

Although the reporting system was already improved, there was still a manual step: transferring processed data from SQL into Google Sheets.

To reduce repetitive work and minimize copy-paste errors, I developed a Python automation process.

Python was used to:

* Process the output from SQL
* Automatically update Google Sheets
* Reduce manual reporting activities

The final workflow became:

Import Raw Data
↓
Execute SQL Process
↓
Python Automation
↓
Refresh Looker Studio Dashboard

---

## Result

The reporting process was transformed from a manual reporting workflow into an automated analytics system.

Key improvements:

* Reduced reporting preparation time from approximately **6 hours to less than 30 minutes**.
* Scaled reporting capability from **5 regions to 15 regions** and supported **500+ salespeople**.
* Automated data preparation and reporting flow, reducing manual copy-paste processes and potential human errors.
* Enabled online dashboard access for multiple management levels, from **CEO, VP, Manager, to Supervisor**.

Final workflow:

**Import Raw Data → Execute SQL → Automated Update → Refresh Dashboard**


## Tools

* **Excel** — Initial data cleaning, summary, and reporting
* **MySQL / SQL** — Data cleaning, transformation, and reporting
* **DBeaver** — Local database and SQL environment
* **Python** — Reporting automation
* **Google Sheets** — Online reporting and data source
* **Power BI** — Interactive dashboard development
* **Looker Studio** — Final online dashboard

**01 - Summary Table Excel:**
<img width="901" height="552" alt="SUMMARY TABEL " src="https://github.com/user-attachments/assets/265d5c30-9243-470f-9fc3-347d59a5ca17" />

**02 — Power BI Dashboard:**
<img width="1327" height="742" alt="netcom" src="https://github.com/user-attachments/assets/7d2bfaf7-bf32-495a-9321-826269a58de9" />

**03 — Looker Studio Dashboard:**
<img width="1462" height="647" alt="netcom looker" src="https://github.com/user-attachments/assets/ce086910-ec49-445b-b59c-d70ac40861f8" />

**04 — Final Reporting Workflow:**
**raw data:**
<img width="1601" height="647" alt="RAW DATA " src="https://github.com/user-attachments/assets/55f41039-0967-4b28-a253-87ff48274d4c" />

**sql:**
<img width="1295" height="840" alt="view_laporan_ready_sql" src="https://github.com/user-attachments/assets/dc992e4b-0912-48d1-a519-a2faf95b0f59" />

**sql:**














# HR & Workforce Analytics

Attrition analysis of 1,470 IBM employees using Python, SQL and Power BI.  
**Key finding:** Sales Representatives have the highest attrition rate (39.8%) — employees who left earned on average $2,000 less per month than those who stayed.

---

## Business Problem

Companies lose significant resources when employees leave — recruitment, training, and lost productivity. This project analyses IBM HR data to answer: **who is most likely to leave, and what factors drive attrition?**

---

## Tools & Stack

| Tool | Purpose |
|------|---------|
| Python (pandas) | Data cleaning, transformation, feature engineering |
| SQL (SQLite) | Data storage and business queries |
| Power BI + DAX | Interactive 3-page dashboard |
| Git / GitHub | Version control |

---

## Dataset

- **Source:** IBM HR Analytics Employee Attrition Dataset (Kaggle)
- **Scope:** 1,470 employees, 35 features
- **Target variable:** Attrition (Yes/No)

---

## Key Findings

- **Overall attrition rate: 16.1%** (237 out of 1,470 employees)
- Employees working **overtime are 3x more likely to leave**
- **Sales Representatives** have the highest attrition rate at 39.8%
- Employees who left earned on average **$2,046 less per month**
- **Single employees** show nearly 2x higher attrition than divorced
- **Frequent travelers** have the highest attrition among travel groups
- High risk profile: overtime + income < $3,000 + low job satisfaction → **avg attrition rate 30.53%**

---

## Project Structure
hr-analytics/
│
├── data/
│   ├── raw/                        # Original dataset
│   └── processed/
│       ├── hr_clean.csv            # Cleaned dataset
│       ├── hr_analytics.db         # SQLite database
│       ├── attrition_overall.csv
│       ├── attrition_by_dept.csv
│       ├── income_by_dept.csv
│       └── high_risk.csv
│
├── 01_load_and_explore.py          # Initial data exploration
├── 02_clean_and_transform.py       # Data cleaning & feature engineering
├── 03_load_to_sqlite.py            # Load data into SQLite
├── 04_run_sql.py                   # SQL business questions
├── 05_export_for_powerbi.py        # Export data for Power BI
└── README.md

---

## Pipeline — Step by Step

### `01_load_and_explore.py`
- Load raw CSV file
- Check dataset shape (1,470 rows × 35 columns)
- Explore attrition distribution, average income, attrition by department

### `02_clean_and_transform.py`
- Check for missing values (none found)
- Remove constant columns: `EmployeeCount`, `Over18`, `StandardHours`
- Convert `Attrition` to numeric: Yes=1, No=0 (`AttritionNum`)
- Save cleaned data to `data/processed/hr_clean.csv`

### `03_load_to_sqlite.py`
- Load cleaned CSV into SQLite database
- Create table: `employees`

### `04_run_sql.py`
- Q1: Overall attrition rate
- Q2: Attrition rate by department
- Q3: Average income by department and attrition
- Q4: High risk employees (overtime + low income + low satisfaction)

### `05_export_for_powerbi.py`
- Export all SQL query results as CSV files for Power BI

---

## Power BI Dashboard

Three-page interactive dashboard built in Power BI Desktop.

**Page 1 — Overview**
- 3 KPI cards: Total Employees, Employees Left, Attrition Rate %
- Attrition Distribution pie chart
- Attrition Rate by Department bar chart
- Attrition Rate by Job Role bar chart
<img width="2040" height="1148" alt="Zrzut ekranu 2026-05-20 150121" src="https://github.com/user-attachments/assets/085a4f3b-7d3f-4eb5-a321-c34c4ed73ca5" />

**Page 2 — Risk Factors**
- Does overtime increase attrition risk?
- Does personal life affect attrition?
- Do lower earners leave more often?
- Does frequent travel drive employees away?
<img width="2042" height="1149" alt="Zrzut ekranu 2026-05-20 150131" src="https://github.com/user-attachments/assets/62094a1e-ffd0-4dcd-8631-9392a4011ee1" />

**Page 3 — High Risk Profiles**
- Who is at highest risk of leaving?
- High Risk Employee Profile table
- KPI: Avg Income & Avg Tenure of high risk group
- Filter by Department slicer
<img width="2040" height="1148" alt="Zrzut ekranu 2026-05-20 150121" src="https://github.com/user-attachments/assets/c1ecfc7c-ae1b-44da-a156-3ae0088f9185" />

---

## Business Recommendations

| Finding | Recommended Action |
|---------|-------------------|
| Overtime drives attrition 3x | Review workload distribution, hire additional staff in overloaded teams |
| Sales Representatives leave most | Investigate compensation structure and career progression in Sales |
| Low earners leave more | Conduct salary benchmarking, especially at Job Level 1–2 |
| Frequent travelers at risk | Review travel policies, consider remote alternatives |
| Single employees at higher risk | Improve work-life balance initiatives and social engagement programs |

---

## How to Run

```bash
# Clone the repository
git clone https://github.com/12listopada/hr-analytics.git
cd hr-analytics

# Install dependencies
pip install pandas

# Run the pipeline in order
python 01_load_and_explore.py
python 02_clean_and_transform.py
python 03_load_to_sqlite.py
python 04_run_sql.py
python 05_export_for_powerbi.py
```

Then open the Power BI `.pbix` file and refresh the data connection.

---

## Author

**Oliwia** — Data Analyst  
[GitHub](https://github.com/12listopada)

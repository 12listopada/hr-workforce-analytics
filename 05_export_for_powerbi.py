import pandas as pd
import sqlite3

conn = sqlite3.connect('data/processed/hr_analytics.db')

# Q1: Overall attrition rate
q1 = """
SELECT 
    Attrition,
    COUNT(*) as count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM employees), 1) as percentage
FROM employees
GROUP BY Attrition
"""

# Q2: Attrition rate by department
q2 = """
SELECT 
    Department,
    COUNT(*) as total,
    SUM(AttritionNum) as left_company,
    ROUND(AVG(AttritionNum) * 100, 1) as attrition_rate
FROM employees
GROUP BY Department
ORDER BY attrition_rate DESC
"""

# Q3: Avg income by attrition and department
q3 = """
SELECT 
    Department,
    Attrition,
    ROUND(AVG(MonthlyIncome), 0) as avg_income
FROM employees
GROUP BY Department, Attrition
ORDER BY Department, Attrition
"""

# Q4: High risk employees
q4 = """
SELECT 
    JobRole,
    COUNT(*) as high_risk_count
FROM employees
WHERE OverTime = 'Yes'
    AND MonthlyIncome < 3000
    AND JobSatisfaction <= 2
GROUP BY JobRole
ORDER BY high_risk_count DESC
"""

# Save all to CSV
pd.read_sql(q1, conn).to_csv('data/processed/attrition_overall.csv', index=False)
pd.read_sql(q2, conn).to_csv('data/processed/attrition_by_dept.csv', index=False)
pd.read_sql(q3, conn).to_csv('data/processed/income_by_dept.csv', index=False)
pd.read_sql(q4, conn).to_csv('data/processed/high_risk.csv', index=False)

print("Exported:")
print("  - data/processed/attrition_overall.csv")
print("  - data/processed/attrition_by_dept.csv")
print("  - data/processed/income_by_dept.csv")
print("  - data/processed/high_risk.csv")

conn.close()
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

# Q4: High risk employees (overtime + low income + low satisfaction)
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

print("=== Q1: OVERALL ATTRITION ===")
print(pd.read_sql(q1, conn))

print("\n=== Q2: ATTRITION BY DEPARTMENT ===")
print(pd.read_sql(q2, conn))

print("\n=== Q3: AVG INCOME BY DEPT & ATTRITION ===")
print(pd.read_sql(q3, conn))

print("\n=== Q4: HIGH RISK EMPLOYEES ===")
print(pd.read_sql(q4, conn))

conn.close()
# 🧠 HR Attrition Analytics Dashboard – Power BI

## 📊 Project Title
**Employee Attrition Analysis using Power BI**

## 📌 Project Description
This project presents a Power BI dashboard to analyze employee attrition data and uncover key factors contributing to employee turnover. The goal is to help HR departments make informed, data-driven decisions to improve employee satisfaction and reduce attrition rates.

---

## 🛠️ Tools & Technologies Used
- Power BI Desktop  
- Microsoft Excel  
- Python  
- Pandas

---

## 📂 Dataset Overview
- **Total Records**: 1470 Employees  
- **Cleaned Columns**: 29 (after removing unnecessary ones)  
- **Target Column**: `Attrition` (Yes/No)

---

## 📑 Dataset Column Details

| Column Name               | Description                                 |
|--------------------------|---------------------------------------------|
| Age                      | Age of the employee                         |
| Attrition                | Whether the employee left (Yes/No)          |
| BusinessTravel           | Travel frequency                            |
| DailyRate                | Daily rate of employee                      |
| Department               | Department name                             |
| DistanceFromHome         | Distance between home and work              |
| Education                | Education level (1–5)                       |
| EducationField           | Field of education                          |
| EnvironmentSatisfaction  | Satisfaction with environment               |
| Gender                   | Male/Female                                 |
| HourlyRate               | Hourly wage                                 |
| JobInvolvement           | Level of job involvement                    |
| JobLevel                 | Job level within organization               |
| JobRole                  | Role/designation                            |
| JobSatisfaction          | Satisfaction with job                       |
| MaritalStatus            | Marital status                              |
| MonthlyIncome            | Monthly salary                              |
| MonthlyRate              | Monthly rate                                |
| NumCompaniesWorked       | Total companies worked before               |
| OverTime                 | Works overtime or not                       |
| PercentSalaryHike        | Percentage salary hike                      |
| PerformanceRating        | Rating given to employee                    |
| RelationshipSatisfaction | Satisfaction with coworkers                 |
| StockOptionLevel         | Stock option level                          |
| TotalWorkingYears        | Total work experience                       |
| TrainingTimesLastYear    | Number of trainings in last year            |
| WorkLifeBalance          | Work-life balance rating                    |
| YearsAtCompany           | Number of years in company                  |
| YearsInCurrentRole       | Years in current role                       |

---

## 🧹 Data Cleaning & Preprocessing
- ✅ Removed unnecessary columns: `EmployeeNumber`, `Over18`, `StandardHours`, `EmployeeCount` etc.
- ✅ Converted appropriate fields to categorical or numerical
- ✅ Ensured data consistency and fixed data types

---

## 📊 Dashboard Structure

### 🧷 Section 1: KPI Cards (Top Row)
| KPI Metric              | Description                                |
|-------------------------|--------------------------------------------|
| Total Employees         | Total number of current employees          |
| Attrition Count         | Total employees who left                   |
| Attrition Rate (%)      | Percentage of employees who left           |
| Average Monthly Income  | Mean salary of all employees               |
| Avg Distance From Home  | Average commute distance                   |

---

### 📈 Section 2: Attrition Overview
| Chart Type              | Visualization                             |
|-------------------------|--------------------------------------------|
| Pie Chart               | Gender vs Attrition                        |
| Stacked Bar Chart       | Job Role vs Attrition                      |
| Clustered Column Chart  | Department vs Attrition Count              |
| 100% Stacked Bar Chart  | Over Time vs Attrition                     |

---

### 📉 Section 3: Trend & Impact Analysis
| Chart Type              | Visualization                             |
|-------------------------|--------------------------------------------|
| Line Chart              | Age vs Attrition Count                     |
| Scatter Plot            | Monthly Income vs Total Working Years      |
| Clustered Column Chart  | Performance Rating vs Avg Monthly Income (Attrition-wise) |
| Donut Chart             | Education vs Attrition                     |
| Bar Chart               | Job Satisfaction vs Attrition              |

---

### 🎛️ Section 4: Slicers (Interactive Filters)
- Department  
- Job Role  
- Marital Status  
- Gender  
- Education Field

These slicers allow dynamic filtering and deep data exploration.

---

## 🔍 Key Insights

- 📌 Employees working **Over Time** are more likely to leave.
- 📌 **Sales Executives** have the highest attrition rate.
- 📌 **Low Job Satisfaction** is directly related to higher attrition.
- 📌 Employees with **lower income and less experience** are more likely to leave.
- 📌 **Distance from Home** has moderate influence on attrition.

---

## ✅ Conclusion
This dashboard helps HR managers and decision-makers understand the root causes behind employee attrition. With easy-to-use interactive visuals and filters, the organization can:

- Monitor attrition trends  
- Identify at-risk groups  
- Take timely actions to improve retention  
- Create a better workplace experience  


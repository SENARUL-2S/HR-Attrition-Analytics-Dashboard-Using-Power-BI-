import pandas as pd 

df=pd.read_csv("C:\\LEVEL-3 SEM-1\\LEVEL-3 SEM-1\\Data Analysis Project\\New folder\\HR_data.csv")

print(df.head(5))
print(df.isnull().sum())
print(df.describe())
#data almost ok 
df.drop(['CF_attrition label', 'CF_current Employee', 'emp no', 'Over18', 'Employee Count', 'Standard Hours', '-2', '0', 'Daily Rate', 'Hourly Rate', 'Monthly Rate'
], axis=1, inplace=True)

print(df.info())

df.to_csv("C:\\LEVEL-3 SEM-1\\LEVEL-3 SEM-1\\Data Analysis Project\\New folder\\Clean_HR_Analytic_data.csv")

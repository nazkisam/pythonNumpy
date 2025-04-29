import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\PLCPP\python\LECTURE\Numpy for Data Science ¦ Full Course ¦ Sagar Chouksey\Numpy\AdvanceNumpy\capstone\indian_employee_data.csv')

print(df.head())


#check the missing values.
print('Total missing values')

print(df.isnull().sum())




df['Salary (INR)'].fillna(df['Salary (INR)'].mean(), inplace = True)

df['Performance Rating'].fillna(df['Performance Rating'].median(), inplace = True)

df.replace([np.inf, -np.inf], np.nan, inplace= True)

df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

df.drop_duplicates(inplace = True)

df['Salary (INR)'] = np.where(df['Salary (INR)'] < 0, df['Salary (INR)'].mean() , df['Salary (INR)'])

salary_mean = df['Salary (INR)'].mean()
salary_std = df['Salary (INR)'].std()
lower_bound = salary_mean - (3 * salary_std)
upper_bound = salary_mean + (3* salary_std)

df = df[(df['Salary (INR)']>=lower_bound) & (df['Salary (INR)']<=upper_bound)]

df.to_csv('cleaned_indian_emp_data.csv' , index = False)

print('completed')
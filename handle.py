import pandas as pd
data={
    "Name":['Harsh',None,'Sachin','Harshit',None,'Krrish'],
    "Age":[34,65,34,23,None,91],
    "Salary":[10000,15000,None,67000,45000,None],
    "Performance":[56,87,None,98,54,23]
}

df= pd.DataFrame(data)
print(df)

df['Age'].fillna(df['Age'].mean(), inplace=True)
print(df)
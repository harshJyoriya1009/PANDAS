'''
1- How big is your dataset
2- What are the names of columns

shapes and columns
'''

import pandas as pd

data={
    "Name":['Harsh','Dev','Sachin','Harshit','Rahul','Krrish'],
    "Age":[34,65,34,23,98,91],
    "Salary":[10000,15000,25000,67000,45000,90000],
    "performance":[56,87,23,98,54,23]
}

df=pd.DataFrame(data)
print(f'Shape: {df.shape}')
print(f'Column name: {df.columns}')
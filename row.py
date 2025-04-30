import pandas as pd

df= pd.read_json("sample_data.json")

print("Display 10 rows of first")
print(df.head())

print("Display 10 rows of last")
print(df.tail())
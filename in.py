import pandas as pd

df= pd.read_json("sample_data.json")

print("Displaying the info of Data set:")
print(df.info())
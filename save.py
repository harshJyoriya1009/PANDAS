import pandas as pd

data={
    "Name": ['Harsh', 'Atif','Prohit','Shubhi','Manu'],
    "Age":['24','45','89','12','90'],
    "City":["Jhansi","Mahobha","Lahore","Allahbad","Knowhere"]
}

df= pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index=False)
# df.to_excel("output.xlsx", index=False)
df.to_json("output.json", index=False)

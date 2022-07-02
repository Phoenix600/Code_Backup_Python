import pandas as pd

#data  = pd.read_csv("database.xlsx")

# setting max_rows parameters to 999(max limit for standard scv)
pd.options.display.max_rows= 999
data  = pd.read_csv("student.csv")
print(data)

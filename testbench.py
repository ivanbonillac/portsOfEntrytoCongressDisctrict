import pandas as pd

df = pd.read_csv("merged-edit.txt", sep=",",names=["Portcode", "Zipcode", "State", "District"])
print(df[df.Portcode.str.contains('3901')])
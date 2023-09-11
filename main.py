# importing libraries
import pandas as pd

# Read the .csv file
# .csv file must be at root path of the project
zipcode_congress_df = pd.read_csv("zip-codes-to-congressional-districts.txt", sep=",", header=None, dtype = {"Zipcode":str, "State":str, "DistrictNum":str }, names=["Zipcode", "State", "DistrictNum"])
zipcode_portcode_df = pd.read_csv("portcode-zipcode.txt", sep=",", header=None, dtype = {"PortCode":str, "Zipcode":str} ,names=["PortCode", "Zipcode"])

# ---TESTING COMMAND LINES
# Display only 3 rows contents of each dataframes and each column datatype
""""
print(zipcode_congress_df.head(3))
print(zipcode_portcode_df.head(3))
print(zipcode_congress_df.dtypes)
print(zipcode_portcode_df.dtypes)
"""

# Checkpoint A
# Code is reading successfully both .csv
# Code is creating df successfully

# Merge both df using Zipcode as a key
zip_state_dis_port_df = pd.merge(zipcode_portcode_df, zipcode_congress_df, on="Zipcode")

# adding 0 to districts under 10 for 00 format
zip_state_dis_port_df['DistrictNum'] = zip_state_dis_port_df['DistrictNum'].astype(str).str.zfill(2)
# replacing districts with 00 to a AL (At large)
zip_state_dis_port_df['DistrictNum'] = zip_state_dis_port_df['DistrictNum'].replace("00", 'AL')
print(zip_state_dis_port_df)
# Checkpoint B
# Code successfully merged both csv into new df using key

# exporting new df to csv, txt
zip_state_dis_port_df.to_csv('zip_state_dis_port_merged.csv', index=False)
zip_state_dis_port_df.to_csv('zip_state_dis_port_merged.txt', index=False)
# Checkpoint C
# Export of merged csv done successful
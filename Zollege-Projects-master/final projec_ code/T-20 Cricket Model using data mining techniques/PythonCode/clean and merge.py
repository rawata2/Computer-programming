# Import necessary modules
import glob, os
import pandas as pd
from pandas import ExcelWriter
import numpy as np



######################################Loadnig of data from the directory
os.chdir("C:/Users/kuldeep/Desktop/Cricket data original/csv data")


# Write the pattern: pattern
pattern = '*.csv'
# Save all file matches: csv_files
csv_files_name = glob.glob(pattern)


# Print the file names
#print(csv_files_name)
# Load the second file into a DataFrame: csv2
df0 = pd.read_csv(csv_files_name[0])
df1 = pd.read_csv(csv_files_name[1])
df2 = pd.read_csv(csv_files_name[2])
df3 = pd.read_csv(csv_files_name[3])
df4 = pd.read_csv(csv_files_name[4])
df5 = pd.read_csv(csv_files_name[5])
df6 = pd.read_csv(csv_files_name[6])
df7 = pd.read_csv(csv_files_name[7])
df8 = pd.read_csv(csv_files_name[8])
df9 = pd.read_csv(csv_files_name[9])
df10 = pd.read_csv(csv_files_name[10])
df11 = pd.read_csv(csv_files_name[11])
df12 = pd.read_csv(csv_files_name[12])

######################################Exploratory data analysis
#print(csv1prin.head())# Done
#print(csv2.head())
#print(csv3.head())
#print(csv4.head())
#print(csv5.head())
#print(csv6.head())
#print(df7.info()) # Done
#print(df8.info()) #

#print(df9.head()) # Done

#print(df10.head()) # Done

#print(csv11.head())
#print(csv12.head())

############################# cleaning 2 files data frame 9 and data frame 10

#print(df9.columns)
#print(df10.columns)

##################### Combining above 2 excel data with country column as  v-look up
#MergeddataFrame1 = pd.merge(df9, df10, on='Country', how='inner')
#m2m = pd.merge(left=df9, right=df10, left_on='Country', right_on='Country')

#result = pd.concat([df9, df10], axis=1, join_axes=[df9.index])

#result = pd.concat([df1, df4], axis=1)
#print(m2m.head())
#m2m.info()
################## Merging df9 and df 10
df9 = df9.rename(columns={'Country1': 'Country'}) ## Renaming column name for merging
Merge1 = pd.merge(left=df9, right=df10, left_on='Country', right_on='Country')
#print(Merge1.head(10))
#print(Merge1.info())
#####################
################## Merging df7 and merge1
df9 = df9.rename(columns={'Country1': 'Country'}) ## Renaming column name for merging
Merge2 = pd.merge(left=Merge1, right=df7, left_on='Country', right_on='Country')
#print(Merge2.head(10))
#print(Merge2.info())

######################### ###########333 merge2 and df8
#Merge3 = pd.concat([Merge2, df8], axis=1, join_axes=[df8.Country])
Merge3 = pd.merge(left=Merge2, right=df8, left_on='Country', right_on='Country')
#print(df8.info())
#print(Merge2.info())
#print(Merge3.info())
############################################
df1 = df1.rename(columns={'Winner': 'Country'}) ## Renaming column name for merging
Merge4 = pd.merge(left=Merge3, right=df1, left_on='Country', right_on='Country')


############ Export merge file

writer = pd.ExcelWriter('C:/Users/kuldeep/Desktop/Cricket data original/Merged.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
Merge4.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()


#print(pd0.head())
#print(df1.info())
#print(Merge3.info())
#print(Merge4.info())
#print(csv3.head())





###########################
# Print the head of csv2
#print(csv2.head())
# Create an empty list: frames
"""
frames = []
#  Iterate over csv_files
for csv in csv_files_name:
    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)
    # Append df to frames
    frames.append(df)
# Concatenate frames into a single DataFrame: uber
All_Files = pd.concat(frames)

# Print the shape of uber
print(All_Files.shape)

# Print the head of uber
print(All_Files.head())
"""

################################################# Exploratory data analysis

#print(Merge4.unique()) # To see the unoque value in the data frame
#print(Merge4.drop_duplicates) # 0
print(Merge4.head())

# Import necessary modules
import glob, os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
#print(csv1.head())# Done
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
#print(Merge4.info())
#print(Merge4.Matches)

################### Conveterting the column name which contains the space
Merge4.columns = [c.replace(' ', '_') for c in Merge4.columns]
#print(Merge4.head())

############### Printing the distinct column name




from sklearn.preprocessing import Imputer
#print(Merge4.columns)


''''''''' #### Split for linear regression
x=Merge4.iloc[:,[20]].values

#print(x.head(5))

y=Merge4.iloc[:,2].values'''''''''''

'''''''''## Split for Multiple linear  regression
print( Merge4.head(5))
x=Merge4.iloc[:,[20,15,1]].values

#print(x.head(5))

y=Merge4.iloc[:,2].values'''''''''

## Split for polynomial linear  regression
#print( Merge4.head(5))
x=Merge4.iloc[:,20:21].values

#print(x.head(5))

y=Merge4.iloc[:,2].values

#print(y.head(5))




################ Droping a errored row

################## Encoding the categorical data


#print(x.head())

#x.drop([170])

#x=np.delete(x, 179, axis=0)
#x=np.delete(x, 1809, axis=0)
#x=np.delete(x, 2019, axis=0)
######### Deleting rows in  array
from pandas import ExcelWriter
from pandas import ExcelFile
#writer = ExcelWriter("F:\\temp-excel.xlsx")
#Merge4.to_excel(writer,'Sheet1',index=False)
#writer.save()



#from sklearn.preprocessing import LabelEncoder , OneHotEncoder
#Labelencoder_X=LabelEncoder()
#x[:,0]=Labelencoder_X.fit_transform(x[:,0])
#Encoder=OneHotEncoder(categorical_features=[0])

#x= Encoder.fit_transform(x).toarray()

#Labencoder_y=LabelEncoder()

#y=Labencoder_y.fit_transform(y)


from sklearn.cross_validation import train_test_split
x_train, x_test ,y_train ,y_test =train_test_split(x,y,test_size=0.2,random_state=0)

## Feature scaling
from sklearn.preprocessing import StandardScaler
sc_x=StandardScaler()
x_train=sc_x.fit_transform(x_train)
x_test =sc_x.fit_transform(x_test)


''''''' ''''#############Linear regression
from sklearn.linear_model import  LinearRegression
regressor =LinearRegression()
regressor.fit(x_train,y_train)

 ####### Predicting    the test set  results
ypred=regressor.predict(x_train)

 # visulaize the training set
plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,regressor.predict(x_train),color='blue')
plt.show()'''''''''

'' '''###### Multiple linear regression

from sklearn.linear_model import LinearRegression
Multiple_regression=LinearRegression()
Multiple_regression.fit(x_train,y_train)

## Prediting the test set result
y_pred=Multiple_regression.predict(x_test) '''''''''


###### Poloynomial  linear regression

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
poly_reg=PolynomialFeatures(degree=2)
x_poly=poly_reg.fit_transform(x)


lin_reg_2=LinearRegression()
lin_reg_2.fit(x_poly,y)

## Visualing the Polynomial regression
plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Points  and Matches Played')
plt.xlabel('Points')
plt.ylabel('Macthes Played')
plt.show()





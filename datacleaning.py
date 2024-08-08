import pandas as pd
data = pd.read_csv('D:/download/01.Data Cleaning and Preprocessing mainflow.csv')
df= pd.DataFrame(data)
pd.set_option('display.max_columns', 50)
print(data)

print("*"*200)

print(data.describe())     # describe the data

print("*"*200)

print("IS NULL",data.isnull().sum())        # null value sum
print("*"*200)

print("IS NULL",data.isnull())  # is data have any null value or not
print("*"*200)

print(data.notnull())          # is data has not null values

print(data.isnull().sum().sum())     # sum of all null values
print("*"*200)

data= data.drop_duplicates()               # if any duplicates are there so remove it
print(data)

print("fill the null values")              # we can fill null values with zero, forward fill, or backward fill
data2= data.fillna(value=0)
print(data2)

#print(data.fillna(method='ffill'))
#print(data.fillna(method='bfill'))
print()
print("*"*200)
print()

import numpy as np                # all data is in form of number so we can import numpy
from scipy import stats

print(data2.columns)                #  we check columns present in it
print("*"*200)
print()

#drop observation column because it is date value and all are numeric value

data2.drop(['Observation'],axis=1,inplace=True)
print(data2.columns)
print("*"*200)
print()

Q1= data2.quantile(0.25)                          # check quantiles
Q3= data2.quantile(0.75)
IQR=Q3-Q1
print(IQR)
print("*"*200)
print()

data2=data2[~((data2<(Q1-1.5*IQR)) & (data2>(Q3+1.5*IQR))).any(axis=1)]
print(data2)
print("*"*200)
print()

print(data2.describe())
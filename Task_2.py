import numpy as np
import pandas as pd

# Load a CSV file into pandas dataframe(df)
df = pd.read_csv('01.Data Cleaning and Preprocessing (1).csv')
print(df.head())

# Filtering data based on conditions
filtered_df = df[df['Y-Kappa'] > 23]
# print(filtered_df.head())

#
# print(df.isnull().sum()) -----> for checking the no. of times a null value appeared in a column.
# print(df.isnull().sum().sum())-----> for the total no. of null values in the csv file.
# 1.1. fill the null values with some values(0)
df2 = df.fillna(value=0)
# 1.2 fill the null values with previous value in the column
df3 = df.fillna(method='pad')
# 1.3 fill the null values with next value in the column
df4 = df.fillna(method='bfill')
# 1.4 fill the null value with the previous value in the row
df5 = df.fillna(method='pad', axis=1)
# 1.5 fill the null value with the next value in the row
df6 = df.fillna(method='bfill', axis=1)
# 1.6 filling different values of null in different columns
df7 = df.fillna({'AAWhiteSt-4 ': 'abcd', 'SulphidityL-4 ': 'efgh'})
# 1.7 filling the null value with the mean value of a column
df8 = df.fillna(value=df['Y-Kappa'].mean())
# 1.8 filling the null value with the max value of a column
df9 = df.fillna(value=df['Y-Kappa'].max())
# 1.9 filling the null value with the min value of a column
df10 = df.fillna(value=df['Y-Kappa'].min())

# 2.1 drop such rows
df11 = df.dropna()   # dropna() function has taken any as the default value of the as any
# 2.2 dropping the whole row if there are any null value in the row
df12 = df.dropna(how='any')
# 2.3 dropping the whole row if all the values in the row are null
df13 = df.dropna(how='all')

# 3. replace them with replace function
df14 = df.replace(to_replace=np.nan, value=777)
# 3.2 replace the null value with interpolate value
df['SulphidityL-4 '] = df['SulphidityL-4 '].interpolate(method='linear')

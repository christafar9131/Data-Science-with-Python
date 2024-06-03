import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('USvideos.csv')

# Summary statistics
print(df.describe())

# Histograms for each numeric variable
df.hist(bins=30, figsize=(15, 10))
plt.suptitle('Distribution of Numeric Variables')
plt.show()

# Box plots to identify outliers
plt.figure(figsize=(15, 10))
sns.boxplot(data=df, orient='h')
plt.title('Box Plots of Numeric Variables')
plt.show()

# Correlation matrix
corr_matrix = df.corr()

# Heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Pair plot
sns.pairplot(df)
plt.suptitle('Pair Plot of Variables', y=1.02)
plt.show()





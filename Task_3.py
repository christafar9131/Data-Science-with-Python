import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('householdtask3.csv')
print(data.head(10))

# -----------------------> Line chart <--------------------------------
plt.plot(data['year'])
plt.plot(data['own'])
# Title
plt.title("Line chart")
# setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
# Adding the legends
plt.show()

# ------------------------> Bar chart/plot <-----------------------------
plt.bar(data['year'], data['own'])
# adding title to the plot
plt.title("Bar Plot")
# setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
# Adding the legends
plt.show()

# -----------------------> Scatter plot <-----------------------------
plt.scatter(data['year'], data['own'])
# adding title to the plot
plt.title("scatter plot")
# setting the x and y labels
plt.xlabel('year')
plt.ylabel('own')
# Adding the legends
plt.show()

# -----------------------> histogram <--------------------------------
plt.hist(data['income'])
plt.title("histogram")
plt.show()

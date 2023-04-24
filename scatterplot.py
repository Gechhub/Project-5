import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load the data from the CSV file
df = pd.read_csv('sales_dataset.csv')

# plot the scatter plot in the figure
# I have chosen the configuration to make the figure accommodate the dataset without congestion
plt.figure(figsize= (20,12), dpi = 200)

# This plots the Salary vs Sales of Professionals in different Global Cities
# The 'hue' argument sets the color of each point based on the 'location' column
# The 'style' argument sets the shape of each point based again on the 'location' column
# The 'size' argument sets the size of each point based on the 'salary' column
# This makes the distribution to appear more distinguishable and the legend hence will have two parameters to read information off.
sns.scatterplot(x='salary', y='sales', data=df, s=20, size='salary', hue='location',style='location')

# Adding title and labels for more clarity
plt.title('Sales Vs Salary distribution in Financial centers of the world')
plt.xlabel('Salary(in $)')
plt.ylabel('Sales(in $)')
plt.legend(loc='lower right')
plt.show()







import pandas as pd

import matplotlib.pyplot as plt

# This specifies the file path which is in the same folder as the python file
file_path = "Geological_dataset.csv"

# create a function which takes the argument csv_path which contains the path to the csv file
def plot_data(csv_path):

    # Load the data
    df = pd.read_csv(csv_path)
    print(df.head())

    # assign the columns to x and y variables
    x = df['Temperature']
    y = df['Precipitation']

    # adjust the figure size based on the size of the data set(which is, 2000x2)
    plt.figure(figsize= (15, 15))

    # Create a scatter plot
    plt.scatter(x,y , c= 'Orange', marker = 'o')
    plt.xlabel('Temperature[°C]', fontsize=14)
    plt.ylabel('Precipitation[mm/a]', fontsize=14)
    plt.title('Geological data plot', c='navy', fontsize=18)
    plt.show()

plot_data(file_path)



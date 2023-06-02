# Project 5:  This Project extracts columns from a Geological dataset and plots a scatterplot.

# A) Dataset
The dataset for this project was the one provided in the Project description and after refering the desciption on the website I have determined the following information.

Rows: correspond to pixels in the analysed global raster data set.

Columns: correspond to

    1.	Elevation(m)                  

    2.	Local relief(m)
    
    3.	Slope (°*10)
    
    4.	Precipitation(mm/a)
    
    5.	Temperature (°C *10)
    
    6.	NDVI Average (0 - 255)
    
    7.	NDVI Max (0 - 255)
    
    8.	Latitude (°N *100)
    
    9.	Ksn
    
    10.	Tetrapoid species richness (# of species)
    
    11.	Amphibian Special Richness (# of species)
    
    12.	Mammal species richness (# of species)
    
    13.	Köppen-Geiger Climate zone
    
    14.	Geologic unit
    
    15.	Landcover
    
    16.	Strain rate (10e-9 /yr)


# B) Columns of Interest
Out of the above Columns I have chosen columns 4 and 5 for my plot which are Temperature[°C] and Precipitation[mm/a] values respectively.

# C) Methods

1) First Part: Linux Implementation

Since the file was a txt file and it was rather not ideal to extract the columns, so I first changed it to a csv file of 2000x2 datapoints using a linux command line as follows.



(echo "Temperature,Precipitation" && awk -F',' '{OFS=","; print $4,$5}' global_data_50mLC2.txt | head -n 2000) > Geological_dataset.csv


P.S: Since the header in the original txt file started with numerical values, this command lines adds the two Headers as shown. They will be the parameters the values pertain to

The output file is then used for the Python Implementation

2) Second Part: Python Implemantation

The columns are hence extracted from the yielded csv file to plot the scatter. This implementation is done through the Scatter.py code.

# C) Tools

Linux Command: Jupyter GWDG platform was used


Python code: Pycharm was used


Contributor: Getabalew Yemane Teshome

ID: 26832510


Sharing: available on Github


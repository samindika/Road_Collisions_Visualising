"import modules"
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# import Dataset - This is used through out the program
df_Collisions = pd.read_csv("Road_Collisions.csv")


# Function to draw the Line plot
def lineplot(index):
    """
    Function 1: A function to create a line plot
    Parameters
    One parameter : index
    index : integer
        Represent years from 2012 to 2021.
    """

    plt.figure(figsize=(9, 6), facecolor="lightgray")

    # plot the line chart for number of accidents from 2012-2021-West Midlands
    plt.plot(index, df_t["Pedestrians"].astype(
        int), label="Pedestrians", linestyle="-")
    plt.plot(index, df_t["Pedal cyclists"].astype(
        int), label="Pedal cyclists", linestyle="-")
    plt.plot(index, df_t["Motorcycle users"].astype(int),
             label="Motorcycle users", linestyle=":", linewidth="2")
    plt.plot(index, df_t["Car occupants"].astype(int),
             label="Car occupants", linestyle=":", linewidth="2")

    # set the current tick locations and labels of the x-axis
    plt.xticks([2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021])

    # labeling
    plt.xlabel("Year")
    plt.ylabel("Number of Road fatalities")
    plt.title(
        "Road Traffic Fatalities by Road User Type - West Midlands(UK)",
        fontweight='bold')

    # removing white space left and right.
    plt.xlim(2012, 2021)
    plt.legend()

    # save as png
    plt.savefig("linplot.png")
    plt.show()


# Function to draw the Bar chart
def barchart(b, bar1, bar2, bar3, bar4):
    """
    Function 2: A function to create a bar chart
    Parameters:
    four parameters : b,bar1,bar2,bar3,bar4
    b : integer
        length of variable x. x is the length of Road User Types in the dataset
    bar1 : integer
        Data in the column "2021" in London Dataframe. Convert data to integer
    bar2 : integer
        Data in the column "2021" in Wales Dataframe. Convert data to integer
    bar3 : integer
        Data in the column "2021" in Scotland Dataframe.Convert data to integer
    bar4 : integer
        Data in the column "2021" in SouthEast Dataframe.Convert data to integer
    """

    plt.figure(figsize=(9, 6), facecolor="lightgray")

    # plot the bar chart for number of accident by Accident type in four region
    plt.bar(b-0.2, bar1, width, color='#06c258', label="London")
    plt.bar(b, bar2, width, color='#ffee78', label="Wales")
    plt.bar(b+0.2, bar3, width, color='#5D3FD3', label="Scotland")
    plt.bar(b+0.4, bar4, width, color='#007AFF', label="South East")

    # set the current tick locations and labels of the x-axis
    plt.xticks(b, ['Pedestrians', 'Pedal cyclists',
               'Motorcycle users', 'Car occupants'], size=10)

    # labeling
    plt.xlabel("Road User types")
    plt.ylabel("Number of Road fatalities")
    plt.title("Road Fatalities in different regions 2021- UK",
              size=12, fontweight='bold')
    plt.legend()

    # save as png
    plt.savefig("barchart.png")
    plt.show()


# Function to draw the Pie chart
def piechart(x, y1, y2, y3, y4):
    """
    Function 3: A function to create pie charts
    Parameters 
    four parameters: x, y1, y2, y3, y4
    x : Object
        Road user types in the dataset.
    y1 : Object
        Number of Road accidents in the North East Region - Year 2018
    y2 : Object
        Number of Road accidents in the North East Region - Year 2019.
    y3 : Object
        Number of Road accidents in the North East Region - Year 2020.
    y4 : Object
        Number of Road accidents in the North East Region - Year 2021.
    """

    plt.figure(figsize=(12, 8))

    # adjust space between plots
    plt.subplots_adjust(hspace=0.4, wspace=0.4)

    # subplot count starts at 1
    plt.subplot(2, 2, 1)

    # plot the pie chart for number of accidents in each type for year 2018
    plt.pie(y1, labels=x, autopct='%1.0f%%', radius=1.2,
            startangle=180, textprops={'fontsize': 10}, shadow=True)
    plt.title("Year - 2018", fontweight="bold")

    # subplot count starts at 2
    plt.subplot(2, 2, 2)

    # plot the pie chart for number of accidents in each type for year 2019
    plt.pie(y2, labels=x, autopct='%1.0f%%', radius=1.2,
            startangle=90, textprops={'fontsize': 10}, shadow=True)
    plt.title("Year - 2019", fontweight="bold")

    # subplot count starts at 3
    plt.subplot(2, 2, 3)

    # plot the pie chart for number of accidents in each type for year 2020
    plt.pie(y3, labels=x, autopct='%1.0f%%', radius=1.2,
            startangle=0, textprops={'fontsize': 10}, shadow=True)
    plt.title("Year - 2020", fontweight="bold")

    # subplot count starts at 4
    plt.subplot(2, 2, 4)

    # plot the pie chart for number of accidents in each type for year 2021
    plt.pie(y4, labels=x, autopct='%1.0f%%', radius=1.2,
            startangle=180, textprops={'fontsize': 10}, shadow=True)
    plt.title("Year - 2021", fontweight="bold")

    # centered title to a chart that contains multiple subplots
    plt.suptitle(
        "Road Fatalities by road user type - North East(UK)",
        fontweight='bold')

    # save as png
    plt.savefig("Piechart.png")
    plt.show()


# =============================================================================
# Main program contains the code to create data frames to plot the three graphs
# line chart, bar chart and pie chart
# =============================================================================

# Line Chart


# Create a new dataframes to filter data from Region and Severity level
df_midlands = df_Collisions[(df_Collisions["Region or Country"] == "West Midlands") & (
    df_Collisions["Severity"] == "Killed")]

# rotates the rows and columns of dataframe
df_t = pd.DataFrame.transpose(df_midlands)

# select the second row of transposed dataframe and make it as column names
df_t.columns = df_t.iloc[2]

# filter out necessary rows,all columns to be plotted in  transposed data frame
df_t = df_t.iloc[4:14, :]

# converts index of DataFrame "df_t" from a non-numeric type to a numeric type.
df_t.index = pd.to_numeric(df_t.index)

# =============================================================================
# bar chart
# =============================================================================

# Create four new dataframes to filter data from Region and Severity level
df_London = df_Collisions[(df_Collisions["Region or Country"] == "London") & (
    df_Collisions["Severity"] == "Killed")]
df_Wales = df_Collisions[(df_Collisions["Region or Country"] == "Wales") & (
    df_Collisions["Severity"] == "Killed")]
df_Scotland = df_Collisions[(df_Collisions["Region or Country"] == "Scotland") & (
    df_Collisions["Severity"] == "Killed")]
df_SouthEast = df_Collisions[(df_Collisions["Region or Country"] == "South East") & (
    df_Collisions["Severity"] == "Killed")]

# Take Road user type of London dataframe to x variable
x = df_London["Road user type"]

# Take data in the column "2021" in  London,Wales,Scotland and South East
# Dataframes in to variables.
# Convert data to integer
bar1 = df_London['2021'].astype(int)
bar2 = df_Wales["2021"].astype(int)
bar3 = df_Scotland["2021"].astype(int)
bar4 = df_SouthEast["2021"].astype(int)

# length of variable x. x is the length of Road User Types in the dataset
b = np.arange(len(x))
width = 0.2

# =============================================================================
# Pie Chart
# =============================================================================

# Create a new dataframes to filter data from Region and Severity level
df_northeast = df_Collisions[(df_Collisions["Region or Country"] == "North East") & (
    df_Collisions["Severity"] == "Killed")]

# Take Road user type of Northeast dataframe to x variable
x = df_northeast["Road user type"]

# filter out Number of accidents of each type for 2018-2021
y1 = df_northeast["2018"]
y2 = df_northeast["2019"]
y3 = df_northeast["2020"]
y4 = df_northeast["2021"]


# calling plots with necessary parameters to be plotted.
lineplot(df_t.index)
barchart(b, bar1, bar2, bar3, bar4)
piechart(x, y1, y2, y3, y4)

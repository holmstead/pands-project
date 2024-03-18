# author MHolmes

import pandas as pd
import matplotlib.pyplot as plt
import os    # for checking if directory exists
#import seaborn as sb

# load local csv into a pandas dataframe
# source:
# https://ocw.mit.edu/courses/15-097-prediction-machine-learning-and-statistics-spring-2012/resources/iris/
# better format source:
# https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv
df = pd.read_csv("iris.csv")

# print head and tail of the dataframe
print(df) 

# view datatypes
print(df.dtypes) 

def summarize_variables(df):
    '''
    This function generates a csv file containing a summary (mean,
    std dev, max, min) of each of the variables in the dataframe.
    '''

    # creat and open textfile
    with open("variables_summary.txt", "w") as f:
        # write to textfile
        f.write(f"variable, mean, standard_deviation, max, min\n")
        f.write(f"{'sepal_length'}, {df['sepal_length'].mean()}, {df['sepal_length'].std()}, {df['sepal_length'].max()}, {df['sepal_length'].min()}\n")
        f.write(f"sepal_width, test, test, test")


def plot_hist(variable):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe
    '''
    # creat a directory for plots if it doenst exist:
    # https://www.w3schools.com/python/ref_os_makedirs.asp
    os.makedirs("plots", exist_ok=True)

    # plot a histogram of the specified variable in the df
    #hist = df.plot.hist(column=["sepal_length"], edgecolor='black')
    plt.hist(df[variable], edgecolor="black")

    # decorate the plot
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {variable}")

    # save plot as png
    plt.savefig(f"plots/Histogram of {variable}.png")

    # display the plot
    plt.show()


def plot_scatter(var1, var2):
    '''
    This function plots a scatterplot from a two given 
    variables in a pandas dataframe
    '''
    # creat a directory for plots if it doenst exist:
    os.makedirs("plots", exist_ok=True)

    # now a scatterplot
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
    x = df[var1]
    y = df[var2]
    plt.scatter(x, y)

    # decorate the plot
    plt.xlabel(var1)
    plt.ylabel(var2)
    #plt.title('Scatterplot of ... ')

    # save plot as png
    plt.savefig(f"plots/{var1} vs {var2}.png")

    # display the plot
    plt.show()


# call functions
plot_hist("sepal_length")
plot_scatter("sepal_length", "sepal_width")
summarize_variables(df)
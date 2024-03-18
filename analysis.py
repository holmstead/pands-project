# author MHolmes

import pandas as pd
import matplotlib.pyplot as plt
import os    # for checking if directory exists
#import seaborn as sb

# load local csv into a pandas dataframe [1]
df = pd.read_csv("iris.csv")

# print head and tail of the dataframe
print(df) 

# view datatypes
print(df.dtypes) 

# view headers
print(df.head)

def summarize_variables(df):
    '''
    This function generates a text file containing a summary
    (mean, std dev, max, min) of each of the variables in 
    the dataframe.
    '''

    # list of variables
    variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    # create and open text file
    with open("variables_summary.txt", "w") as f:
        # write to text file
        f.write(f"variable, mean, standard_deviation, max, min\n")

        # create loop to cycle through variables
        for var in variables:
            # write stats for each variable to the text file
            f.write(f"{var}, {df[var].mean()}, {df[var].std()}, {df[var].max()}, {df[var].min()}\n")


def plot_hist(variable):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe
    '''
    # create a directory for plots if it doenst exist [2]
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

    # now a scatterplot [3]
    # 
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


'''
References:

[1] https://ocw.mit.edu/courses/15-097-prediction-machine-learning-and-statistics-spring-2012/resources/iris/
    https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv

[2] https://www.w3schools.com/python/ref_os_makedirs.asp

[3] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

'''
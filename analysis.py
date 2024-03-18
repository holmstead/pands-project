# author MHolmes

import pandas as pd             # for data analyis
import matplotlib.pyplot as plt # for plotting
import os                       # checking if directory exists
import seaborn as sns           # more plotting


# load local csv into a pandas dataframe [1]
df = pd.read_csv("iris.csv")

# print head and tail of the dataframe
print(df) 

# view datatypes
print(df.dtypes) 

# print a statistical summary of the dataframe
print(df.describe())

# view headers
print(df.columns.tolist())


# define functions
def summarize_variables(df):
    '''
    This function generates a text file containing a summary
    (mean, std dev, max, min) of each of the variables in 
    the dataframe.
    '''

    # list of variables
    variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    # use pandas to generate list of variables from df headers
    #variables = df.columns.tolist()
    print(variables)

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

    # set up the canvas to have subplots
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # plot a histogram of the specified variable in the df
    #hist = df.plot.hist(column=["sepal_length"], edgecolor='black')
    ax.hist(df[variable], edgecolor="black")

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {variable}")

    # save plot as png
    ax.get_figure().savefig(f"plots/Histogram of {variable}.png")
    #ax.savefig(f"plots/Histogram of {variable}.png")

    # display the whole figure
    plt.show()


def plot_scatter(var1, var2):
    '''
    This function plots a scatterplot from a two given 
    variables in a pandas dataframe
    '''
    # creat a directory for plots if it doenst exist:
    os.makedirs("plots", exist_ok=True)

    # set up the canvas to have subplots
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # now a scatterplot [3]
    # 
    x = df[var1]
    y = df[var2]
    ax.scatter(x, y)

    # decorate the plot
    ax.set_xlabel(var1)
    ax.set_ylabel(var2)
    ax.set_title("Iris Dataset")

    # save plot as png
    ax.get_figure().savefig(f"plots/{var1} vs {var2}.png")

    # display the whole figure
    plt.show()


# call functions
plot_hist("sepal_length")
plot_scatter("sepal_length", "sepal_width")
summarize_variables(df)

# plot a grid of scatter plots using seaborn [4]
pairplot = sns.pairplot(df, hue="species")
plt.savefig(f"plots/pairplot.png")
#plt.show()


'''
References:

[1] https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

[2] https://www.w3schools.com/python/ref_os_makedirs.asp

[3] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

[4] Pairplot plots "pairwise relationships in a dataset." 
https://seaborn.pydata.org/generated/seaborn.pairplot.html

'''
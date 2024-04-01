# author MHolmes

import pandas as pd             # for data analyis
import matplotlib.pyplot as plt # for plotting
import os                       # checking if directory exists
import seaborn as sns           # more plotting
import sys


# define functions
def summarize_variables(numeric_df):
    '''
    This function generates a text file containing a summary
    (mean, std dev, max, min) of each of the variables in 
    the dataframe.
    '''

    # list of variables
    #variables = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

    # create and open text file
    with open("variables_summary.txt", "w") as f:
        # write to text file
        f.write(f"variable, mean, standard_deviation, max, min\n")

        # create loop to cycle through variables
        for var in numeric_df:
            # write stats for each variable to the text file
            f.write(f"{var}, {df[var].mean()}, {df[var].std()}, {df[var].max()}, {df[var].min()}\n")


def plot_hist(variable):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe
    '''
    
    # set up the canvas
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
    #plt.show()

    # close figures
    plt.close()


def plot_scatter(var1, var2):
    '''
    This function plots a scatterplot from a two given 
    variables in a pandas dataframe
    '''
    
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
    #ax.set_title("Iris Dataset")

    # save plot as png
    ax.get_figure().savefig(f"plots/{var1} vs {var2}_scatter.png")

    # display the whole figure
    #plt.show()

    # close figures
    plt.close()

def lm_scatter(df, var1, var2, hue):
    '''
    https://seaborn.pydata.org/generated/seaborn.lmplot.html
    '''
    # set up variables
    x = df[var1]
    y = df[var2]

    # scatter plot using lmplot()
    #print(f"lmplot {var1}, {var2}")
    sns.lmplot(data=df, x=var1, y=var2, hue=hue)

    # save plot as png
    plt.savefig(f"plots/{var1} vs {var2}_lmplot_{hue}.png")

    # display the whole figure
    #plt.show()

    # close figures
    plt.close()
    

def create_pairplot(df, hue):
    # plot a grid of scatter plots using seaborn [4]
    fig, ax = plt.subplots(1, 1) 
    ax = sns.pairplot(df, hue=hue)
    ax.savefig(f"plots/pairplot_{hue}.png")
    #plt.show()

    # close figures
    plt.close()

if __name__ == "__main__":
    # load local csv into a pandas dataframe [1]
    #df = pd.read_csv(sys.argv[1])
    df = pd.read_csv(sys.argv[1])

    # print head and tail of the dataframe
    print(f"\nDataframe head and tail:")
    print(df) 

    # view datatypes
    #print(df.dtypes) 

    # print a statistical summary of the dataframe
    #print(df.describe())

    # view headers
    print(f"\nHeaders")
    print(df.columns.tolist())

    # determine numeric and non-numeric columns
    numeric_df = df.select_dtypes(include='number')
    print(f"\nNumeric only headers:")
    print(numeric_df.columns.tolist())
    non_numeric_df = df.select_dtypes(exclude='number')
    print(f"\nNon-numeric headers:")
    print(non_numeric_df.columns.tolist())

    # check which columns we have in numeric_df
    print(f"\nLooping through columns in numeric_df:")
    for var in numeric_df:
        print(var)

    # call the function that summariz each of the variables
    summarize_variables(numeric_df)

    # creat a directory for plots if it doenst exist:
    os.makedirs("plots", exist_ok=True)

    # create loop to cycle through variables
    for var1 in numeric_df:
        print(f"\nPlotting histogram of {var1}")
        plot_hist(var1)
        for var2 in numeric_df:
            # check if variable names match from both loops
            if var1 == var2:
                print(f"\nNot plotting {var1} against {var2}")
                #skip this loop in the for loop if the two variable names match
                continue
            print(f"\nScatter plotting {var1} v {var2}")
            # if they dont match, then they get plotted against each other
            plot_scatter(var1, var2)

            
            for hue in non_numeric_df:
                print(f"Plotting lmplot of {var1} v {var2} with hue={hue}")
                # lmplot() using seaborn
                lm_scatter(df, var1, var2, hue)
    
              
    for hue in non_numeric_df:
        print(f"\nCreating pairplot with hue={hue}") 
        create_pairplot(df, hue)

    # end
    print(f"\nAnalysis complete.")


'''
References:

[1] https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

[2] https://www.w3schools.com/python/ref_os_makedirs.asp

[3] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

[4] Pairplot plots "pairwise relationships in a dataset." 
https://seaborn.pydata.org/generated/seaborn.pairplot.html

'''
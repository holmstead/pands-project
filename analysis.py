# author MHolmes

import pandas as pd             # for data analyis
import matplotlib.pyplot as plt # for plotting
import os                       # checking if directory exists
import seaborn as sns           # more plotting
import sys


# define functions

def plot_hist(df, variable):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe using matplotlibs hist() method.
    - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
    '''
    
    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # matplotlibs hist function takes the df as an arg
    ax.hist(df[variable], bins=10, color="green", edgecolor="black")

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {variable} using matplotlib")

    # save plot as png
    ax.get_figure().savefig(f"plots/Histogram_of_{variable}_using_matplotlib.png")

    # display the whole figure
    #plt.show()

    # close figures
    plt.close()


def plot_scatter(var1, var2):
    '''
    This function plots a scatterplot from a two given 
    variables in a pandas dataframe using matplotlib
    '''
    
    # set up the canvas to have subplots
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # assign variables
    x = df[var1]
    y = df[var2]
    
    # plot using matplotlibs scatter() method
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
    # assign variables
    x = df[var1]
    y = df[var2]

    # scatter plot using lmplot()
    print(f"Creating scatterplot using lmplot of {var1}, {var2}")
    sns.lmplot(data=df, x=var1, y=var2, hue=hue)

    # save plot as png
    plt.savefig(f"plots/{var1} vs {var2}_lmplot_{hue}.png")
    #ax.get_figure().savefig(f"plots/{var1} vs {var2}_lmplot_{hue}.png")
    # display the whole figure
    #plt.show()

    # close figures
    plt.close()
    

def create_pairplot(df, hue):
    # plot a grid of scatter plots using seaborn [4]
    print(f"Creating pairplot using {hue} as hue")

    # set up the canvas
    fig, ax = plt.subplots(1, 1) 
    ax = sns.pairplot(df, hue=hue)
    ax.savefig(f"plots/pairplot_by_{hue}.png")
    #plt.show()

    # close figures
    plt.close()


def create_heatmap(df): 
    # plot a heatmap using seaborn [a]
    fig, ax = plt.subplots(1, 1) 
    ax = sns.heatmap(df.corr(numeric_only=True), annot=True)
    plt.savefig(f"plots/heatmap.png")
    #plt.show()

    # close figures
    plt.close()


def plot_hist_by_species(species_to_plot, var, species):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe
    '''
    
    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    print(f"Species to plot: {species_to_plot}")
    ax.hist(species_to_plot, color="orange",  edgecolor='black')

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {var} - {species}")

    # save plot as png
    ax.get_figure().savefig(f"plots/Hist {var} - {species}.png")
    #ax.savefig(f"plots/Histogram of {variable}.png")

    # display the whole figure
    #plt.show()

    # close figures
    plt.close()



if __name__ == "__main__":
    # load local csv into a pandas dataframe [1]
    df = pd.read_csv(sys.argv[1])

    # print head and tail of the dataframe
    print(f"\nDataframe head and tail:")
    #print(df) 

    # view datatypes
    print(df.dtypes) 


    # print a statistical summary of the dataframe
    print(df.describe())


    # view headers
    print(f"\nAll headers: {df.columns.tolist()}")
 

    # create numeric only df
    numeric_df = df.select_dtypes(include="number")
    print(numeric_df)
    print(f"\nNumeric column headers:")
    # make a list from numeric_columns variable
    print(numeric_df.columns.tolist())
    

    # create df from non-numeric dtypes
    non_numeric_df = df.select_dtypes(exclude="number")
    print(f"\nNon-numeric column headers:")
    print(non_numeric_df.columns.tolist())


    # check which columns we have in numeric_columns
    print(f"\nLooping through column headers in numeric_headers:")
    for column_header in numeric_df:
        print(column_header)


    # write statistical summary to textfile
    # create and open text file
    with open("variables_summary.txt", "w") as f:
        # write to text file
        # convert to string first, cant write <class 'pandas.core.frame.DataFrame'> straight to file
        print(f"{type(numeric_df.describe())} \n")
        f.write(str(numeric_df.describe()) + '\n')



    ## PLOTTING ##

    # creat a directory for plots if it doenst exist:
    os.makedirs("plots", exist_ok=True)


    ## HISTOGRAMS

    # https://realpython.com/python-histograms/

    # plot the entire dataframe using pandas built in hist method
    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 
    # plot histogram using pandas built in hist()
    df.hist(ax=ax) 
    # df.plot.hist() pluts them all on one figure, its a mess
    # ax = df.hist() doesnt work for some reason
    
    # save plot as png
    ax.get_figure().savefig(f"plots/df.hist.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


    ## KDE plots

    # what are kernel density plots:
    # https://en.wikipedia.org/wiki/Kernel_density_estimation
    
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.kde.html



    

    # seaborn KDE
    # https://seaborn.pydata.org/generated/seaborn.kdeplot.html

    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # pass the pandas dataframe in to seaborn
    sns.kdeplot(data=df, ax=ax)

    # save plot as png
    ax.get_figure().savefig(f"plots/kde_seaborn.png")
    plt.tight_layout()
    plt.show()
    plt.close()






    # create loop to cycle through variables and plot hist
    for var1 in numeric_df:
        print(f"\nPlotting histogram of {var1} using matplotlib hist()")
        #plot_hist(df, var1)


    # nested loop through variables to get two variables for scatter
    for var1 in numeric_df:
        for var2 in numeric_df:
            # check if variable names match from both loops
            if var1 == var2:
                print(f"\nNot plotting {var1} against {var2}")
                #skip this loop in the for loop if the two variable names match
                continue
            print(f"\nScatter plotting {var1} v {var2}")
            # if they dont match, then they get plotted against each other
            #plot_scatter(var1, var2)

            
            for hue in non_numeric_df:
                print(f"Plotting lmplot of {var1} v {var2} with hue={hue}")
                # lmplot() using seaborn
                #lm_scatter(df, var1, var2, hue)
    
              
    for hue in non_numeric_df:
        print(f"\nCreating pairplot with hue={hue}") 
        #create_pairplot(df, hue)



    plt.close()
    #create_heatmap(df)







    # plot histogram for a given variable for each species
    # group by species
    #sepal_length_by_species = df.groupby('species')['sepal_length']

    # specify the species to plot
    #species = 'setosa'

    # get the data for the specified species
    #species_to_plot = sepal_length_by_species.get_group(species)
    #plt.hist(species_to_plot, edgecolor='black')
    # decorate plot
    #plt.xlabel('sepal length')
    #plt.ylabel('Frequency')
    #plt.title(f'Histogram of sepal length - {species}')
    #plt.show()


    ### MORE HISTOGRAMS




    ###



    # loop through species and variables and plot histograms
    # get unique species values
    unique_species = df['species'].unique()
    #print(f"Unique species: {unique_species}")

    for var in numeric_df:
        #print(var)
        #var_by_species = df.groupby('species')[var]
        # print each unique species
        for species in unique_species:
            #print(f"\nPlotting histograms for {var} by {species}")
            var_by_species = df.groupby('species')[var]
            species_to_plot = var_by_species.get_group(species)
            #plot_hist_by_species(species_to_plot, var, species)


            

    ####






    # end
    print(f"\nAnalysis complete.")


'''
References:

[1] https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

[2] https://www.w3schools.com/python/ref_os_makedirs.asp

[3] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

[4] Pairplot plots "pairwise relationships in a dataset." 
https://seaborn.pydata.org/generated/seaborn.pairplot.html

[a] https://seaborn.pydata.org/generated/seaborn.heatmap.html

'''
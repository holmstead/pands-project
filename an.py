# this module contains fucntions used in analysis.py

import pandas as pd                 # for data analyis
import matplotlib.pyplot as plt     # for plotting
import os                           # checking if directory exists
import seaborn as sns               # more plotting
import sys
import numpy as np                  # for line of best fit on scatterplot 


def plot_pivot(df, index):
    # create a pivot table, with given arguement (species) as index
    # then get the mean for each variable grouped by species
    pivot_table_df = pd.pivot_table(df, index=index, aggfunc="mean")

    # have a look at the pivot table
    #print(pivot_table_df)

    # determine std deviation for variables grouped by each species
    # for error bars
    std_dev = df.groupby("species").std()

    # set up the canvas
    # (N, n) sets how many subplots: (N row, n columns, figuresize)
    fig, ax = plt.subplots(1, 1, figsize=(5, 5))

    # plot barchart of the new df 
    pivot_table_df.plot(kind="bar", yerr=std_dev,capsize=4, ylabel="Mean (cm)", rot=0, ax=ax)

    # save plot as png
    ax.get_figure().savefig(f"plots/pivot_barchart.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_hist_entire_df(df):
    # set up the canvas
    # (N, n) sets how many subplots: (N row, n columns, figuresize)
    # testing how to adjust figure size for nice readme.md
    fig, ax = plt.subplots(1, 1, figsize=(5, 5)) 

    # plot histogram using pandas built in hist()
    df.hist(bins=10, ax=ax) 
    # df.plot.hist() puts them all on one figure, its a mess
    # https://stackoverflow.com/questions/57008086/df-hist-vs-df-plot-hist
    # "They do different things, df.hist() will produce a separate plot for each Series whilst df.plot.hist() will produce a stacked single plot"
    # ax = df.hist() doesnt work for some reason

    # save plot as png
    ax.get_figure().savefig(f"plots/df_hist.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_hist(df, var):
    # plot hist using matplotlib

    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # matplotlibs hist function takes a Series as an arg
    ax.hist(df[var], bins=10, edgecolor="black")

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {var}, species=all")

    # save plot as png
    ax.get_figure().savefig(f"plots/{var}_hist.png")
    #plt.show()
    plt.close()


def plot_hist_by_species(df, var, species):
    # plot histogram for a given variable for each species 
    # group by species
    attribute_by_species = df.groupby("species")[var]

    # get the data for the specified species
    species_to_plot = attribute_by_species.get_group(species)

    # set up canvas
    fig, ax = plt.subplots(1, 1) 

    # plot the histogram using matplotlib
    ax.hist(species_to_plot, bins=10, rwidth=1, edgecolor='black')

    # decorate plot
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {var} - {species}')

    # save plot as png
    ax.get_figure().savefig(f"plots/{var}_{species}_hist.png")
    #plt.show()
    plt.close()


def plot_pands_hist_by_species(df, var):
    # plot histograms of each attriubte, colored by species
    print(f"\nPlotting histograms grouping by {var} using pandas.")
    
    # set up the canvas
    fig, ax = plt.subplots(1, 1)

    # group by species using groupby() method, and filter by 'variable'
    group = df.groupby("species")[var]

    # plot the group
    group.hist(bins=10, alpha=0.5, ax=ax)
    # note: earlier it was df.hist(), now its group.hist()

    # decorate plot
    ax.set_xlabel(var)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {var} by species")

    # add legend
    # when you use groupby() it auto creates keys which can be used in the legend
    ax.legend(group.groups.keys())
    
    # save png
    ax.get_figure().savefig(f"plots/{var}_grouped_by_species_hist.png")

    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_kde(df):
    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # specify variable to plot on x axis, and hue
    sns.kdeplot(data=df, fill=True, ax=ax)

    # save plot as png
    ax.get_figure().savefig(f"plots/df_kde.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_kde_by_species(df, var):
    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # specify variable to plot on x axis, and hue
    sns.kdeplot(data=df, x=var, hue="species", fill=True, ax=ax)

    # save plot as png
    ax.get_figure().savefig(f"plots/kde_{var}_species_seaborn.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_scatter(df, var1, var2, groups):
    # set up the canvas (N rows, n columns)
    fig, ax = plt.subplots(1, 1) 

    colors = ["red", "blue", "green"]
    for i, species in enumerate(groups):

        # create a new df from filtering
        species_df = df[df['species'] == species]

        # assign variables from dataframe
        x = species_df[var1]
        y = species_df[var2]

        # plot using matplotlibs scatter() method
        ax.scatter(x, y, alpha=0.6, color=colors[i])#, label=species)

        # determine line of best fit using polyfit()
        # https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
        # https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
        m, c = np.polyfit(x, y, 1)

        # add line of best fit to plot
        # use y=mx+c 
        ax.plot(x, m*x+c, color=colors[i], label=f"{species}; y = {m:.2f}x + {c:.2f}")
        

    # decorate the plot
    ax.set_xlabel(var1)
    ax.set_ylabel(var2)
    
    # add grid to plot
    ax.grid(True)
    
    # add legend
    ax.legend()

    # save plot as png
    ax.get_figure().savefig(f"plots/{var1}_vs_{var2}_scatter.png")
    #plt.show()
    plt.close()


def plot_heatmap_by_species(df, species):
    # set up canvas
    fig, ax = plt.subplots(1, 1) 
    
    # filter the DataFrame by the current species
    species_df = df[df['species'] == species]

    # Ensure the filtered DataFrame contains numeric columns for correlation calculation
    numeric_species_df = species_df.select_dtypes(include='number')

     # calculate the correlation matrix
    corr = numeric_species_df.corr()
    
    # plot the heatmap using seaborn
    sns.heatmap(corr, annot=True)

    # save the plot as png
    plt.savefig(f"plots/{species}_heatmap.png")

    plt.show()
    plt.close()


def plot_pairplot(df, hue):
    # plot a grid of scatter plots using seaborn [4]
    # https://seaborn.pydata.org/generated/seaborn.pairplot.html
    print(f"\nCreating pairplot using {hue} as hue")

    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # create the pairplot using seaborn
    sns.pairplot(df, hue=hue)

    # save the plot as png
    plt.savefig(f"plots/pairplot_by_{hue}.png")

    #plt.show()
    plt.close()


def plot_hist_subplots(df, numeric_headers_list):
    # create a loop to plot a histogram of every numeric variable 
    # using pandas built in hist() method and PLOT ALL ON ONE FIGURE
    # set up the canvas BEFORE the for loop
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(2, 2)


    # now start the loop
    # add enumerate feature so we number each variable as we iterate through 1-4
    # flatten the subplots to iterate over them in the loop
    # https://www.tutorialspoint.com/what-does-axes-flat-in-matplotlib-do
    for i, ax in enumerate(ax.flat):
        # plot a histogram of the specified variable in the df
        #print(f"\nPlotting histogram of {variable} using pandas")
        # create a hist from a given column in the df using df["sepal_length"] for example
        df[numeric_headers_list[i]].plot.hist(bins=30, color="green", edgecolor="black", ax=ax)

        # decorate the plot
        ax.set_xlabel("Value")
        ax.set_ylabel("Frequency")
        ax.set_title(f"Histogram of {numeric_headers_list[i]}")

        # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
        # Hide x labels and tick labels for top plots and y ticks for right plots.
        ax.label_outer() # straight from matplotlib



    # auto adjust layout before saving
    plt.tight_layout()
    # save plot as png
    plt.savefig(f"plots/combined_histogram_of_variables_using_pandas.png")

    # display the whole figure
    plt.show()
    # close figures
    plt.close()
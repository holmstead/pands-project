# fucntions used in analysis.py

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

    # have a look 
    print(pivot_table_df)

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
    ax.get_figure().savefig(f"plots/df.hist.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


def plot_hist(df, var):
    # plot hist using matplotlib

    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # matplotlibs hist function takes a Series as an arg
    ax.hist(df[var], bins=20, edgecolor="black")

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {var}, species=all")

    # save plot as png
    ax.get_figure().savefig(f"plots/histogram_of_{var}_species=all_using_matplotlib.png")

    # display the whole figure
    #plt.show()
    # close figures
    plt.close()


def plot_hist_by_species(df, var, species):
    # plot histogram for a given variable for each species 
    # group by species
    attribute_by_species = df.groupby("species")[var]

    # get the data for the specified species
    species_to_plot = attribute_by_species.get_group(species)

    # set up canvas
    fig, ax = plt.subplots(1, 1) 

    ax.hist(species_to_plot, bins=10, rwidth=1, edgecolor='black')
    # decorate plot
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {var} - {species}')

    # save plot as png
    ax.get_figure().savefig(f"plots/histogram_of_{var}_by_species_using_matplotlib.png")

    plt.show()
    plt.close()
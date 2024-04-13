# author MHolmes

import pandas as pd                 # for data analyis
import matplotlib.pyplot as plt     # for plotting
import os                           # checking if directory exists
import seaborn as sns               # more plotting
import sys
import numpy as np                  # for line of best fit on scatterplot 



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


#################################################################################

# load local csv into a pandas dataframe [1]
df = pd.read_csv(sys.argv[1])

# print head and tail of the dataframe
print(f"\nDataframe head and tail:\n {df}")

# view datatypes
print(df.dtypes) 

# view headers
print(f"\nAll headers: {df.columns.tolist()}")


# create numeric only df
numeric_df = df.select_dtypes(include="number")
#print(numeric_df)
# make a list from numeric_columns variable
numeric_headers_list = numeric_df.columns.tolist()
print(f"\nNumeric column headers: {numeric_headers_list}")


# create df from non-numeric dtypes and make list of headers
non_numeric_df = df.select_dtypes(exclude="number")
non_numeric_headers_list = non_numeric_df.columns.tolist()
print(f"\nNon-numeric column headers: {non_numeric_headers_list}")


# write statistical summary to textfile using df.describe()
# create and open text file
with open("variables_summary.txt", "w") as f:
    # write to text file
    # convert to string first, cant write <class 'pandas.core.frame.DataFrame'> straight to file
    print(f"\n{type(numeric_df.describe())} \n")
    f.write(str(numeric_df.describe()) + '\n')


#######################################################################


## PLOTTING ##


# create a directory for plots if it doenst exist:
os.makedirs("plots", exist_ok=True)


## HISTOGRAMS 

# https://realpython.com/python-histograms/


# plot the entire dataframe using pandas built in hist() method

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

#############################################################


# create loop to cycle through variables and plot hist using matplotlib

# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html

for var in numeric_headers_list:
    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1) 

    # matplotlibs hist function takes the df as an arg
    ax.hist(df[var], bins=10, edgecolor="black")

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

#############################################################


# plot histogram for a given variable for each species

for var in numeric_headers_list:
    
    # group by species
    attribute_by_species = df.groupby('species')[var]

    # specify the species to plot
    species = 'setosa'

    # get the data for the specified species
    species_to_plot = attribute_by_species.get_group(species)

    # set up canvas
    fig, ax = plt.subplots(1, 1) 

    ax.hist(species_to_plot, edgecolor='black')
    # decorate plot
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Histogram of {var} - {species}')

    # save plot as png
    ax.get_figure().savefig(f"plots/histogram_of_{var}_by_species_using_matplotlib.png")

    #plt.show()
    plt.close()

#############################################################


# plot histograms of a Series for each unique species

# get unique species values and put in a list
unique_species_list = df['species'].unique()
print(f"Unique species list: {unique_species_list}")

# start outer for loop
for var in numeric_headers_list:
    
    # inner loop through species in unique species list
    for species in unique_species_list:
        #print(f"\nPlotting histograms for {var} by {species}")
        var_by_species = df.groupby('species')[var]
        
        # get the data for the specified species
        species_to_plot = var_by_species.get_group(species)

        # set up canvas
        fig, ax = plt.subplots(1, 1) 

        ax.hist(species_to_plot, edgecolor='black')
        # decorate plot
        ax.set_xlabel('Value')
        ax.set_ylabel('Frequency')
        ax.set_title(f'Histogram of {var} - {species}')

        # save plot as png
        ax.get_figure().savefig(f"plots/histogram_of_{var}_species={species}_using_matplotlib.png")

        plt.show()
        plt.close()



#############################################################


# create a loop to plot a histogram of every numeric column 
# using pandas built in hist() method.
for variable in numeric_headers_list:
    # plot a histogram of the specified variable in the df
    print(f"\nPlotting histogram of {variable} using pandas")

    # set up the canvas
    # (N, n) sets how many subplots: N row, n columns
    fig, ax = plt.subplots(1, 1)

    # create a hist from a given column in the df using df["sepal_length"] for example
    df[variable].plot.hist(bins=30, color="green", edgecolor="black", ax=ax)

    # decorate the plot
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {variable}")

    # save plot as png
    ax.get_figure().savefig(f"plots/histogram_of_{variable}_using_pandas.png")
    # display the whole figure
    #plt.show()
    # close figures
    plt.close()

    # need to figure out how to put those 4 histograms onto one figure
    # https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    # using ax=ax[0], ax[1] or something

###############################################################


# create a loop to plot a histogram of every numeric column 
# using pandas built in hist() method and PLOT ALL ON ONE FIGURE
# set up the canvas BEFORE the for loop
# (N, n) sets how many subplots: N row, n columns
fig, ax = plt.subplots(2, 2)
# have to flatten 2x2 to 1x4 so we can iterate over it 
ax = ax.flatten()
# now start the loop
# add enumerate feature so we number each variable as we iterate through 1-4
# use i for assigning axes number e.g. ax=ax[2]
for i, variable in enumerate(numeric_headers_list):
    # plot a histogram of the specified variable in the df
    #print(f"\nPlotting histogram of {variable} using pandas")
    # create a hist from a given column in the df using df["sepal_length"] for example
    df[variable].plot.hist(bins=30, color="green", edgecolor="black", ax=ax[i])

    # decorate the plot
    ax[i].set_xlabel("Value")
    ax[i].set_ylabel("Frequency")
    ax[i].set_title(f"Histogram of {variable}")

# auto adjust layout before saving
plt.tight_layout()
# save plot as png
plt.savefig(f"plots/combined_histogram_of_variables_using_pandas.png")

# display the whole figure
#plt.show()
# close figures
plt.close()

########################################################


# create histograms grouped by species using pandas hist() and groupby()
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html

for variable in numeric_headers_list:
    print(f"\nPlotting histograms grouping by {variable} using pandas.")
    
    # set up the canvas
    fig, ax = plt.subplots(1, 1)

    # group by species using groupby() method, and filter by 'variable'
    group = df.groupby("species")[variable]

    # plot the group
    group.hist(bins=10, alpha=0.5, ax=ax)
    # note: earlier it was df.hist(), now its group.hist()

    # decorate plot
    ax.set_xlabel(variable)
    ax.set_ylabel("Frequency")
    ax.set_title(f"Histogram of {variable} by species")

    # add legend
    # when you use groupby() it auto creates keys which can be used in the legend
    ax.legend(group.groups.keys())
    
    # save png
    ax.get_figure().savefig(f"plots/histogram_of_{variable}_grouped_by_species.png")

    plt.tight_layout()
    #plt.show()
    plt.close()

########################################################


# create histograms grouped by species using pandas hist() and groupby()
# and plot all 4 on one figure
# set up canvas
fig, ax = plt.subplots(2, 2, figsize=(12,10))
# flatten
ax = ax.flatten()
for i, variable in enumerate(numeric_headers_list):
    print(f"\nPlotting histograms grouping by {variable} using pandas.")
    
    # group by species using groupby() method, and filter by 'variable'
    group = df.groupby("species")[variable]

    # plot the group
    group.hist(bins=10, alpha=0.5, ax=ax[i])

    # decorate plot
    ax[i].set_xlabel(variable)
    ax[i].set_ylabel("Frequency")
    ax[i].set_title(f"Histogram of {variable} by species")

    # add legend
    # when you use groupby() it auto creates keys which can be used in the legend
    #ax.legend(group.groups.keys())

# specify where legend is using loc and bbox_to_anchor()
# https://matplotlib.org/stable/users/explain/axes/legend_guide.html
plt.legend(group.groups.keys(), loc="upper left", bbox_to_anchor=(1, 1))   
plt.tight_layout()
# save png
plt.savefig(f"plots/combined_hist_of_variables_grouped_by_species.png", bbox_inches="tight")
#plt.show()
plt.close()


#####################################################################


## KERNEL DENSITY ESTIMATION (KDE) PLOTS 


# what are kernel density plots:
# https://en.wikipedia.org/wiki/Kernel_density_estimation

# plot KDE using pandas
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.kde.html

# not yet


# plot KDE using seaborn
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html

# set up the canvas
fig, ax = plt.subplots(1, 1) 

# pass the pandas dataframe in to seaborn
sns.kdeplot(data=df, fill=True, ax=ax)

# save plot as png
ax.get_figure().savefig(f"plots/kde_seaborn.png")
plt.tight_layout()
#plt.show()
plt.close()


# plot KDE using seaborn but using species as hue
# loop through variables on x-axis
for var in numeric_headers_list:
    
    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # specify variable to plot on x axis, and hue
    sns.kdeplot(data=df, x=var, hue="species", fill=True, ax=ax)

    # save plot as png
    ax.get_figure().savefig(f"plots/kde_{var}_species_seaborn.png")
    plt.tight_layout()
    #plt.show()
    plt.close()


###############################################################################


## SCATTERPLOTS


# nested loop through variables to get two variables for scatter
for var1 in numeric_headers_list:
    for var2 in numeric_headers_list:
        # check if variable names match from both loops
        if var1 == var2:
            print(f"\nNot plotting {var1} against {var2}")
            #skip this loop in the for loop if the two variable names match
            continue
        print(f"\nScatter plotting {var1} v {var2} using matplotlib")
        # if they dont match, then they get plotted against each other
        # define functions

        # set up the canvas to have subplots
        # (N, n) sets how many subplots: N row, n columns
        fig, ax = plt.subplots(1, 1) 

        # assign variables from dataframe
        x = df[var1]
        y = df[var2]

        # plot using matplotlibs scatter() method
        ax.scatter(x, y)
        # ax.plot(x, y) creates a big line instead of points

        # determine line of best fit using polyfit()
        # https://numpy.org/doc/stable/reference/generated/numpy.polyfit.html
        # https://stackoverflow.com/questions/19068862/how-to-overplot-a-line-on-a-scatter-plot-in-python
        m, c = np.polyfit(x, y, 1)

        # add line of best fit to plot
        # use y=mx+c 
        ax.plot(x, m*x+c)

        # decorate the plot
        ax.set_xlabel(var1)
        ax.set_ylabel(var2)
        #ax.set_title("Iris Dataset")

        # save plot as png
        ax.get_figure().savefig(f"plots/{var1}_vs_{var2}_scatter.png")

        # display the whole figure
        #plt.show()
        # close figures
        plt.close()


###########################################################

# scatterplots using seaborns lmplot() method

# https://seaborn.pydata.org/generated/seaborn.lmplot.html

for var1 in numeric_headers_list:
    for var2 in numeric_headers_list:
        # check if variable names match from both loops
        if var1 == var2:
            #skip this loop in the for loop if the two variable names match
            continue
        
        for hue in non_numeric_headers_list:
            print(f"\nPlotting lmplot of {var1} v {var2} with hue={hue}")
            # lmplot() using seaborn

            # assign variables
            x = df[var1]
            y = df[var2]

            # scatter plot using lmplot()
            sns.lmplot(data=df, x=var1, y=var2, hue=hue)

            # save plot as png
            plt.savefig(f"plots/{var1}_vs_{var2}_lmplot_{hue}.png")
            #ax.get_figure().savefig(f"plots/{var1} vs {var2}_lmplot_{hue}.png")
            # display the whole figure
            #plt.show()

            # close figures
            plt.close()

###########################################################
   

# pairplots using seaborns pairplot() method

# https://seaborn.pydata.org/generated/seaborn.pairplot.html

for hue in non_numeric_headers_list: 
    # plot a grid of scatter plots using seaborn [4]
    print(f"\nCreating pairplot using {hue} as hue")

    # set up the canvas
    fig, ax = plt.subplots(1, 1) 

    # create the pairplot using seaborn
    sns.pairplot(df, hue=hue)

    # save the plot as png
    plt.savefig(f"plots/pairplot_by_{hue}.png")

    #plt.show()
    plt.close()

#########################################################


# create a heatmap using seaborn

# https://seaborn.pydata.org/generated/seaborn.heatmap.html

# set up canvas
fig, ax = plt.subplots(1, 1) 

# plot the heatmap using seaborn
sns.heatmap(df.corr(numeric_only=True), annot=True)

# save the plot as png
plt.savefig(f"plots/heatmap.png")

#plt.show()
plt.close()

########################################################


## END
print(f"\nAnalysis complete.")


'''
References:

[1] https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

[2] https://www.w3schools.com/python/ref_os_makedirs.asp

[3] https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html

[4] Pairplot plots "pairwise relationships in a dataset." 
https://seaborn.pydata.org/generated/seaborn.pairplot.html

[a] 

'''
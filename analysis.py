'''
This program reads in a dataset (csv) and summarizes numerical variables, 
plots histograms, scatterplots, etc.
'''

import pandas as pd                 # for data analyis
import matplotlib.pyplot as plt     # for plotting
import os                           # checking if directory exists
import seaborn as sns               # more plotting
import sys                          # ends program if not enough args given
#import numpy as np                  # for line of best fit on scatterplot 
import an                           # import custom module


# check if two arguments given
if len(sys.argv) != 2:
    print("Usage: python analysis.py <filename>\nExiting.")
    # kill the program if we didnt get 2 args
    sys.exit(1)
# handle file not found exception
else:
    try:
        with open(sys.argv[1], "r"):
            # file found ok so pass 
            pass
    except FileNotFoundError:
        print("File not found.\nExiting.", end="\n")
        sys.exit(1)


# load specified csv into a pandas dataframe [1]
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

# make a list from numeric_df variables
numeric_headers_list = numeric_df.columns.tolist()
print(f"\nNumeric column headers: {numeric_headers_list}")


# create df from non-numeric dtypes and make list of headers
non_numeric_df = df.select_dtypes(exclude="number")
non_numeric_headers_list = non_numeric_df.columns.tolist()
print(f"\nNon-numeric column headers: {non_numeric_headers_list}")


# get unique species values and put in a list
unique_species_list = df["species"].unique()
print(f"Unique species list: {unique_species_list}")


# write statistical summary to textfile using df.describe()
# create and open text file
with open("variables_summary.txt", "w") as f:
    # write to text file
    # convert to string first, cant write <class 'pandas.core.frame.DataFrame'> straight to file
    print(f"\n{type(numeric_df.describe())} \n")
    f.write(str(numeric_df.describe()) + '\n')


## PLOTTING

# create a directory for plots if it doesn't already exist:
os.makedirs("plots", exist_ok=True)


## BARCHARTS

# call function to create barchart from a pivot table, with species as index
an.plot_pivot(df, "species")


## HISTOGRAMS & KDE PLOTS

# https://realpython.com/python-histograms/

# what are kernel density plots:
# https://en.wikipedia.org/wiki/Kernel_density_estimation

# plot the entire dataframe using pandas built in hist() method
an.plot_hist_entire_df(df)

# plot KDE of entire df using seaborn
# https://seaborn.pydata.org/generated/seaborn.kdeplot.html
an.plot_kde(df)


# create loop to cycle through variables and plot histograms 
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html
for var in numeric_headers_list:
    # plot a histogram of each variable using matplotlib
    an.plot_hist(df, var)
    
    # create histograms grouped by species using pandas hist() and groupby()
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html
    an.plot_pands_hist_by_species(df, var)

    # plot KDE using seaborn but using species as hue
    an.plot_kde_by_species(df, var)

    
    # inner loop through species in unique species list
    for species in unique_species_list:
        # plot histograms of a Series for each unique species
        an.plot_hist_by_species(df, var, species)


# need to figure out how to put those 4 histograms onto one figure
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
# using ax=ax[0], ax[1] or something


# plot a histogram of every numeric variable 
# using pandas built in hist() method and PLOT ALL ON ONE FIGURE
an.plot_hist_subplots(df, numeric_headers_list)


########################################################


# create histograms grouped by species using pandas hist() and groupby()
# and plot all 4 on one figure
# set up canvas
fig, ax = plt.subplots(2, 2, figsize=(12,10))
# have to flatten 2x2 to 1x4 so we can iterate over it 
# https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html
#ax = ax.flatten()
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
    ax[i].set_title(f"Histogram of {variable}")

# specify where legend is using loc and bbox_to_anchor()
# https://matplotlib.org/stable/users/explain/axes/legend_guide.html
plt.legend(group.groups.keys(), loc="upper left", bbox_to_anchor=(1, 1))   
plt.tight_layout()
# save png
plt.savefig(f"plots/combined_hist_of_variables_grouped_by_species.png", bbox_inches="tight")
#plt.show()
plt.close()




###############################################################################


## SCATTERPLOTS

# scatterplot using matplotlib but with color by species
# with line of best fit and equation in legend

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

        # create scatter plot
        an.plot_scatter(df, var1, var2, groups=unique_species_list)

###########################################################
   

# pairplots using seaborns pairplot() method
for hue in non_numeric_headers_list: 
    an.plot_pairplot(df, hue)

#########################################################

# loop through species in unique species list
for species in unique_species_list:
    # plot heatmap for each species
    # https://seaborn.pydata.org/generated/seaborn.heatmap.html
    an.plot_heatmap_by_species(df, species)



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
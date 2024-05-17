'''
This program reads in the iris dataset (csv) and summarizes numerical variables, 
plots histograms, scatterplots, etc.
'''

import pandas as pd                 # for data analyis
import os                           # checking if directory exists
import sys                          # taking arguements from commadn line 
import an                           # import custom module


# check if two arguments given
if len(sys.argv) != 2:
    # kill the program if we didnt get 2 args
    raise SystemExit("Usage: python analysis.py <filename>\nExiting.")
# handle file not found exception
else:
    try:
        with open(sys.argv[1], "r"):
            # file found ok so pass 
            pass
    except FileNotFoundError:
        raise SystemExit("File not found.\nExiting.")


# load specified csv into a pandas dataframe
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
numeric_variables_list = numeric_df.columns.tolist()
print(f"\nNumeric column headers: {numeric_variables_list}")


# create df from non-numeric dtypes and make list of headers
non_numeric_df = df.select_dtypes(exclude="number")
categorical_variables_list = non_numeric_df.columns.tolist()
print(f"\nNon-numeric column headers: {categorical_variables_list}")


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
print(f"\nCreating barcharts ...")
# call function to create barchart from a pivot table, with species as index
an.plot_pivot(df, "species")


## HISTOGRAMS & KDE PLOTS
print(f"\nCreating histograms and KDE plots ...")
# plot the entire dataframe using pandas built in hist() method
an.plot_hist_entire_df(df)

# plot KDE of entire df using seaborn
an.plot_kde(df)

# create loop to cycle through variables and plot histograms 
for var in numeric_variables_list:
    # plot a histogram of each variable using matplotlib
    an.plot_hist(df, var)
    
    # create histograms grouped by species using pandas hist() and groupby()
    an.plot_pands_hist_by_species(df, var)

    # plot KDE using seaborn but using species as hue
    an.plot_kde_by_species(df, var)

    
    # inner loop through species in unique species list
    for species in unique_species_list:
        # plot histograms of a Series for each unique species
        an.plot_hist_by_species(df, var, species)

        # plot combined histogram and kde on one fig
        an.plot_displot(df, var, species)


# plot a histogram of every numeric variable 
# using pandas built in hist() method and PLOT ALL ON ONE FIGURE
an.plot_hist_subplots(df, numeric_variables_list)


# create histograms grouped by species using pandas hist() and groupby()
# and plot all 4 on one figure
an.plot_grouped_hist_subplots(df, numeric_variables_list)


# SCATTERPLOTS
print(f"\nScatter plotting ...")
# nested loop through variables to get two variables for scatter
for var1 in numeric_variables_list:
    for var2 in numeric_variables_list:
        # check if variable names match from both loops
        if var1 == var2:
            #skip this loop in the for loop if the two variable names match
            continue
        
        # if they dont match, then they get plotted against each other
        # create scatter plot using matplotlib, coloured by species
        an.plot_scatter(df, var1, var2, groups=unique_species_list)


# PAIRPLOT
print(f"\nCreating pairplots ...")
# create pairplot using seaborns pairplot() method
for hue in categorical_variables_list: 
    an.plot_pairplot(df, hue)


# HEATMAPS
print(f"\nCreating heatmaps ...")
# plot heatmap for all species
an.plot_heatmap(df)

# loop through species in unique species list
for species in unique_species_list:
    # plot heatmap for each individual species
    an.plot_heatmap_by_species(df, species)


# END
print(f"\nAnalysis complete.")
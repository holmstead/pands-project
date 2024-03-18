# author MHolmes

import pandas as pd
import matplotlib.pyplot as plt
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

# creat and open textfile
with open("variables_summary.txt", "w") as f:
    # write to textfile
    f.write("test")

def plot_hist(variable):
    '''
    This function plots a histogram from a given variable
    in a pandas dataframe
    '''
    # plot a histogram of the specified variable in the df
    #hist = df.plot.hist(column=["sepal_length"], edgecolor='black')
    plt.hist(df[variable], edgecolor="black")

    # decorate the plot
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.title(f"Histogram of {variable}")

    # save plot as png
    plt.savefig(f"Histogram of {variable}.png")

    # display the plot
    plt.show()

plot_hist("sepal_length")




# now a scatterplot
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
x = df.sepal_length
y = df.sepal_width
plt.scatter(x, y)

# decorate the plot
plt.xlabel("sepal_length")
plt.ylabel("sepal_width")
#plt.title('Scatterplot of ... ')

# save plot as png
plt.savefig("scatter.png")

# display the plot
plt.show()
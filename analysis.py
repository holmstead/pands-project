# author MHolmes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

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
with open('variables_summary.txt', 'w') as f:
    # write to textfile
    f.write('test')

# plot a histogram of the array
hist = df.plot.hist(column=["sepal_length"], edgecolor='black')
plt.show()
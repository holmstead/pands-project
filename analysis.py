# author MHolmes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

# load local csv into a pandas dataframe
df = pd.read_csv("iris.csv")

# print head and tail of the dataframe
print(df) 

# view datatypes
print(df.dtypes) 


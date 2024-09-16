import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

featuresData_df = pd.read_csv('data/Features data set.csv')
salesData_df = pd.read_csv('data/sales data-set.csv')
storesData_df = pd.read_csv('data/stores data-set.csv')

# Get the top 5 entries for each DataFrame
top5_df1 = featuresData_df.head(5)
top5_df2 = salesData_df.head(5)
top5_df3 = storesData_df.head(5)

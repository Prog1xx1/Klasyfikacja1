import pandas as pd
import numpy as np

df = pd.read_csv("FC.csv", sep=',')
print(df.head())
print(df.info())
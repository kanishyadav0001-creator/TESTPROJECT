import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Bestsellers with categories.csv')
print(data.head(5))

print(data.isnull().sum())


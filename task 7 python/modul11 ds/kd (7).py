import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 

df = pd.read_csv("datatitanic.csv")
df.drop("cabin", axis=1, inplace=True)
df.head(5)
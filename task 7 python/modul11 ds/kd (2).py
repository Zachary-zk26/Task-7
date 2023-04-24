import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 

df = pd.read_csv("datatitanic.csv")
plt.scatter(df.Age, df.Survived, color='red', marker='o')

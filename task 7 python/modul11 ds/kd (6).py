import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 

df = pd.read_csv("datatitanic.csv")
sb.heatmap(f.isnull())
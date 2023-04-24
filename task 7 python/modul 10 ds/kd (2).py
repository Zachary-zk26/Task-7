import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 

df = pd.read_csv("dataasuransi.csv")
sb.regplot(x='umur', t='membeli_asuransi', data=df, logistic=True, color='red')

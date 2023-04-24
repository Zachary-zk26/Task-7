import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LogisticRegression

df = pd.read_csv("dataasuransi.csv")
x_train, x_test, y_train, y_test = train_test_split(df[['umur']], df.membeli_asuransi,
train_size=0.9)
model = LogisticRegression()
model.score(x_test)
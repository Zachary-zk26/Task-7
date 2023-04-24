import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import LogisticRegression

df = pd.read_csv("dataasuransi.csv")
model = LogisticRegression()
model.fit(x_train, y_train)
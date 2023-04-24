import pandas as pd 
from matplotlib import pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import train_test_split

df = pd.read_csv("datatitanic.csv")
x_train, x_test, y_train, y_test = train_test_split(df[['Age']], df.Survived, train_size=0.9)
x_test

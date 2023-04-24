import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sb 
from sklearn.model_selection import train_test_split
from sklearn.model_selection import LogisticRegression
import math
import warnings
warnings.filterwarnings('ignore')

data = 'CarPrice_Assignment.csv'
dataset = pd.read_csv(data)

x = dataset['enginesize'].values.reshape(-1,1)
y = dataset['price'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x,y, train_size = 0.8,
test_size= 0.2, random_state= 100)

regressor= LinearRegression()
regressor.fit(x_train,y_train)
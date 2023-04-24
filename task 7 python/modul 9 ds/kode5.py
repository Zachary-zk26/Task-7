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

plt.scatter(dataset['enginesize'], dataset['price'])
plt.xlabel('enginesize')
plt.ylabel('price')
plt.title('scatter plot enginesize vs price')
plt.show()
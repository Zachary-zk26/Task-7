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
def pp(x,y,z):
    sns.pairplot(dataset,s_vars[x,y,z], y_vars='price', size=4, aspect=1, kind='scatter')
    plt.show

pp('enginesize', 'boreratio', 'stroke')
pp('compressionratio', 'horsepower', 'peakrpm')
pp('wheelbase', 'citympg', 'highwaympg')


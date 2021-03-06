# %load q04_correlation_plot/build.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.switch_backend('agg')
import sys, os
from greyatomlib.german_credit.q03_encode_features.build import q03_encode_features
path = 'data/GermanData.csv'

def q04_correlation_plot(path):
    data = q03_encode_features(path)
    sns.pairplot(data[0])
    plt.show()
    





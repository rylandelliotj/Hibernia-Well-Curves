# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:01:56 2025

@author: werty
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

curves = pd.read_csv('Inputs\\arps_curves.csv')

test_well = curves['Well Name'].unique()[3]
test_data = curves[curves['Well Name'] == test_well]

plt.figure(figsize=(30,10))
sns.barplot(data=test_data, x='Cumulative Months', y='Oil (m3)')
sns.lineplot(data=test_data, x='Cumulative Months', y='Fitted Values', color='orange', linewidth=7)
plt.xticks(np.arange(0, test_data['Cumulative Months'].max(), 10))
plt.title(test_well, size=30)
plt.show()
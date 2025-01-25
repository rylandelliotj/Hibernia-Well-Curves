# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:00:32 2025

@author: werty
"""
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit

df = pd.read_csv("C:\\Users\\werty\\Desktop\\Portfolio\\Hibernia Decline Curves\\Inputs\\well_data.csv")
df.sort_values(['Well Name', 'Year', 'Month'], inplace=True)
df = df[['Well Name', 'Oil (m3)']]
df['Cumulative Months'] = df.groupby(['Well Name']).cumcount()


def arps(t, qi, b, Di):
    return qi * (1 + b * Di * t)**(-1/b)

def curves(well):
    y = well['Oil (m3)']
    x = well['Cumulative Months']
    max_y = y.max()
    
    # Use your initial guess for the model parameters
    initial_guess = [max_y, 1, 0.1]

    # Define upper and lower bounds
    bounds = ([-np.inf, 1, 0], [np.inf, 2, np.inf])
    
    # Fit curve
    parameters, covariance = curve_fit(arps, x, y, p0=initial_guess, bounds=bounds)
    
    # Create data of estimated y (avg_prod) at each x (T) given the model parameters
    ans = arps(x, parameters[0], parameters[1], parameters[2])
    
    return ans

results = df.groupby('Well Name').apply(curves).reset_index()
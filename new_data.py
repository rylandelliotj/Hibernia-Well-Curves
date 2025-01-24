# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 20:55:07 2025

@author: werty
"""

import camelot
import numpy as np
import pandas as pd

url = 'https://www.cnlopb.ca/wp-content/uploads/hibstats/hib_oil_{}.pdf'
first_table_year = 2016
last_table_year = 2024

def clean_table(table):
    columns = ['Well Name', 'Year', 'Month', 'Oil (m3)', 'Gas (e3m3)', 'Water (m3)']
    numerics = columns[1:]
    bad_words = ['Yearly Total:', 'Well Name', '[image]']
    table.columns = columns
    table = table.replace('', np.nan)
    table[['Well Name','Year']] = table[['Well Name','Year']].ffill()
    table = table[~table['Well Name'].isin(bad_words)]
    table = table[~table['Month'].astype(str).str.contains('Yearly')]
    table.dropna(inplace=True)
    table[numerics] = table[numerics].replace({',':''}, regex=True)
    table[numerics] = table[numerics].astype(float)
    table.sort_values(['Well Name', 'Year', 'Month'])
    
    return table

def concat_tables(tables):
    df = pd.concat(tables)
    df['Well Name'] = df['Well Name'].ffill()
    
    return df

def main(tables):
    cleaned_tables = [clean_table(x.df) for x in tables]
    concat_table = concat_tables(cleaned_tables)
    
    return concat_table

new_dfs = []
for year in range(first_table_year, last_table_year + 1):
    print(year)
    tables = camelot.read_pdf(url.format(year))
    df = main(tables)
    new_dfs.append(df)
    
final_new = pd.concat(new_dfs)

old_dfs = []
for year in range(1997, 2016):
    print(year)
    table = pd.read_excel("C:\\Users\\werty\\Desktop\\Portfolio\\Hibernia Decline Curves\\Inputs\\old_data.xlsx", sheet_name=str(year))
    df = clean_table(table)
    old_dfs.append(df)

final_old = pd.concat(old_dfs)

final_concat = pd.concat([final_old, final_new])
final_concat.to_csv("C:\\Users\\werty\\Desktop\\Portfolio\\Hibernia Decline Curves\\Inputs\\well_data.csv")
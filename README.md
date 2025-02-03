# Hibernia Well Curves
This project is aimed at using the ARPS equation to determine decline curves for Newfoundland's oldest offshore drilling rig: Hibernia

## Inputs
This is where you can find raw data used in the python scripts.
>old_data: data that is not easily scraped using the Camelot module in python, so I used PowerQuery editor to extract these data.
>well_data: old and new well data from cnlopb's website (https://www.cnlopb.ca/information/statistics/#rm)
>arps_curves: data used to create an arps curve for each well in the well_data file.

## data.py
This script collects and cleans data from the CNLOPB.
You will notice that it only takes data from 2016 and up.
This is because Camelot has a difficult time parsing out older data.
Pre-2016 data is easier to collect and clean through Power Query Editor in Excel.

## curve_fit.py
This applies ARPS curves to the well data using scipy's 'curve_fit' method.

## viz.py
A basic vizualization script for EDA

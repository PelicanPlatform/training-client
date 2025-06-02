#!/usr/bin/env python3

"""
Example script for analyzing temperature data for one station.
Takes valid station ID as the first argument.
"""
from sys import argv
import pandas as pd

from my_functions import extract_temp_data, identify_season, create_histogram

# Get station ID from argument
station_id = str(argv[1])

# Read data from file
station_data_filename = f"{station_id}.csv"
station_df = pd.read_csv(station_data_filename, low_memory=False)

# Extract Min, Max Temperatures as dataframe
tempdf = extract_temp_data(station_df)

# Describe the dataset
print(f"{tempdf.describe()}\n")

# Label by season
tempdf['SEASON'] = tempdf.index.map(identify_season)

# Create histograms
# Saves as <STATION ID>-temp-dist.png, unless otherwise specified.
create_histogram(tempdf, station_id)

import pandas as pd

station_URL='osdf:///aws-opendata/us-east-1/noaa-ghcn-pds/csv/by_station/USW00014837.csv'

station_df = pd.read_csv(station_URL, low_memory=False)
print(station_df.head())


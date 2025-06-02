"""
This module contains useful functions for analyzing the example temperature data.
"""

from datetime import date
from enum import Enum
from pandas import DataFrame
import matplotlib.pyplot as plt
from numpy import histogram

def convert_int_to_date(date_int: int) -> date:
    """
    Dataset uses dates in the format YYYYMMDD. 
    Turn into proper date.
    """
    date_str = str(date_int)
    year = int(date_str[0:4])
    month = int(date_str[4:6])
    day = int(date_str[6:8])

    return date(year, month, day)


def extract_temp_data(station_df: DataFrame, convert_to_fahrenheit=True) -> DataFrame:
    # Restructure dataframe
    # A. Put all of one day's observations in one row
    station_df = station_df.pivot(index='DATE', columns='ELEMENT', values='DATA_VALUE')
    # B. Set index as proper Date type
    station_df.index = station_df.index.map(convert_int_to_date)

    # Filter down to just temperature data (units are "tenths of degrees C")
    tempdf = station_df[['TMIN', 'TMAX']].dropna().astype(int)

    # Convert to regular degrees Celsius
    tempdf = tempdf / 10

    if convert_to_fahrenheit:
        # Convert to degrees Fahrenheit
        tempdf = tempdf.transform(lambda x: 32 + ((9 / 5) * x))

    return tempdf


class Season(Enum):
    WINTER = 0
    SPRING = 1
    SUMMER = 2
    FALL = 3


def identify_season(date_value: date, southern_hemisphere: bool = False) -> Season:
    """
    Identifies the ~meteorological season using the provided date.

    For the northern hemisphere, using
        Spring: Mar thru May  
        Summer: Jun thru Aug
        Fall:   Sep thru Nov
        Winter: Dec thru Feb

    Invert the seasons by setting `southern_hemisphere` to `True`.
    """
    if southern_hemisphere: 
        # There's probably a more elegant pythonic way of doing this..
        season_dict = {
            3: Season.FALL, 4: Season.FALL, 5: Season.FALL,
            6: Season.WINTER, 7: Season.WINTER, 8: Season.WINTER,
            9: Season.SPRING, 10: Season.SPRING, 11: Season.SPRING,
            12: Season.SUMMER, 1: Season.SUMMER, 2: Season.SUMMER,
        }
    else:
        season_dict = {
            3: Season.SPRING, 4: Season.SPRING, 5: Season.SPRING,
            6: Season.SUMMER, 7: Season.SUMMER, 8: Season.SUMMER,
            9: Season.FALL, 10: Season.FALL, 11: Season.FALL,
            12: Season.WINTER, 1: Season.WINTER, 2: Season.WINTER,
        }

    return season_dict[date_value.month]


def create_histogram(tempdf: DataFrame, station_id: str, filename: str = None):
    if filename is None:
        filename = f"{station_id}.png"

    # Overview of data
    n_days = len(tempdf)
    start_date = min(tempdf.index)
    end_date = max(tempdf.index)
    n_years = round((end_date - start_date).days / 365.25, ndigits=1)

    print(f"""
Plotting histograms of observations for {n_days:,} days, spanning {n_years} years 
from {start_date} to {end_date}, to '{filename}' .
""")

    # Histogram settings
    min_temp = -40  # Fahrenheit
    max_temp = 110  # Fahrenheit
    step_temp = 5   # Fahrenheit
    bins = range(min_temp, max_temp, step_temp)
    bin_pos = list(map(lambda x: x + (step_temp / 2), bins[:-1]))

    # Figure
    fig, axs = plt.subplots(4, figsize=(8,10))
    fig.suptitle(f"Distribution of Min, Max temperatures across the Seasons\nfor station {station_id} from {start_date} to {end_date}.\n")
    fig.supxlabel('Degrees F')
    fig.supylabel('Number of observations')
    fig.tight_layout()

    # Plotting mirror histograms for each season
    for season in Season:
        tmax_heights, tmax_bins = histogram(tempdf[tempdf['SEASON'] == season]['TMAX'], density=False, bins=bins)
        tmin_heights, tmin_bins = histogram(tempdf[tempdf['SEASON'] == season]['TMIN'], density=False, bins=bins)
        tmin_heights *= -1
        
        sub_axs = axs[season.value]

        sub_axs.bar(bin_pos, list(tmax_heights), width=step_temp, edgecolor='black', color='red')
        sub_axs.bar(bin_pos, list(tmin_heights), width=step_temp, edgecolor='black', color='blue')
        sub_axs.set_title(f"{season.name}")

    fig.savefig(filename)

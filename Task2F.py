"""
Plots the water levels, degree-4 polynomial fit and typical range over the past 2 days for the 5 stations at which the current relative water level is greatest.
"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)
    stations.sort(key = lambda x: x.latest_level or 0, reverse=True) # sorted list of stations, highest to lowest
    
    # prep vars for plotting call
    top_5 = []
    dates_combined = []
    levels_combined = []

    i = 0
    while len(top_5) < 5: 
        station = stations[i]
        dates, levels = fetch_measure_levels(
            station.measure_id,
            dt = datetime.timedelta(days=2)
        )

        if len(dates) > 0 and len(levels) > 0 and station.typical_range_consistent(): # if data is valid for plotting
            top_5.append(station) # add it to plotted stations
            dates_combined.append(dates)
            levels_combined.append(levels)

        i += 1

    plot_water_level_with_fit(top_5, dates_combined, levels_combined, 4)

if __name__ == '__main__':
    run()
"""
Plots the water levels and typical ranges over the past 10 days for the 5 stations at which the current relative water level is greatest.
"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    top_5 = stations_highest_rel_level(stations, 5)

    dates_combined = []
    levels_combined = []

    for station in top_5: 
        dates, levels = fetch_measure_levels(
            station.measure_id,
            dt = datetime.timedelta(days=2)
        )

        dates_combined.append(dates)
        levels_combined.append(levels)

    plot_water_levels(top_5, dates_combined, levels_combined)

if __name__ == '__main__':
    run()
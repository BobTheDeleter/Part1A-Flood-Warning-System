"""
Plots the water levels over the past 10 days for the 5 stations at which the current relative water level is greatest.
"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list
from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import update_water_levels

def run():
    stations = build_station_list()
    stations_valid = [station for station in stations if station.typical_range_consistent()]
    update_water_levels(stations_valid)
    stations_valid.sort(key = lambda x: x.latest_level or 0)
    top_5 = stations_valid[-5:-1]
    
    dates_combined = []
    levels_combined = []
    for station in top_5:
        dates, levels = fetch_measure_levels(
            station.measure_id,
            dt = datetime.timedelta(days=5)
        )
        dates_combined.append(dates)
        levels_combined.append(levels)

    plot_water_levels(top_5, dates_combined, levels_combined)

if __name__ == '__main__':
    run()
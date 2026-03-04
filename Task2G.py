#First, I am going to compare the relative levels to some current govt warnings
import datetime

from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import stations_over_relative_level, polyfit, will_exceed_relative_level_in_range
from floodsystem.datafetcher import fetch_measure_levels

def run():
    stations = build_station_list()
    update_water_levels(stations)

    DATA_RANGE_DAYS = 7

    LOW = 1.1
    MODERATE = 1.3
    SEVERE = 1.5
    FLOOD = 2.0

    MODERATE_FUTURE_WINDOW_DAYS = 10
    SEVERE_FUTURE_WINDOW_DAYS = 14

    stations_at_risk = stations_over_relative_level(stations, [FLOOD, SEVERE, MODERATE, LOW])

    currently_flooding_stations = stations_at_risk[0]
    print("Currently flooding:")
    for station in currently_flooding_stations:
        print(f" - {station.name}")
    
    print("Stations at severe risk:")
    for station in stations_at_risk[1]:
        print(f" - {station.name}")

    print("Stations at moderate risk:")
    for station in stations_at_risk[2]:
        print(f" - {station.name}")

    print("Stations at low risk:")
    for station in stations_at_risk[3]:
        print(f" - {station.name}")

    print("")

    severe_stations_predicted_to_flood = set()

    for station in stations_at_risk[1]: # check stations at severe risk, but not currently flooding
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=DATA_RANGE_DAYS))
        if len(dates) < 1 or len(levels) < 1:
            continue

        poly, offset = polyfit(dates, levels, 4)

        if will_exceed_relative_level_in_range(station, poly, offset, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=SEVERE_FUTURE_WINDOW_DAYS), FLOOD):
            severe_stations_predicted_to_flood.add(station)

    print(f"Towns at severe risk, predicted to flood in the next {SEVERE_FUTURE_WINDOW_DAYS} days:")

    severe_towns_predicted_to_flood = set(station.town for station in severe_stations_predicted_to_flood)
    for town in severe_towns_predicted_to_flood:
        print(f" - {town}")

    moderate_stations_predicted_to_flood = set()
    
    for station in stations_at_risk[2]: # check stations at moderate risk, but not currently flooding
        dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=DATA_RANGE_DAYS))
        if len(dates) < 1 or len(levels) < 1:
            continue

        poly, offset = polyfit(dates, levels, 4)

        if will_exceed_relative_level_in_range(station, poly, offset, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=MODERATE_FUTURE_WINDOW_DAYS), FLOOD):
            moderate_stations_predicted_to_flood.add(station)

    print(f"Towns at moderate risk, predicted to flood in the next {MODERATE_FUTURE_WINDOW_DAYS} days:")

    moderate_towns_predicted_to_flood = set(station.town for station in moderate_stations_predicted_to_flood)
    for town in moderate_towns_predicted_to_flood:
        print(f" - {town}")

    # Plot at tisk stations

    from plot_stations_on_map import plot_grouped_stations_on_map

    colors = ["green", "orange", "red"] # low to high to ensure that stations with higher risk are plotted on top of stations with lower risk
    sizes = [5, 10, 15]
    stations_to_plot = [moderate_stations_predicted_to_flood, severe_stations_predicted_to_flood, currently_flooding_stations]

    plot_grouped_stations_on_map(stations_to_plot, colors, sizes)

if __name__ == '__main__':
    print("*** Task 2G: CUED Part ID Flood Warning System ***")
    run()
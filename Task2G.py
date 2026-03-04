#First, I am going to compare the relative levels to some current govt warnings
import datetime

from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import stations_over_thresholds, polyfit, will_exceed_threshold_in_range
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

    stations_at_risk = stations_over_thresholds(stations, [FLOOD, SEVERE, MODERATE, LOW])

    currently_flooding_towns = stations_at_risk[0]
    print("Currently flooding:")
    for town in currently_flooding_towns:
        print(f" - {town.name}")
    
    print("Stations at severe risk:")
    for town in stations_at_risk[1]:
        print(f" - {town.name}")

    print("Stations at moderate risk:")
    for town in stations_at_risk[2]:
        print(f" - {town.name}")

    print("Stations at low risk:")
    for town in stations_at_risk[3]:
        print(f" - {town.name}")

    print("")

    severe_town_predicted_to_flood = set()

    for town in stations_at_risk[1]: # check stations at severe risk, but not currently flooding
        dates, levels = fetch_measure_levels(town.measure_id, dt=datetime.timedelta(days=DATA_RANGE_DAYS))
        if len(dates) < 1 or len(levels) < 1:
            continue

        poly, offset = polyfit(dates, levels, 4)

        if will_exceed_threshold_in_range(town, poly, offset, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=SEVERE_FUTURE_WINDOW_DAYS), FLOOD):
            severe_town_predicted_to_flood.add(town.town)
    print(f"Towns at severe risk, predicted to flood in the next {SEVERE_FUTURE_WINDOW_DAYS} days:")
    
    for town in severe_town_predicted_to_flood:
        print(f" - {town}")

    moderate_towns_predicted_to_flood = set()
    
    for town in stations_at_risk[2]: # check stations at moderate risk, but not currently flooding
        dates, levels = fetch_measure_levels(town.measure_id, dt=datetime.timedelta(days=DATA_RANGE_DAYS))
        if len(dates) < 1 or len(levels) < 1:
            continue

        poly, offset = polyfit(dates, levels, 4)

        if will_exceed_threshold_in_range(town, poly, offset, datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=MODERATE_FUTURE_WINDOW_DAYS), FLOOD):
            moderate_towns_predicted_to_flood.add(town.town)

    print(f"Towns at moderate risk, predicted to flood in the next {MODERATE_FUTURE_WINDOW_DAYS} days:")
    for town in moderate_towns_predicted_to_flood:
        print(f" - {town}")

if __name__ == '__main__':
    print("*** Task 2G: CUED Part ID Flood Warning System ***")
    run()
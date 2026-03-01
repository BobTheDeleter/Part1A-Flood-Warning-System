from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    #could implement a check for internet connection / timeout error
    stations = build_station_list()
    update_water_levels(stations)
    #print("Updated levels")
    at_risk_stations = stations_highest_rel_level(stations, 10)
    for station in at_risk_stations:
        print(station.name, station.relative_water_level())

if __name__ == "__main__":
    print("*** Task 2C: CUED Part ID Flood Warning System ***")
    run()
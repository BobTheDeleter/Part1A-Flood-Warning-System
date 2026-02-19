from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    print("Running")
    stations = build_station_list()
    update_water_levels(stations)
    print("Updated levels")
    stations_levels = stations_level_over_threshold(stations, 0.8)
    #print(stations_levels)
    for station_level_tuple in stations_levels:
        
        print(station_level_tuple[0].name, station_level_tuple[1])

if __name__ == "__main__":
    print("*** Task 2B: CUED Part ID Flood Warning System ***")
    run()
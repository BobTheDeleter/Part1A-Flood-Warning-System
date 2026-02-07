from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """
    Prints the 9 rivers with the most stations
    """
    stations = build_station_list()
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part ID Flood Warning System ***")
    run()
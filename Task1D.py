from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station

def run():
    """
    Docstring for run
    """
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))
    print(len(rivers), "rivers. First 10: ", rivers[0:9])

if __name__ == "__main__":
    print("*** Task 1D: CUED Part ID Flood Warning System ***")
    run()

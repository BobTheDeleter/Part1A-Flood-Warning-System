from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """

    """
    stations = build_station_list()
    inconsistent_stations = inconsistent_typical_range_stations(stations)
    inconsistent_station_names = [station.name for station in inconsistent_stations]
    inconsistent_station_names.sort()
    print(inconsistent_station_names)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part ID Flood Warning System ***")
    run()
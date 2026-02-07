from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """
    Prints the number of rivers with a station, and the first 10 rivers. Then prints stations on the Aire, Cam, and Thames.
    """
    stations = build_station_list()
    rivers = list(rivers_with_station(stations))
    rivers.sort()
    print(len(rivers), "rivers. First 10: ", rivers[0:10])

    stations_by_river_dict = stations_by_river(stations)

    aire_stations = stations_by_river_dict["River Aire"]
    aire_station_names = [airestation.name for airestation in aire_stations]
    aire_station_names.sort()
    print("River Aire: ", aire_station_names)

    cam_stations = stations_by_river_dict["River Cam"]
    cam_station_names = [camstation.name for camstation in cam_stations]
    cam_station_names.sort()
    print("River Cam: ", cam_station_names)

    thames_stations = stations_by_river_dict["River Thames"]
    thames_station_names = [thamesstation.name for thamesstation in thames_stations]
    thames_station_names.sort()
    print("River Thames: ", thames_station_names)

if __name__ == "__main__":
    print("*** Task 1D: CUED Part ID Flood Warning System ***")
    run()

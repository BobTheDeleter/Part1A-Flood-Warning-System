from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """
    Uses the function geo.stations_within_radius to build a list of stations within 10 km of the Cambridge city centre (coordinate (52.2053, 0.1218)). Print the names of the stations, listed in alphabetical order.
    """

    stations = build_station_list()

    within_radius = stations_within_radius(stations, (52.2053, 0.1218), 10)
    names = [wr.name for wr in within_radius]
    names.sort()
    print(names)

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()

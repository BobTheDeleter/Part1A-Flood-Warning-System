from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def run():
    """
    Provide a program file Task1B.py that uses geo.stations_by_distance and prints a list of tuples (station name, town, distance) for the 10 closest and the 10 furthest stations from the Cambridge city centre, (52.2053, 0.1218)
    """

    # Build list of stations
    stations = build_station_list()

    station_distances = stations_by_distance(stations, (52.2053, 0.1218))

    format_station = lambda x: (x[0].name, x[0].town, x[1])
    
    closest = [format_station(sd) for sd in station_distances[:10]]
    furthest = [format_station(sd) for sd in station_distances[-10:]]

    print(f"10 closest stations to Cambridge City Centre:\n{closest}")
    print("\n")
    print(f"10 furthest stations from Cambridge City Centre:\n{furthest}")

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()

from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    stations = [
        MonitoringStation(None, None, "test 1", (0, 0), None, None, "test 1"),
        MonitoringStation(None, None, "test 2", (0, 90), None, None, "test 2"),
        MonitoringStation(None, None, "test 3", (0, 180), None, None, "test 3"),
    ]

    station_distances = stations_by_distance(stations, (1, 1))

    assert [sd[0].name for sd in station_distances] == ["test 1", "test 2", "test 3"]

def test_stations_within_radius():
    stations = [
        MonitoringStation(None, None, "test 1", (0, 0), None, None, "test 1"),
        MonitoringStation(None, None, "test 2", (0, 1), None, None, "test 2"),
        MonitoringStation(None, None, "test 3", (0, 5), None, None, "test 3"),
    ]
        
    within_radius = stations_within_radius(stations, (0, 0), 120)
    names = [wr.name for wr in within_radius]

    assert ("test 1" in names) and ("test 2" in names) and ("test 3" not in names)
""" unit test for the geo module """

from floodsystem.geo import rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.station import MonitoringStation

def create_test_station_list():
    #anish, feel free to use this and change measure, label, coord, and trange if you need to. please don't change stationid, river, and town
    station_1 = MonitoringStation("station 1", "Measure 1", "Label 1", "Coord 1", "Trange1", "River Cam", "Town 1")
    
    station_2 = MonitoringStation("station 2", "Measure 2", "Label 2", "Coord 2", "Trange2", "River Cam", "Town 2")
    
    station_3 = MonitoringStation("station 3", "Measure 3", "Label 3", "Coord 3", "Trange3", "River Thames", "Town 3")

    return [station_1, station_2, station_3]

test_stations = create_test_station_list()

def test_rivers_with_station():
    rivers_with_station_set = rivers_with_station(test_stations)
    assert rivers_with_station_set == {"River Cam", "River Thames"}

def test_stations_by_river():
    stations_by_river_dict = stations_by_river(test_stations)
    assert stations_by_river_dict == {"River Cam": test_stations[0:2], "River Thames": test_stations[2:]}

def test_rivers_by_station_number():
    assert rivers_by_station_number(test_stations, 2) == [("River Cam", 2), ("River Thames", 1)]
    assert rivers_by_station_number(test_stations, 1) == [("River Cam", 2)]

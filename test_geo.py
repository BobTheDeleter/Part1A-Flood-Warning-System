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

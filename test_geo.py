from floodsystem.geo import stations_by_distance
from floodsystem.station import MonitoringStation

def test_stations_by_distance():
    stations = [
        MonitoringStation(None, None, "test 1", (0, 0), None, None, "test 1"),
        MonitoringStation(None, None, "test 2", (0, 90), None, None, "test 2"),
        MonitoringStation(None, None, "test 3", (0, 180), None, None, "test 3"),
    ]

    station_distances = stations_by_distance(stations, (1, 1))

    assert [sd[0].name for sd in station_distances] == ["test 1", "test 2", "test 3"]
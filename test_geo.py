from floodsystem.geo import rivers_with_station
from floodsystem.station import MonitoringStation

def test_rivers_with_station():
    station_1 = MonitoringStation("station 1", "Measure 1", "Trange1", "River Cam", "Town 1")
    
    station_2 = MonitoringStation("station 2", "Measure 2", "Trange2", "River Cam", "Town 2")
    
    station_3 = MonitoringStation("station 3", "Measure 3", "Trange3", "River Thames", "Town 3")

    stations = [station_1, station_2, station_3]

    rivers_with_station_set = rivers_with_station(stations)

    assert rivers_with_station_set == {"River Cam", "River Thames"}
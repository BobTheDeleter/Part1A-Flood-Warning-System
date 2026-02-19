from floodsystem.station import MonitoringStation   
from floodsystem.flood import stations_level_over_threshold 

def test_stations_level_over_threshold():
    s1 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s2 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s3 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s4 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s5 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s6 = MonitoringStation("test 2", None, None, None, (-2, 10), None, None)

    tolerance = 1.0
    s1.latest_level = 0
    s2.latest_level = 5
    s3.latest_level = 10
    s4.latest_level = 12.5
    s5.latest_level = 20
    s6.latest_level = 6

    assert stations_level_over_threshold([s1, s2, s3, s4, s5, s6], tolerance) == [(s4, 1.25), (s5, 2.0)]

test_stations_level_over_threshold()
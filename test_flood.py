from floodsystem.station import MonitoringStation   
from floodsystem.flood import *

def test_stations_level_over_threshold():
    s1 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s2 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s3 = MonitoringStation("test 3", None, None, None, (0, 10), None, None)
    s4 = MonitoringStation("test 4", None, None, None, (0, 10), None, None)
    s5 = MonitoringStation("test 5", None, None, None, (0, 10), None, None)
    s6 = MonitoringStation("test 6", None, None, None, (-2, 10), None, None)

    s1.latest_level = 0
    s2.latest_level = 5
    s3.latest_level = 10
    s4.latest_level = 12.5
    s5.latest_level = 20
    s6.latest_level = 6

    tolerance = 1.0
    print(stations_level_over_threshold([s1, s2, s3, s4, s5, s6], tolerance))

    assert stations_level_over_threshold([s1, s2, s3, s4, s5, s6], tolerance) == [(s5, 2.0), (s4, 1.25)]

def test_f_level_over_threshold():
    s1 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s2 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s3 = MonitoringStation("test 3", None, None, None, (0, 10), None, None)
    s4 = MonitoringStation("test 4", None, None, None, (0, 10), None, None)
    s5 = MonitoringStation("test 5", None, None, None, (0, 10), None, None)
    s6 = MonitoringStation("test 6", None, None, None, (-2, 10), None, None)

    s1.latest_level = 0
    s2.latest_level = 5
    s3.latest_level = 10
    s4.latest_level = 12.5
    s5.latest_level = 20
    s6.latest_level = 6

    tolerance = 1.0
    print(f_level_over_threshold([s1, s2, s3, s4, s5, s6], tolerance))

    assert f_level_over_threshold([s1, s2, s3, s4, s5, s6], tolerance) == [(s5, 2.0), (s4, 1.25)]

def test_stations_highest_rel_level():
    
    s1 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s2 = MonitoringStation("test 1", None, None, None, (0, 10), None, None)
    s3 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s4 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s5 = MonitoringStation("test 2", None, None, None, (0, 10), None, None)
    s6 = MonitoringStation("test 2", None, None, None, (-2, 10), None, None)
    s1.latest_level = 0
    s2.latest_level = 5
    s3.latest_level = 10
    s4.latest_level = 12.5
    s5.latest_level = 20
    s6.latest_level = 6
    
    assert stations_highest_rel_level([s1, s2, s3, s4, s5, s6], 3) == [s5, s4, s3]

test_stations_level_over_threshold()

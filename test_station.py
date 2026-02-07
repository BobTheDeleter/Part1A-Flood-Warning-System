# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    s1 = MonitoringStation("test 1", None, None, None, (1, 10), None, None)
    s2 = MonitoringStation("test 2", None, None, None, (0, 0), None, None)
    s3 = MonitoringStation("test 3", None, None, None, None, None, None)
    s4 = MonitoringStation("test 4", None, None, None, (10, 1), None, None)
    s5 = MonitoringStation("test 5", None, None, None, (-1, 1), None, None)

    assert s1.typical_range_consistent
    assert not s2.typical_range_consistent()
    assert not s3.typical_range_consistent()
    assert not s4.typical_range_consistent()
    assert not s5.typical_range_consistent()

def test_inconsistent_typical_range_stations():
    s1 = MonitoringStation("test 1", None, None, None, (1, 10), None, None)
    s2 = MonitoringStation("test 2", None, None, None, (0, 0), None, None)
    s3 = MonitoringStation("test 3", None, None, None, None, None, None)
    s4 = MonitoringStation("test 4", None, None, None, (10, 1), None, None)
    s5 = MonitoringStation("test 5", None, None, None, (-1, 1), None, None)

    assert set(inconsistent_typical_range_stations([s1, s2, s3, s4, s5])) == set([s2, s3, s4, s5])
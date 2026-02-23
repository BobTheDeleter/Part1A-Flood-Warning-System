from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.station import MonitoringStation

def test_plot_water_levels():
    try:
        plot_water_levels(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [[]],
            []
        )
    except ValueError:
        pass

    try:
        plot_water_levels(
            [],
            [[]],
            [[]]
        )
    except ValueError:
        pass

    try:
        plot_water_levels(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [],
            [[]]
        )
    except ValueError:
        pass

    try:
        plot_water_levels(
            [MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None)],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []]
        )
    except ValueError:
        pass

from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import datetime

def test_plot_water_levels_with_fit():
    try:
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [[]],
            [], 1
        )
    except ValueError:
        pass

    try:
        plot_water_level_with_fit(
            [],
            [[]],
            [[]], 1
        )
    except ValueError:
        pass

    try:
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [],
            [[]], 1
        )
    except ValueError:
        pass

    try:
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None)],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []], 1
        )
    except ValueError:
        pass
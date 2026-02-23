from floodsystem.plot import plot_water_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
import datetime

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
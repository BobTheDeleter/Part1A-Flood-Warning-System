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

    try:
        plot_water_levels([], [], [])
    except ValueError:
        pass

def test_plot_water_levels_with_fit():
    try: #levels don't match
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [[]],
            [], 1
        )
    except ValueError:
        pass

    try: #stations don't match
        plot_water_level_with_fit(
            [],
            [[]],
            [[]], 1
        )
    except ValueError:
        pass

    try: #dates don't match
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None)],
            [],
            [[]], 1
        )
    except ValueError:
        pass

    try: # greater than 6 stations
        plot_water_level_with_fit(
            [MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None), MonitoringStation(None, None, None, None, None, None, None)],
            [[], [], [], [], [], [], []],
            [[], [], [], [], [], [], []], 1
        )
    except ValueError:
        pass

    try: # no data
        plot_water_level_with_fit([], [], [], 1)
    except ValueError:
        pass
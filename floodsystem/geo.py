# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def stations_by_distance(stations: list[MonitoringStation], p: tuple[float, float]) -> list[tuple[MonitoringStation, float]]:
    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        station_distance.append((station, distance))

    station_distance.sort(key=lambda x:x[1])
    return station_distance

def stations_within_radius(stations: list[MonitoringStation], centre: tuple[float, float], r: float) -> list[MonitoringStation]:
    within_radius = []
    for station in stations:
        if haversine(station.coord, centre, unit=Unit.KILOMETERS) <= r:
            within_radius.append(station)

    return within_radius
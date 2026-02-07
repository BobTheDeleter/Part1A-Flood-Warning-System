# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def stations_by_distance(stations: list[MonitoringStation], p: tuple) -> list[tuple[MonitoringStation, float]]:
    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        station_distance.append((station, distance))

    station_distance.sort(key=lambda x:x[1])
    return station_distance
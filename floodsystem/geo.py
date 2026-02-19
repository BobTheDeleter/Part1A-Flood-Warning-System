# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.station import MonitoringStation
from haversine import haversine, Unit

def stations_by_distance(stations: list[MonitoringStation], p: tuple[float, float]) -> list[tuple[MonitoringStation, float]]:
    """
    Takes a list of stations and a coordinate point and outputs a list of stations and their distances from the point in km, sorted by distance.
    """
    station_distance = []
    for station in stations:
        distance = haversine(station.coord, p, unit=Unit.KILOMETERS)
        station_distance.append((station, distance))

    station_distance.sort(key=lambda x:x[1])
    return station_distance

def stations_within_radius(stations: list[MonitoringStation], centre: tuple[float, float], r: float) -> list[MonitoringStation]:
    """
    Takes a list of stations, a coordinate point and a radius in km and outputs only those stations in the list within the radius of the point. 
    """
    within_radius = []
    for station in stations:
        if haversine(station.coord, centre, unit=Unit.KILOMETERS) <= r:
            within_radius.append(station)

    return within_radius
from .utils import sorted_by_key  # noqa
import heapq

#TASK 1D

def rivers_with_station(stations):
    """
    outputs a set of names of rivers which have at least one monitoring station in the list of stations given
    
    :param stations: list of MonitoringStation objects
    """
    set_of_rivers = set()
    for station in stations:
        set_of_rivers.add(station.river)
    return set_of_rivers


def stations_by_river(stations):
    """
    outputs a dictionary of {rivers (str): [stations (obj)]}
    
    :param stations: list of MonitoringStation objects
    """
    #{river: stations}
    stations_by_river_dict = {}
    for station in stations:
        if station.river not in stations_by_river_dict:
            stations_by_river_dict[station.river] = [station]
        else:
            mylist = stations_by_river_dict[station.river]
            mylist.append(station)
            stations_by_river_dict[station.river] = mylist
    return stations_by_river_dict

#TASK 1E

def rivers_by_station_number(stations, N):
    """
    Creates a list of (river, number of stations) tuples in order of most to least stations
    
    :param stations: list of MonitoringStation objects
    :param N: integer, number of rivers in output list
    """

    stations_by_river_dict = stations_by_river(stations)

    num_stations_list = [len(stations_list) for stations_list in stations_by_river_dict.values()]

    rivers_numbers = zip(stations_by_river_dict.keys(), num_stations_list)

    sorted_rivers_numbers = heapq.nlargest(N, rivers_numbers, key=lambda x: x[1])

    for i in range(len(num_stations_list)):
        number = num_stations_list[i]
        river = list(stations_by_river_dict.keys())[i]
        if number == sorted_rivers_numbers[-1][1]:
            if (river, number) not in sorted_rivers_numbers:
                sorted_rivers_numbers.append((river, number))
    
    return sorted_rivers_numbers

# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa


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
    Docstring for stations_by_river
    
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
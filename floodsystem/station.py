# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):
        """Create a monitoring station."""

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name) #string
        d += "   id:            {}\n".format(self.station_id) #string (hyperlink)
        d += "   measure id:    {}\n".format(self.measure_id) #string (hyperlink)
        d += "   coordinate:    {}\n".format(self.coord) #tuple of two floats
        d += "   town:          {}\n".format(self.town) #string
        d += "   river:         {}\n".format(self.river) #string
        d += "   typical range: {}".format(self.typical_range) #tuple of two floats
        return d
    
    def typical_range_consistent(self):
        trange = self.typical_range
        if trange == (0, 0) or trange == None or trange[0] < 0 or trange[1] < 0:
            return False
        elif trange[1] < trange[0]:
            return False
        else:
            return True
        
    def relative_water_level(self):
        trange = self.typical_range
        level = self.latest_level
        return (level - trange[0])/(trange[1] - trange[0])

def inconsistent_typical_range_stations(stations):
    inconsistent_stations = []
    for station in stations:
        if MonitoringStation.typical_range_consistent(station) == False:
            inconsistent_stations.append(station)
    
    return inconsistent_stations
from floodsystem.station import MonitoringStation
import heapq

def stations_level_over_threshold(stations, tol):
    """
    Returns a list of tuples (stations, relative_water_level) of stations with level over the tolerance
    
    :param stations: list of station objects
    :param tol: float, tolerance of relative water level
    """

    #In the submodule flood, implement a function that returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the relative level in descending order. 
    stations_levels = []
    for station in stations:
        level = station.relative_water_level()
        if type(level) == float:
            if level > tol:
                stations_levels.append((station, level))
    stations_levels.sort(key=lambda x: x[1], reverse=True)
    return stations_levels
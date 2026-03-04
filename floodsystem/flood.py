from floodsystem.station import MonitoringStation
import heapq
from floodsystem.datafetcher import fetch_measure_levels

def stations_level_over_threshold(stations: list[MonitoringStation], tol: float) -> list[tuple[MonitoringStation, float]]:
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

#might need further measures to exclude illigitimate data, eg thornhill

#the following function can replace the above function, with greater generality.

def f_level_over_threshold(f, stations, tol):
    """
    Returns a list of stations with level over the tolerance, sorted by greatest to least level.
    
    :param f: a property of station, such as current level, predicted level, or rate of increase???
    :param stations: list of station objects
    :param tol: float, tolerance of relative water level
    """

    #In the submodule flood, implement a function that returns a list of tuples, where each tuple holds (i) a station (object) at which the latest relative water level is over tol and (ii) the relative water level at the station. The returned list should be sorted by the relative level in descending order. 
    stations_levels = []
    for station in stations:
        level = f(station)
        if type(level) == float:
            if level > tol:
                stations_levels.append((station, level))
    stations_levels.sort(key=lambda x: x[1], reverse=True)
    return stations_levels

def alt_stations_highest_rel_level(stations, N):
    """
    returns a list of station objects of the N highest relative water levels

    :param stations: list of station objects
    :param N: integer, number of stations to return
    """
    stations_levels = []
    for station in stations:
        level = station.relative_water_level()
        if type(level) == float:
            stations_levels.append((station, level))
    sorted_stations_levels = heapq.nlargest(N, stations_levels, key=lambda x: x[1])
    return [station_level[0] for station_level in sorted_stations_levels]

def stations_highest_rel_level(stations, N) -> list[MonitoringStation]:
    stations_levels = stations_level_over_threshold(stations, 0)
    n_stations_levels = stations_levels[0:N]
    return [station_level[0] for station_level in n_stations_levels]
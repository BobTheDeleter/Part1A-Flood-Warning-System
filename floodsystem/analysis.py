'''
This module provides functionality for fitting functions to historic water levels.
'''

import datetime
import numpy
from floodsystem.flood import *

def polyfit(dates: list[datetime.datetime], levels: list[float], p: int) -> tuple[numpy.poly1d, float]:
    '''
    This function returns a polynomial of degree p using x = dates and y = levels.
    It also returns a date offset, which should be subtracted from any input to the polynomial. This is done to avoid floating point errors.
    '''
    # convert dates to floats
    date_floats = [date.timestamp() for date in dates]

    # shift dates to avoid floating point errors with large floats
    shifted_dates = [d - date_floats[0] for d in date_floats]
    p_coeff = numpy.polyfit(shifted_dates, levels, p)
    poly = numpy.poly1d(p_coeff)

    return (poly, date_floats[0])

def risk_assessment(stations, severe_tol, high_tol, moderate_tol):
    """
    Returns a list of [[severe towns], [high towns], [moderate towns], [low towns]] based on the level of the station in each town, and the given tolerances for each risk level.
    """

    # + set(f_level_over_threshold(predicted_level, stations, pred_severe_tol)) + set(f_level_over_threshold(rate, stations, rate_severe_tol))
    
    #creates sets of severe, high, and moderate risk towns by subtracting higher risk sets from a set of everything above a particular risk level's threshold.
    severe_towns = set([x[0].town for x in stations_level_over_threshold(stations, severe_tol)])
    high_towns = set([x[0].town for x in stations_level_over_threshold(stations, high_tol)]) - severe_towns
    moderate_towns =  set([x[0].town for x in stations_level_over_threshold(stations, moderate_tol)]) - high_towns
    low_towns = set(x.town for x in stations) - moderate_towns

    return [list(severe_towns), list(high_towns), list(moderate_towns), list(low_towns)]
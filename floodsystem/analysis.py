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

def stations_over_relative_levels(stations: list[MonitoringStation], tolerances: list[float]) -> list[list[MonitoringStation]]:
    """
    Returns a list of lists of stations based on the current relative water level of the station, and the given tolerances for each risk level.
    """
    tolerances.sort(reverse=True) # highest risk level first
    stations_at_above_tolerance = []

    for tol in tolerances:
        stations_at_above_tolerance.append(set(station_rel_level[0] for station_rel_level in stations_level_over_threshold(stations, tol)))

    for i, risk_level in enumerate(stations_at_above_tolerance, start=1):
        for higher_risk_level in stations_at_above_tolerance[:i-1]:
            risk_level -= higher_risk_level

    return stations_at_above_tolerance

def apply_polynomial_to_date_range(polynomial_fit: numpy.poly1d, date_offset: float, start_date: datetime.datetime, end_date: datetime.datetime) -> numpy.ndarray:
    """
    Returns the predicted hourly relative water level of a station over a time period, based on a polynomial fit to historic data.
    """

    # create hourly intervals between start and end date
    date_range = [start_date + datetime.timedelta(hours=i) for i in range(int((end_date - start_date).total_seconds() / 3600) + 1)]
    # predict level for each datetime
    date_range_timstamps = numpy.array([date.timestamp() for date in date_range])
    return polynomial_fit(date_range_timstamps - date_offset)

def will_exceed_relative_level_in_range(station: MonitoringStation, polynomial_fit: numpy.poly1d, date_offset: float, start_date: datetime.datetime, end_date: datetime.datetime, relative_tol: float) -> bool:
    """
    Returns True if the predicted water level of a station will exceed its typical range in the given date range, and False otherwise.
    """

    predicted_levels = apply_polynomial_to_date_range(polynomial_fit, date_offset, start_date, end_date)
    return any(predicted_levels > station.typical_range[1]*relative_tol)
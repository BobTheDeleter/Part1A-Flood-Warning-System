'''
This module provides functionality for fitting functions to historic water levels.
'''

import datetime
import numpy

def polyfit(dates: list[datetime.datetime], levels: list[float], p: int) -> tuple[numpy.poly1d, float]:
    '''
    This function returns a polynomial of degree p using x = dates and y = levels.
    It also returns a date offset, which should be subtracted from any input to the polynomial. This is done to avoid floating point errors.
    '''
    # convert dates to floats
    date_floats = [date.timestamp() for date in dates]

    # shift dates to avoid floating point errors with large floats
    p_coeff = numpy.polyfit([date_float - date_floats[0] for date_float in date_floats], levels, p)
    poly = numpy.poly1d(p_coeff)

    return (poly, date_floats[0])
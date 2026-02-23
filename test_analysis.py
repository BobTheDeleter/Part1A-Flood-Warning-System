from floodsystem.analysis import polyfit
import datetime
import numpy

def test_polyfit():
    # perfect linear relationship
    dates = [
        datetime.datetime(2022, 1, 1),
        datetime.datetime(2022, 1, 2),
        datetime.datetime(2022, 1, 3),
    ]

    levels = [2.0, 4.0, 6.0]

    poly, d0 = polyfit(dates, levels, 1)

    shifted = [d.timestamp() - d0 for d in dates]
    predictions = [poly(x) for x in shifted]

    assert numpy.allclose(predictions, levels)

    ## qudratic
    base = datetime.datetime(2023, 1, 1)
    dates = [base + datetime.timedelta(days=i) for i in range(5)]

    levels = [float(i)**2 for i in range(5)]

    poly, d0 = polyfit(dates, levels, 2)

    shifted = [d.timestamp() - d0 for d in dates]
    predictions = [poly(x) for x in shifted]

    assert numpy.allclose(predictions, levels)
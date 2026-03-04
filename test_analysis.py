from floodsystem.analysis import *
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

def test_stations_over_relative_level():
    from floodsystem.station import MonitoringStation

    station1 = MonitoringStation("id1", "measure_id1", "name1", (0, 0), (0.0, 1.0), "river1", "town1")
    station2 = MonitoringStation("id2", "measure_id2", "name2", (0, 0), (0.0, 1.0), "river2", "town2")
    station3 = MonitoringStation("id3", "measure_id3", "name3", (0, 0), (0.0, 1.0), "river3", "town3")

    station1.latest_level = 1.6 # relative level 1.6
    station2.latest_level = 1.3 # relative level 1.3
    station3.latest_level = 1.0 # relative level 1.0

    stations = [station1, station2, station3]

    result = stations_over_relative_levels(stations, [1.5, 1.2, 0.0])

    assert set(result[0]) == {station1} # above 1.5
    assert set(result[1]) == {station2} # above 1.2 but not above 1.5
    assert set(result[2]) == {station3} # not above 1.2


def test_apply_polynomial_to_date_range():
    base = datetime.datetime(2023, 1, 1)
    dates = [base + datetime.timedelta(days=i) for i in range(5)]
    levels = [float(i)**2 for i in range(5)]

    poly, d0 = polyfit(dates, levels, 2)

    predicted_levels = apply_polynomial_to_date_range(poly, d0, base, base + datetime.timedelta(days=4))

    # Generate expected hourly predictions
    hourly_dates = [base + datetime.timedelta(hours=i) for i in range(int((base + datetime.timedelta(days=4) - base).total_seconds() / 3600) + 1)]
    expected_levels = [poly(date.timestamp() - d0) for date in hourly_dates]

    assert numpy.allclose(predicted_levels, expected_levels)

def test_will_exceed_relative_level_in_range():
    station = MonitoringStation("id1", "measure_id1", "name1", (0, 0), (0.0, 1.0), "river1", "town1")
    station.latest_level = 1.6 # relative level 1.6

    base = datetime.datetime(2023, 1, 1)
    dates = [base + datetime.timedelta(days=i) for i in range(5)]
    levels = [float(i)**2 for i in range(5)]

    poly, d0 = polyfit(dates, levels, 2)

    assert will_exceed_relative_level_in_range(station, poly, d0, base, base + datetime.timedelta(days=4), 1.5) == True
    assert will_exceed_relative_level_in_range(station, poly, d0, base, base + datetime.timedelta(days=4), 36.0) == False
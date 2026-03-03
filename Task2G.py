#First, I am going to compare the relative levels to some current govt warnings
from floodsystem.flood import *
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import risk_assessment


#Could these please be methods of station?
def predicted_level(station):
    """
    Predicts the level of a station ??
    """
    return

def rate_of_increase(station):
    """
    Measures current gradient of increase?
    """

def run():
    stations = build_station_list()
    update_water_levels(stations)
    towns_at_risk = risk_assessment(stations, 1.5, 1.3, 1.1)
    print("SEVERE:")
    print(towns_at_risk[0])
    print("HIGH: ")
    print(towns_at_risk[1])
    print("MODERATE: ")
    print(towns_at_risk[2])

if __name__ == '__main__':
    print("*** Task 2G: CUED Part ID Flood Warning System ***")
    run()
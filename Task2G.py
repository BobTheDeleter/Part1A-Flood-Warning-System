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
    print(risk_assessment(stations, 1.5, 1.2, 1))

if __name__ == '__main__':
    print("*** Task 2G: CUED Part ID Flood Warning System ***")
    run()
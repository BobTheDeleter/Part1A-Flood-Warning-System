# Use the plotly library to plot the stations on a map, colour coded by risk level
import plotly.express as px
from floodsystem.analysis import stations_over_relative_levels
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list, update_water_levels
import pandas

def plot_all_stations_on_map(stations: list[MonitoringStation], tolerances: list[float], colors: list[str], sizes: list[int]):
    """
    Plots the stations on a map, colour coded by risk level based on the given tolerances.
    Colors should be a list from lowest risk to highest risk (e.g., green to red).
    Sizes should be a list from lowest risk to highest risk (smaller to larger).
    """
    
    stations_at_risk = stations_over_relative_levels(stations, tolerances)
    stations_at_risk.reverse() # lowest risk first, so that highest risk is plotted on top

    lats = []
    lons = []
    colours = []
    station_sizes = []
    hover_names = []
    hover_data = []

    for risk_level, stations in enumerate(stations_at_risk):
        for station in stations:
            if station.coord[0] is None or station.coord[1] is None:
                continue

            lats.append(station.coord[0])
            lons.append(station.coord[1])
            colours.append(colors[risk_level])
            station_sizes.append(sizes[risk_level])
            hover_names.append(station.name)
            hover_data.append(station.relative_water_level())

    dataframe = pandas.DataFrame({
        "lat": lats,
        "lon": lons,
        "hover_name": hover_names,
        "relative_water_level": hover_data,
        "color": colours,
        "size": station_sizes
    })

    color_discrete_map = {c: c for c in colors}

    fig = px.scatter_map(
        dataframe,
        lat="lat",
        lon="lon",
        color="color",
        size="size",
        hover_name="hover_name",
        hover_data="relative_water_level",
        color_discrete_map=color_discrete_map,
        zoom=5,
    )

    fig.update_layout(map_style="open-street-map")
    fig.show()

def plot_grouped_stations_on_map(stations_by_risk_level: list[list[MonitoringStation]], colors: list[str], sizes: list[int]):
    """
    Plots the stations on a map, colour coded by risk level based on the given tolerances.
    Colors should be a list from lowest risk to highest risk (e.g., green to red).
    Sizes should be a list from lowest risk to highest risk (smaller to larger).
    """
    
    lats = []
    lons = []
    colours = []
    station_sizes = []
    hover_names = []
    hover_data = []

    for risk_level, stations in enumerate(stations_by_risk_level):
        for station in stations:
            if station.coord[0] is None or station.coord[1] is None:
                continue

            lats.append(station.coord[0])
            lons.append(station.coord[1])
            colours.append(colors[risk_level])
            station_sizes.append(sizes[risk_level])
            hover_names.append(station.name)
            hover_data.append(station.relative_water_level())

    dataframe = pandas.DataFrame({
        "lat": lats,
        "lon": lons,
        "hover_name": hover_names,
        "relative_water_level": hover_data,
        "color": colours,
        "size": station_sizes
    })

    color_discrete_map = {c: c for c in colors}

    fig = px.scatter_map(
        dataframe,
        lat="lat",
        lon="lon",
        color="color",
        size="size",
        hover_name="hover_name",
        hover_data="relative_water_level",
        color_discrete_map=color_discrete_map,
        zoom=5,
    )

    fig.update_layout(map_style="open-street-map")
    fig.show()

def run():
    stations = build_station_list()
    update_water_levels(stations)

    LOW = 1.1
    MODERATE = 1.3
    SEVERE = 1.5
    FLOOD = 2.0

    # Colors from lowest risk (green) to highest risk (red)
    colors = ["gray", "green", "yellow", "orange", "red"]

    # Sizes from lowest risk (small) to highest risk (large)
    sizes = [1, 3, 6, 10, 15]

    plot_all_stations_on_map(stations, [FLOOD, SEVERE, MODERATE, LOW, -100], colors, sizes) # the -100 is to ensure that stations with no data are coloured as well

if __name__ == '__main__':
    print("*** Plotting stations on map ***")
    run()
"""
This module provides functionality for plotting monitoring station data
"""

from .station import MonitoringStation
from datetime import datetime
import plotly.express as px
from plotly.subplots import make_subplots
from plotly import graph_objects
import pandas

def plot_water_levels(stations: list[MonitoringStation], dates_combined:list[list[datetime]], levels_combined: list[list[float]]):
    if len(stations) > 6 or len(stations) < 1:
        raise ValueError("Can only plot between 1 and 6 stations.")
    if len(stations) != len(dates_combined) or len(stations) != len(levels_combined):
        raise ValueError("Number of stations, date series and level series don't match.")
    
    # Enough space for up to 6 plots
    figure = make_subplots(rows=2, cols=3, subplot_titles=[station.name for station in stations])

    for i in range(len(stations)):
        station = stations[i]
        dates = dates_combined[i]
        levels = levels_combined[i]

        # Determining row and 
        row = (i // 3) + 1
        col = (i % 3) + 1

        figure.add_trace(
            graph_objects.Line(
                x=dates,
                y=levels
            ),
            row=row, col=col
        )

        # Lines for typical range
        figure.add_hline(y=station.typical_range[0], line_color='#ff0000', row=row, col=col)
        figure.add_hline(y=station.typical_range[1], line_color='#0000ff', row=row, col=col)
    
    figure.update_layout(showlegend=False, title_text=f'Water level over time for {", ".join([station.name for station in stations])}')

    figure.show()
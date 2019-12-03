from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models import NumeralTickFormatter

def create_mortality_bar_plot(main_df):
    """
    This method plots a bar plot with total mortality rate of children 
    below 5 years in different regions of the world
    """
    regions = list(main_df.region.unique())
    averages = []

    #isolating data within the year in question
    data_2013 = main_df.loc[2013]

    for _region_ in regions:
        reg_data = data_2013[data_2013.region == _region_]
        average = reg_data.child_mortality.mean()
        averages.append(average)
    
    source = ColumnDataSource(data = dict(x_axis = regions, y_axis = averages, color = Spectral6))

    fig = figure(x_range = regions, plot_width = 650, plot_height = 350, title = "Average Child Mortality Per Region (2013)")
    fig.vbar( x= 'x_axis', top = 'y_axis', width = 0.9, color = 'color', source = source)

    fig.xgrid.grid_line_color = None
    fig.yaxis[0].formatter = NumeralTickFormatter(format="0,")
    hover = HoverTool(tooltips = [
        ('Region', '@x_axis'),
            ('Child Mortality', '@y_axis{0,}')
        ])
    fig.add_tools(hover)
    fig.xaxis.axis_label = "Regions"
    fig.yaxis.axis_label = "Number of Children"

    return fig

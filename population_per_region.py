from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models import NumeralTickFormatter

def create_bar_chart(main_df):
    """
    This method creates a bar plot of the total population of people
    in the world per region
    """
    regions = list(main_df.region.unique())
    counts = []

    #isolating data within the year in question
    data_2013 = main_df.loc[2013]

    #Create a  mask of the year in question and calculate the totals
    for _region_ in regions:
        reg_data = data_2013[data_2013.region == _region_]
        count = reg_data.population.sum()
        counts.append(count)

    source = ColumnDataSource(data = dict(x_axis = regions, y_axis = counts, color = Spectral6))

    fig = figure(x_range = regions, plot_width = 650, plot_height = 350, title = "Total Population Per Region (2013)")
    fig.vbar( x= 'x_axis', top = 'y_axis', width = 0.9, color = 'color', source = source)

    fig.xgrid.grid_line_color = None
    fig.yaxis[0].formatter = NumeralTickFormatter(format="0,")
    hover = HoverTool(tooltips = [
        ('Region', '@x_axis'),
            ('Population', '@y_axis{0,}')
        ])
    fig.add_tools(hover)
    fig.xaxis.axis_label = "Regions"
    fig.yaxis.axis_label = "Total Population"

    return fig



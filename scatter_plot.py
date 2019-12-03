from bokeh.plotting import figure
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.models import NumeralTickFormatter, LinearInterpolator, CategoricalColorMapper

def create_scatter_plot(main_df):
    """
    This plot is used to depict the GDP vs Life Expectancy of 
    countries in different regions of the world.

    The size of the buble is influenced by the population of a country
    and the colour depicts the region
    """
    fig = figure(title = 'Life Expectancy Against GDP in 2013', x_axis_type = 'log',
             x_range = (200, 200000),y_range = (20, 100), plot_width=1300, plot_height=400)
    
    data_2013 = main_df.loc[2013]

    source = ColumnDataSource(dict(x = data_2013.gdp, y = data_2013.life, 
                               country = data_2013.Country, population = data_2013.population, 
                               region = data_2013.region))
    
    hover = HoverTool(tooltips="@country : $@x")

    size_mapper = LinearInterpolator(x = [main_df.population.min(), main_df.population.max()],
                                 y = [5, 75])
    
    colour_mapper = CategoricalColorMapper(factors = list(main_df.region.unique()),
                                      palette = Spectral6)
    
    fig.circle(x = 'x', y = 'y',
           size = {
               'field' : 'population',
               'transform' : size_mapper
           },
           color = {
               'field': 'region',
               'transform': colour_mapper
           },
           alpha = 0.7,
           legend = 'region',
           source = source)
    
    fig.xaxis[0].formatter = NumeralTickFormatter(format="$0,")
    fig.add_tools(hover)
    fig.legend.location = 'top_center'
    fig.legend.orientation = "horizontal"
    fig.xaxis.axis_label = "GDP Per Capita"
    fig.yaxis.axis_label = "Life Expectancy"

    return fig
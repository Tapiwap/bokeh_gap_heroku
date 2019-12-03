import pandas as pd
from bokeh.io import curdoc
from scatter_plot import create_scatter_plot
from population_per_region import create_bar_chart
from child_mortality_plot import create_mortality_bar_plot
from bokeh.layouts import Row, Column

main_df = pd.read_csv('gapminder_tidy.csv', index_col = 'Year')

scatter_plot = create_scatter_plot(main_df)
pop_per_region_bar = create_bar_chart(main_df)
child_mortality_bar = create_mortality_bar_plot(main_df)

column = Column(pop_per_region_bar, child_mortality_bar)
first_row = Row(scatter_plot)
second_row = Row(child_mortality_bar, pop_per_region_bar)

curdoc().add_root(first_row)
curdoc().add_root(second_row)
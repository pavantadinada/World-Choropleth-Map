import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv('death.csv')

fig = go.Figure(data=go.Choropleth(
    locations = df['CODE'],
    z = df['DEATHS (THOUSANDS)'],
    text = df['COUNTRY'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_tickprefix = '',
    colorbar_title = 'DEATHS<br>THOUSANDS',
))

fig.update_layout(
    title_text='WORLD HEART FAILURE DEATHS',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.5,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Deaths in Thousands',
        showarrow = False
    )]
)

app = dash.Dash()


app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True)
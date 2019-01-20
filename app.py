#import packages
import pandas
import pandas_datareader as web
import datetime
# dash components
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server


app.layout = html.Div(children = [
    html.H1(children = 'Stock Ticker',
    style={
        'textAlign': 'center'
    }),
    html.Div(children = '''
    Select Company '''),

    dcc.Dropdown(
        id='my-dropdown',
        options=[
            {'label': 'TESLA', 'value': 'TSLA'},
            {'label': 'APPLE', 'value': 'AAPL'},
            {'label': 'GOOGLE', 'value': 'GOOG'},
            {'label': 'AMAZON', 'value': 'AMZN'},
            {'label': 'FACEBOOK', 'value': 'FB'},
            {'label': 'NIKE', 'value': 'NKE'},
            {'label': 'ALI BABA', 'value': 'BABA'},
            {'label': 'NETFLIX', 'value': 'NFLX'}
        ],
        value='TSLA'
    ),

    html.Div(dcc.Graph(id = 'stock_graph'))


])


@app.callback(
    Output ('stock_graph', 'figure'),
    [Input( component_id = 'my-dropdown', component_property = 'value')]
    )

def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'iex', start, end)

    trace = go.Scatter( x = df.index,
                        y = df.close,
                        name = 'Closing',
                        mode = 'lines+markers')


    data = [trace]
    layout = go.Layout(title = 'Stock Closing Price',
                        xaxis = dict(title = 'Date'),
                        yaxis = dict(title = 'Price'))
    return {'data' : data, 'layout' : layout}




if __name__ == '__main__':
    app.run_server(debug = True)

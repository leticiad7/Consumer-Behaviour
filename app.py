# imports
from asyncio.base_events import Server
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
#from dash import dcc



# setup
app = dash.Dash('', title='Consumer Behaviour', external_stylesheets=['static/photon.min.css'])
server = app.server

#------ import data
# Region 
#nyorkshire = pd.read_csv("nyorkshire_updated.csv") - when i uncomment it complains 

# Layout
app.layout = html.Div([
    html.H1('Consumer Behaviour'),
    html.Div([
        html.H4('5 most sold products'),
        dcc.Graph(id='pie-graph',
        figure={}, className='top_5'),

        html.H4('5 least sold products')

    ])
    ])



# run: ensures we dont try to run the app using both gunicorn and flask's in-built server
if __name__ == '__main__':
    app.run_server(debug=True)

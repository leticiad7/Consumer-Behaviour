import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from matplotlib.pyplot import figure, xlabel
import pandas as pd
import plotly.express as px

#Quantity sold by all branches 
quantity_sold_allbranches = pd.read_csv("data/allbranches_quantity_sold.csv")
#print(quantity_sold_allbranches)
quantity_sold_allbranches_fig = px.bar(quantity_sold_allbranches, x="Branch", y = "Quantity sold", title = "Quantity sold by all branches")

#Amount in GBP sold by all branches 
amount_in_gbp_allbranches = pd.read_csv("data/allbranches_amountgbp.csv")
#print(amount_in_gbp_allbranches)
amount_in_gbp_allbranches = px.bar(amount_in_gbp_allbranches, x="Branch", y = "Amount Sold", title = "Amount in GBP sold by all branches")

#Profitability
profitability = pd.read_csv("data/profitability.csv")
#print(profitability)
profitability = px.bar(profitability, x="Branch", y = "Profitability", title = "Profitability")

per_hour_data = [{"label": "belfast", "value": "data/per_hour/belf_per_hour.csv"}, 
                {"label": "east camb", "value": "data/per_hour/eastc_per_hour.csv"}, 
                {"label": "flins", "value": "data/per_hour/flins_per_hour.csv"}, 
                {"label": "forest", "value": "data/per_hour/forest_per_hour.csv"}, 
                {"label": "fylde", "value": "data/per_hour/fylde_per_hour.csv"}, 
                {"label": "islington", "value": "data/per_hour/islington_per_hour.csv"}, 
                {"label": "lichfield", "value": "data/per_hour/lichfield_per_hour.csv"}, 
                {"label": "nyorshire", "value": "data/per_hour/nyorshire_per_hour.csv"}, 
                {"label": "orkney", "value": "data/per_hour/orkney_per_hour.csv"}]

branches = [{"label": "belfast", "value": "data/branches/belf_top5.csv"}]



app = dash.Dash(__name__, title= "Dashboard")
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1("Consumer Behaviour"),
    ]),
      html.Div([
        html.H2("Quantity sold by all branches"),
        html.Div([
            dcc.Graph(figure= quantity_sold_allbranches_fig, id="quantity_sold_allbranches")                        
            ]),
        ]),

        html.Div([
        html.H2("Amount in GBP sold by all branches"),
        html.Div([
            dcc.Graph(figure= amount_in_gbp_allbranches, id="amount_in_gbp_allbranches")                        
            ]),
        ]),

        html.Div([
        html.H2("Profitability"),
        html.Div([
            dcc.Graph(figure= profitability, id="profitability")                        
            ]),
        ]),
                
        html.Div([
        html.H2("Quantity sold by Belfast branch"),
            dcc.Dropdown(options=branches, id="most_least_sold"),
        html.Div([
            dcc.Graph(figure= {}, id="belfast")                        
            ]),
        ]),

        html.Div([
        html.H2("Quantity sold by all branches per hour"),
            dcc.Dropdown(options=per_hour_data, id="soldperhour"),
        html.Div([
            dcc.Graph(figure= {}, id="belfast_perhour")                        
            ]),
        ]),

])

####Most and least products sold by each branch 
@app.callback(
    Output(component_id="belfast", component_property="figure"),
    Input(component_id="most_least_sold", component_property="value")
)               
def plot_quantity_sold_by_branch(value):
        if value is not None: 
            belfast = pd.read_csv(value)
            belfast = px.bar(belfast.head(), x="products", y = "quantity")
            return belfast
        return {}


###Quantity sold per hour 
@app.callback(
    Output(component_id="belfast_perhour", component_property="figure"),
    Input(component_id="soldperhour", component_property="value")
)               
def plot_quantity_perhour(value):
    #per hour 
    if value is not None: 
        belfast_perhour = pd.read_csv(value)
        #figure_one = px.bar(belfast_perhour, y = "hour")
        return px.line(belfast_perhour, y="Sales per hour", x= "hour")
    return {}

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
from matplotlib.pyplot import figure, xlabel
import pandas as pd
import plotly.express as px

#Quantity sold by all branches 
quantity_sold_allbranches = pd.read_csv("data/allbranches_quantity_sold.csv")
#print(quantity_sold_allbranches)
quantity_sold_allbranches = px.bar(quantity_sold_allbranches, x="Branch", y = "Quantity sold", title = "Quantity sold by all branches")

#Amount in GBP sold by all branches 
amount_in_gbp_allbranches = pd.read_csv("data/allbranches_amountgbp.csv")
#print(amount_in_gbp_allbranches)
amount_in_gbp_allbranches = px.bar(amount_in_gbp_allbranches, x="Branch", y = "Amount Sold", title = "Amount in GBP sold by all branches")

#Profitability
profitability = pd.read_csv("data/profitability.csv")
#print(profitability)
profitability = px.bar(profitability, x="Branch", y = "Profitability", title = "Profitability")

#
belfast = pd.read_csv("data/belfast_fixed.csv")
belfast = px.bar(belfast, x="products", y = "quantity")

app = dash.Dash(__name__, title= "Dashboard")
server = app.server

app.layout = html.Div([
    html.Div([
        html.H1("Consumer Behaviour"),
    ]),
      html.Div([
        html.H2("Quantity sold by Belfast branch"),
        html.Div([
            dcc.Graph(figure= belfast)                        
            ]),
        ]),

      html.Div([
        html.H2("Quantity sold by all branches"),
        html.Div([
            dcc.Graph(figure= quantity_sold_allbranches)                        
            ]),
        ]),

        html.Div([
        html.H2("Amount in GBP sold by all branches"),
        html.Div([
            dcc.Graph(figure= amount_in_gbp_allbranches)                        
            ]),
        ]),

        html.Div([
        html.H2("Profitability"),
        html.Div([
            dcc.Graph(figure= profitability)                        
            ]),
        ]),
])
                      
@app.callback(
    #Output(component_id="profitability", component_property="figure"),
    #Output(component_id="amount_in_gbp_allbranches", component_property="figure"),
    Output(component_id="quantity_sold_allbranches", component_property="figure"),
    Input(component_id="quantity_sold_allbranches", component_property="value")
)               
def plot_quantity_sold_allbranches(value):
    figure_one = px.bar(quantity_sold_allbranches[quantity_sold_allbranches["Branch"] == value], xlabel= "Branch", y = "Quantity sold")
    return figure_one

@app.callback(
    Output(component_id="belfast", component_property="figure"),
    Input(component_id="belfast", component_property="value")
)               
def plot_products_by_region(value):
    figure_one = px.bar(belfast[belfast["products"] == value], xlabel= "products", y = "quantity")
    return figure_one


if __name__ == '__main__':
    app.run_server(debug=True)

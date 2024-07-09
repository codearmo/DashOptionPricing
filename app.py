#app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from pricing import BS_CALLDIV, BS_PUTDIV
# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout of the app
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.Label('Option Type', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Dropdown(
                id='option-type',
                options=[
                    {'label': 'Call', 'value': 'call'},
                    {'label': 'Put', 'value': 'put'}
                ],
                value='call',
                clearable=False,
                style={'marginBottom': '10px'}
            )
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Stock Price (S)', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='stock-price', type='number', value=100, step=0.01, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Strike Price (K)', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='strike-price', type='number', value=100, step=0.01, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Days to Expiry', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='days-to-expiry', type='number', value=30, step=1, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Risk-free Rate (r)', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='risk-free-rate', type='number', value=0.05, step=0.01, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Dividend Yield (q)', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='dividend-yield', type='number', value=0, step=0.01, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Label('Volatility (sigma)', style={'fontWeight': 'bold', 'fontSize': '16px'}),
            dcc.Input(id='volatility', type='number', value=0.3, step=0.01, style={'width': '100%', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Button('Price Option', id='submit-button', n_clicks=0, color='primary', style={'width': '100%', 'padding': '10px', 'fontSize': '16px'})
        ], width=4, style={'marginBottom': '15px'}),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            html.Div(id='output-container', children='', style={'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc', 'backgroundColor': '#f9f9f9'})
        ], width=12),
    ])
], fluid=True, style={'padding': '20px', 'backgroundColor': '#f7f7f7', 'borderRadius': '10px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'})


# Callback function to handle the inputs and perform calculations
@app.callback(
    Output('output-container', 'children'),
    Input('submit-button', 'n_clicks'),
    State('option-type', 'value'),
    State('stock-price', 'value'),
    State('strike-price', 'value'),
    State('days-to-expiry', 'value'),
    State('risk-free-rate', 'value'),
    State('dividend-yield', 'value'),
    State('volatility', 'value')
)
def update_output(n_clicks, option_type, S, K, days_to_expiry, r, q, sigma):
    if n_clicks > 0:
        T = days_to_expiry / 252  # Convert days to years
        price = BS_CALLDIV(S=S, K=K, T=T, r=r, q=q, sigma=sigma ) if option_type == 'call' else BS_PUTDIV(S=S, K=K, T=T, r=r, q=q, sigma=sigma )
        return f'Price = {price}, Option Type: {option_type}, S: {S}, K: {K}, T: {T}, r: {r}, q: {q}, sigma: {sigma}'
    return ''

if __name__ == '__main__':
    app.run_server(debug=True)

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from calculator import main
from buildings import create_data
import plotly.graph_objects as go
import plotly.express as px

px.set_mapbox_access_token("pk.eyJ1IjoiY2hhcmxpZWNob2YiLCJhIjoiY2trMmozbzJwMGp1NDJwcW94dHAzdmYxZSJ9.PWhcvXLn2xNSZV_gkKpXbw")
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat="centroid_lat", lon="centroid_lon",     color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Waterschade Voorspeller'

colors = {
    'MainBackground': '#60A3D9',
    'HeaderBackground': '#0074B7',
    'SubmitButtonBackground': '#BFD7ED'
}

if __name__ == '__main__':
    app.layout = html.Div([

        html.Div([
            html.Div('Waterschade Voorspeller',
                     style={'color': 'white',
                            'fontSize': 30,
                            'text-align': 'center'})
        ], style={'marginBottom': 25,
                  'marginTop': 0,
                  'backgroundColor': colors['HeaderBackground']}),

        html.Div([
            html.Div([

                # html.Label('Buurt',
                #            style={'marginLeft': 22.5}),
                # dcc.Dropdown(
                #     options=[
                #         {'label': 'Ondiep', 'value': 'Ondiep'},
                #         {'label': 'Witte Vrouwen', 'value': 'Witte Vrouwen'},
                #         {'label': 'Ondiep', 'value': '3'},
                #     ],
                #     value='Initial Value',
                #     id='gekozenBuurt',
                #     style={'marginLeft': 11,
                #            'width': '50%'}),

                html.Label('Kies de benodigde files van de buurt',
                           style={'marginLeft': 22.5}),
                dcc.Upload(
                    id='buurtFiles',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files',
                               style={'color': 'white'})
                    ]),
                    style={'width': '60%',
                           'padding': 3,
                           'verticalAlign': 'middle',
                           'marginLeft': 22,
                           'marginBottom': 10,
                           'lineHeight': '60px',
                           'borderWidth': '1px',
                           'borderStyle': 'dashed',
                           'borderRadius': '5px',
                           'textAlign': 'center',
                           'background': colors['SubmitButtonBackground']
                           },
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.Label('Prijs',
                           style={'marginLeft': 22.5}),
                dcc.Dropdown(
                    options=[
                        {'label': 'Boven', 'value': 'boven'},
                        {'label': 'Onder', 'value': 'onder'},
                    ],
                    value='prijs',
                    id='reparatieMaanden',
                    style={'marginLeft': 11,
                           'width':'50%'}),

                # html.Label('Hoelang duurt de reparatie (in dagen). Max 20 dagen',
                #            style={'marginLeft': 22.5}),
                #     dcc.Input(
                #         value='dagen',
                #         id='reparatieDagen',
                #         type='number',
                #         style={'marginLeft': 22,
                #                'width':'20%'}),
                #
                # html.Label('In welke maand vindt de reparatie plaats',
                #            style={'marginLeft': 22.5}),
                #     dcc.Dropdown(
                #         options=[
                #             {'label': 'Januari', 'value': '1'},
                #             {'label': 'Februari', 'value': '2'},
                #             {'label': 'Maart', 'value': '3'},
                #             {'label': 'April', 'value': '4'},
                #             {'label': 'Mei', 'value': '5'},
                #             {'label': 'Juni', 'value': '6'},
                #             {'label': 'Juli', 'value': '7'},
                #             {'label': 'Augustus', 'value': '8'},
                #             {'label': 'September', 'value': '9'},
                #             {'label': 'Oktober', 'value': '10'},
                #             {'label': 'November', 'value': '11'},
                #             {'label': 'December', 'value': '12'},
                #         ],
                #         value='maand',
                #         id='reparatieMaanden',
                #         style={'marginLeft': 11,
                #                'width':'50%'}),

                html.Label('Scenario',
                           style={'marginLeft': 22.5}),
                dcc.RadioItems(
                    options=[
                        {'label': 'Laag', 'value': 'Laag'},
                        {'label': 'Gemiddeld', 'value': 'Gemiddelde'},
                        {'label': 'Hoog', 'value': 'Hoog'}
                    ],
                    value='Initial Value',
                    id='scenario',
                    style={'marginLeft': 22}
                ),

                html.Button('Submit',
                            id='submitButton',
                            n_clicks=0,
                            style={'width': '20%',
                                   'marginTop': 40,
                                   'marginLeft': 140,
                                   'marginBottom': 440,
                                   'backgroundColor': colors['SubmitButtonBackground']}
                            ),

            ], id='input_div',
                style={'width': '40%',
                       'marginBottom': 25,
                       'marginTop': 0,
                       'display': 'flex',
                       'flexDirection': 'column',
                       'backgroundColor': colors['MainBackground']}),

            html.Div([
                html.Div('Berekenen waterschade...',
                         id='output_div',
                         style={'color': 'white',
                                'fontSize': 30,
                                'text-align': 'center'}),
                dcc.Graph(figure=fig)
            ], style={'marginBottom': 25,
                      'marginTop': 0,
                      'display': 'flex',
                      'backgroundColor': 'MainBackground'}
            ),


        ], style={'marginBottom': 25,
                  'marginLeft': 75,
                  'display': 'flex',
                  'backgroundColor': colors['MainBackground']}),

    ], style={'columnCount': 1,
              'backgroundColor': colors['MainBackground']})

    @app.callback(Output('output_div', 'children'),
                  Input('submitButton', 'n_clicks'),
                  State('buurtFiles', 'filename'),
                  State('scenario', 'value'))

    def update_output(clicks, gekozen_buurtFiles, scenario):
        antwoorden = [gekozen_buurtFiles, scenario]
        if 'Initial Value' not in antwoorden and None not in antwoorden:
            return create_data(gekozen_buurtFiles, scenario, ['gebruiksdo', 'oppervlakt', 'MAX'])
        else:
            return 'Vul de nodige gegevens in'

    app.run_server(debug=True)
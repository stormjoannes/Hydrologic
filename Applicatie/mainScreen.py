import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from Applicatie.buildings import create_data
import plotly.graph_objects as go

def makeMap(latitudes, longtitudes, calculations):
    mapbox_access_token = "pk.eyJ1IjoiY2hhcmxpZWNob2YiLCJhIjoiY2trMmozbzJwMGp1NDJwcW94dHAzdmYxZSJ9.PWhcvXLn2xNSZV_gkKpXbw"
    #Invoeren alle latitudes en longtitudes met bijbehorende gegevens
    fig = go.Figure(go.Scattermapbox(
            lat=latitudes,
            lon=longtitudes,
            mode='markers',
            marker=go.scattermapbox.Marker(
            ),
            text=calculations,
        ))

    #Instellingen voor de map en het begin pointview
    fig.update_layout(
        autosize=True,
        hovermode='closest',
        mapbox=dict(
            accesstoken=mapbox_access_token,
            bearing=0,
            center=dict(
                lat=52.1064958,
                lon=5.101
            ),
            pitch=0,
            zoom=14.5
        ),
    )
    return fig

#Import concents
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#Tab titel
app.title = 'Waterschade Voorspeller'

#Alle gebruikte kleuren definiëren
colors = {
    'MainBackground': '#60A3D9',
    'HeaderBackground': '#0074B7',
    'SubmitButtonBackground': '#BFD7ED'
}

#Main div maken
if __name__ == '__main__':
    app.layout = html.Div([
        #Koptitel aanmaken
        html.Div([
            html.Div('Waterschade Voorspeller',
                     style={'color': 'white',
                            'fontSize': 30,
                            'text-align': 'center'})
        ], style={'marginBottom': 25,
                  'marginTop': 0,
                  'backgroundColor': colors['HeaderBackground']}),

        #Div voor input en output naast elkaar
        html.Div([
            #Linker div voor alle inputs
            html.Div([
                html.Label('Kies de benodigde files van de buurt',
                           style={'marginLeft': 22.5}),
                html.Div([
                    dcc.Dropdown(
                        id='gekozen_buurt',
                        options=[
                            {'label': 'Ondiep', 'value': 'Ondiep'},
                            {'label': 'Witte Vrouwen', 'value': 'Witte Vrouwen'}
                        ],
                        value='Initial Value',
                        style={'marginLeft': 11,
                               'marginBottom': 11,
                               'width': '50%'}
                    ),
                ]),

                html.Label('Scenario',
                           style={'marginLeft': 22.5}),
                dcc.RadioItems(
                    options=[
                        {'label': 'Laag', 'value': 'LOW'},
                        {'label': 'Gemiddeld', 'value': 'MEDIUM'},
                        {'label': 'Hoog', 'value': 'HIGH'}
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
                # dcc.Graph(figure=fig, style={'display':'None'}),
                html.Div('Berekenen waterschade...',
                         id='output_div',
                         style={'color': 'white',
                                'fontSize': 30,
                                'text-align': 'center'})
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

    #verkrijgen van de input values
    @app.callback(Output('output_div', 'children'),
                  Input('submitButton', 'n_clicks'),
                  State('gekozen_buurt', 'value'),
                  State('scenario', 'value'))

    def update_output(clicks, gekozen_buurt, scenario):
        antwoorden = [gekozen_buurt, scenario]
        #zorgen dat alles ingevuld is voordat je op submit kan drukken en resultaten krijgt
        if 'Initial Value' not in antwoorden and None not in antwoorden:
            data = create_data(gekozen_buurt, scenario, ['gebruiksdo', 'oppervlakt', 'MAX', 'LAT', 'LNG'])
            latitudes = []
            longtitudes = []
            calculations = []
            for i in data:
                #De latitude min de correcte van de goede coördinaten
                latitudes.append(float(i.lat) - 0.0009846483658)
                #De latitude min de correcte van de goede coördinaten
                longtitudes.append(float(i.lng) - 0.0003943217995)
                #Format voor de geschatte waterschade
                calculations.append('geschatte waterschade: €' + str(round(i.waterschatting, 2)))
            print(latitudes)
            return dcc.Graph(figure=makeMap(latitudes, longtitudes, calculations),
                             style={'height':'100%',
                                    'width':'100%',
                                    'color': colors['MainBackground']})
        else:
            return 'Vul de nodige gegevens in'

    app.run_server(debug=True)
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from calculator import main


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

                html.Label('Buurt .shp File',
                           style={'marginLeft': 22.5}),
                dcc.Upload(
                    id='buurtFile',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
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
                    multiple=False
                ),

                html.Label('Hoelang duurt de reparatie (in dagen). Max 20 dagen',
                           style={'marginLeft': 22.5}),
                    dcc.Input(
                        value='dagen',
                        id='reparatieDagen',
                        type='number',
                        style={'marginLeft': 22,
                               'width':'20%'}),

                html.Label('In welke maand vindt de reparatie plaats',
                           style={'marginLeft': 22.5}),
                    dcc.Dropdown(
                        options=[
                            {'label': 'Januari', 'value': '1'},
                            {'label': 'Februari', 'value': '2'},
                            {'label': 'Maart', 'value': '3'},
                            {'label': 'April', 'value': '4'},
                            {'label': 'Mei', 'value': '5'},
                            {'label': 'Juni', 'value': '6'},
                            {'label': 'Juli', 'value': '7'},
                            {'label': 'Augustus', 'value': '8'},
                            {'label': 'September', 'value': '9'},
                            {'label': 'Oktober', 'value': '10'},
                            {'label': 'November', 'value': '11'},
                            {'label': 'December', 'value': '12'},
                        ],
                        value='maand',
                        id='reparatieMaanden',
                        style={'marginLeft': 11,
                               'width':'50%'}),

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

    @app.callback(Output('output_div', 'children'),
                  Input('submitButton', 'n_clicks'),
                  State('buurtFile', 'filename'),
                  State('reparatieDagen', 'value'),
                  State('reparatieMaanden', 'value'),
                  State('scenario', 'value'))

    def update_output(clicks, gekozen_buurtFile, reparatieDagen, reparatieMaanden, scenario):
        antwoorden = [gekozen_buurtFile, reparatieDagen, reparatieMaanden, scenario]
        if 'Initial Value' not in antwoorden and None not in antwoorden:
            if gekozen_buurtFile.split(".")[1] == 'shp':
                return gekozen_buurtFile, reparatieDagen, reparatieMaanden, scenario
            else:
                return 'Het gekozen bestand moet een .shp file zijn'
        else:
            return 'Vul de nodige gegevens in'

    app.run_server(debug=True)
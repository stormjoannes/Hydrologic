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
            html.Div('Waterschade Voorspeller', style={'color': 'white', 'fontSize': 30, 'text-align': 'center'})
        ], style={'marginBottom': 25, 'marginTop': 0, 'backgroundColor': colors['HeaderBackground']}),

        html.Div([
            html.Div([

                html.Label('Buurt', style={'marginLeft': 22.5}),
                dcc.Dropdown(
                    options=[
                        {'label': 'Ondiep', 'value': 'Ondiep'},
                        {'label': 'Witte Vrouwen', 'value': 'Witte Vrouwen'},
                    ],
                    value='Initial Value',
                    id='buurt',
                    style={'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10}
                ),

                html.Label('Bebouwing', style={'marginLeft': 22.5}),
                dcc.Dropdown(
                    options=[
                        {'label': 'Gezondheid', 'value': 'Gezondheid'},
                        {'label': 'Onderwijs', 'value': 'Onderwijs'},
                        {'label': 'Industrie', 'value': 'Industrie'},
                        {'label': 'Winkel', 'value': 'Winkel'},
                        {'label': 'Kantoor', 'value': 'Kantoor'},
                        {'label': 'Logies', 'value': 'Logies'},
                        {'label': 'Woon', 'value': 'Woon'},
                        {'label': 'Bijeenkomst', 'value': 'Bijeenkomst'},
                        {'label': 'Cel', 'value': 'Cel'},
                        {'label': 'Sport', 'value': 'Sport'},
                        {'label': 'Land- en Akkerbouw', 'value': 'Land- en Akkerbouw'},
                        {'label': 'Natuur en Recreatie', 'value': 'Natuur en Recreatie'},
                    ],
                    value='Initial Value',
                    id='bebouwing',
                    style={'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10}
                ),

                html.Label("Als 'Land- en Akkerbouw' is gekozen", style={'marginLeft': 22.5, 'display':'none'}, id= 'land'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Agrarisch gras', 'value': 'Agrarisch gras'},
                        {'label': 'Granen', 'value': 'Granen'},
                        {'label': 'Maïs', 'value': 'Maïs'},
                        {'label': 'Aardappelen', 'value': 'Aardappelen'},
                        {'label': 'Bieten', 'value': 'Bieten'},
                        {'label': 'Overige landbouwgewassen', 'value': 'Overige landbouwgewassen'},
                        {'label': 'Fruitteelt', 'value': 'Fruitteelt'},
                        {'label': 'Bloembollen', 'value': 'Bloembollen'},
                        {'label': 'Hoogstam', 'value': 'Hoogstam'},
                        {'label': 'Kassen / glastuinbouw', 'value': 'Kassen / glastuinbouw'},
                    ],
                    value='Initial Value',
                    id='landbouw',
                    style={'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'none'}
                ),

                html.Label("Als 'Natuur en Recreatie' is gekozen", style={'marginLeft': 22.5, 'display':'none'}, id= 'nature'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Sportparken', 'value': 'Sportparken'},
                        {'label': 'Terreinen', 'value': 'Terreinen'},
                        {'label': 'Begraafplaatsen', 'value': 'Begraafplaatsen'},
                        {'label': 'Volkstuinen', 'value': 'Volkstuinen'},
                        {'label': 'Recreatie', 'value': 'Recreatie'},
                        {'label': 'Groen in stedelijk gebied', 'value': 'Groen in stedelijk gebied'},
                    ],
                    value='Initial Value',
                    id='natuur',
                    style={'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'none'}
                ),

                html.Label('regenval in mm', style={'marginLeft': 22.5}),
                dcc.Input(value='Initial Value', type='number',
                          id='regenval',
                          style={'width': '30%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 22,
                                 'marginBottom': 10}),

                html.Label('waterafvoer via put in mm', style={'marginLeft': 22.5}),
                dcc.Input(value='Initial Value', type='number',
                          id='waterafvoer',
                          style={'width': '30%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 22,
                                 'marginBottom': 10}),

                html.Label('Scenario', style={'marginLeft': 22.5}),
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

                html.Button('Submit', id='submitButton', n_clicks=0,
                            style={'width': '20%', 'marginLeft': 220, 'marginBottom': 40,
                                   'backgroundColor': colors[
                                       'SubmitButtonBackground']}),

            ], id='input_div', style={'width': '40%', 'marginBottom': 25, 'marginTop': 0, 'display': 'flex', 'flexDirection': 'column',
                      'backgroundColor': colors['MainBackground']}),

            html.Div([
                html.Div('TEST', id='output_div', style={'color': 'white', 'fontSize': 30, 'text-align': 'center'})
            ], style={'marginBottom': 25, 'marginTop': 0, 'display': 'flex', 'backgroundColor': 'MainBackground'}),

        ], style={'marginBottom': 25, 'marginLeft': 75, 'display': 'flex',
                  'backgroundColor': colors['MainBackground']}),

    ], style={'columnCount': 1, 'backgroundColor': colors['MainBackground']})

    @app.callback(Output('nature', 'style'),
                  Output('natuur', 'style'),
                  Output('land', 'style'),
                  Output('landbouw', 'style'),
                  Input('bebouwing', 'value'),
                  State('nature', 'style'),
                  State('land', 'style'),
                  State('bebouwing', 'value'))

    def update_style(input, natuur, landbouw, bebouwing):
        print(input, natuur, bebouwing)
        if bebouwing == 'Natuur en Recreatie':
            print('hoi')
            return {'marginLeft': 22.5, 'display':'block'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'block'}, {'marginLeft': 22.5, 'display':'none'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'none'}
        elif bebouwing == 'Land- en Akkerbouw':
            return {'marginLeft': 22.5, 'display':'none'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'none'}, {'marginLeft': 22.5, 'display':'block'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'block'}
        else:
            return {'marginLeft': 22.5, 'display': 'none'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display': 'none'}, {'marginLeft': 22.5, 'display':'none'}, {'width': '60%', 'padding': 3, 'verticalAlign': 'middle', 'marginLeft': 10,
                           'marginBottom': 10, 'display':'none'}

    @app.callback(Output('output_div', 'children'),
                  Input('submitButton', 'n_clicks'),
                  State('buurt', 'value'),
                  State('bebouwing', 'value'),
                  State('landbouw', 'value'),
                  State('natuur', 'value'),
                  State('regenval', 'value'),
                  State('waterafvoer', 'value'),
                  State('scenario', 'value'))

    def update_output(clicks, gekozen_buurt, bebouwing, landbouw, natuur, regenval, waterafvoer, scenario):
        antwoorden = [gekozen_buurt, bebouwing, landbouw, natuur, regenval, waterafvoer, scenario]
        print(clicks)
        if bebouwing != 'Natuur en Recreatie' and bebouwing != 'Land- en Akkerbouw':
            antwoorden.remove(landbouw)
            antwoorden.remove(natuur)
        else:
            if bebouwing != 'Natuur en Recreatie':
                antwoorden.remove(natuur)
            else:
                antwoorden.remove(landbouw)

        print(antwoorden)
        if 'Initial Value' not in antwoorden and None not in antwoorden:
            return gekozen_buurt, bebouwing, landbouw, natuur, regenval, waterafvoer, scenario
        else:
            return 'Vul de nodige parameters in'

    app.run_server(debug=True)
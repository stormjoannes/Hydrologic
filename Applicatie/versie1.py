import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Buurt'),
    dcc.Dropdown(
        options=[
            {'label': 'Ondiep', 'value': 'MTL'},
        ],
        value='MTL'
    ),

    html.Label('Bebouwing'),
    dcc.Dropdown(
        options=[
            {'label': 'Gezondheid', 'value': 'MTL'},
            {'label': 'Onderwijs', 'value': 'MTL'},
            {'label': 'Industrie', 'value': 'MTL'},
            {'label': 'Winkel', 'value': 'MTL'},
            {'label': 'Kantoor', 'value': 'MTL'},
            {'label': 'Logies', 'value': 'MTL'},
            {'label': 'Woon', 'value': 'MTL'},
            {'label': 'Bijeenkomst', 'value': 'MTL'},
            {'label': 'Cel', 'value': 'MTL'},
            {'label': 'Sport', 'value': 'MTL'},
            {'label': 'Land- en Akkerbouw', 'value': 'MTL'},
            {'label': 'Natuur en Recreatie', 'value': 'MTL'},
        ],
        value='MTL'
    ),

    html.Label("Als 'Land- en Akkerbouw' is gekozen"),
    dcc.Dropdown(
        options=[
            {'label': 'Agrarisch gras', 'value': 'MTL'},
            {'label': 'Granen', 'value': 'MTL'},
            {'label': 'Maïs', 'value': 'MTL'},
            {'label': 'Aardappelen', 'value': 'MTL'},
            {'label': 'Bieten', 'value': 'MTL'},
            {'label': 'Overige landbouwgewassen', 'value': 'MTL'},
            {'label': 'Fruitteelt', 'value': 'MTL'},
            {'label': 'Bloembollen', 'value': 'MTL'},
            {'label': 'Hoogstam', 'value': 'MTL'},
            {'label': 'Kassen / glastuinbouw', 'value': 'MTL'},
        ],
        value='MTL'
    ),

    html.Label("Als 'Natuur en Recreatie' is gekozen"),
    dcc.Dropdown(
        options=[
            {'label': 'Sportparken', 'value': 'MTL'},
            {'label': 'Terreinen', 'value': 'MTL'},
            {'label': 'Begraafplaatsen', 'value': 'MTL'},
            {'label': 'Volkstuinen', 'value': 'MTL'},
            {'label': 'Recreatie', 'value': 'MTL'},
            {'label': 'Groen in stedelijk gebied', 'value': 'MTL'},
        ],
        value='MTL'
    ),

    html.Label('regenval in mm'),
    dcc.Input(value='MTL', type='number'),

    html.Label('waterafvoer via put in mm'),
    dcc.Input(value='MTL', type='number'),

    # html.Label('Multi-Select Dropdown'),
    # dcc.Dropdown(
    #     options=[
    #         {'label': 'New York City', 'value': 'NYC'},
    #         {'label': u'Montréal', 'value': 'MTL'},
    #         {'label': 'San Francisco', 'value': 'SF'}
    #     ],
    #     value=['MTL', 'SF'],
    #     multi=True
    # ),

    html.Label('Scenario'),
    dcc.RadioItems(
        options=[
            {'label': 'Laag', 'value': 'la'},
            {'label': 'Gemiddeld', 'value': 'gem'},
            {'label': 'Hoog', 'value': 'ho'}
        ],
        value='MTL'
    ),

    # html.Label('Checkboxes'),
    # dcc.Checklist(
    #     options=[
    #         {'label': 'New York City', 'value': 'NYC'},
    #         {'label': u'Montréal', 'value': 'MTL'},
    #         {'label': 'San Francisco', 'value': 'SF'}
    #     ],
    #     value=['MTL', 'SF']
    # ),

    # html.Label('Slider'),
    # dcc.Slider(
    #     min=0,
    #     max=9,
    #     marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
    #     value=5,
    # ),
], style={'columnCount': 1})

if __name__ == '__main__':
    app.run_server(debug=True)
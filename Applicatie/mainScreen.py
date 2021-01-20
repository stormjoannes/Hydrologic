import base64
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, State, Input
from buildings import create_data
import plotly.graph_objects as go

mapbox_access_token = "pk.eyJ1IjoiY2hhcmxpZWNob2YiLCJhIjoiY2trMmozbzJwMGp1NDJwcW94dHAzdmYxZSJ9.PWhcvXLn2xNSZV_gkKpXbw"
#Invoeren alle latitudes en longtitudes met bijbehorende gegevens
fig = go.Figure(go.Scattermapbox(
        lat=['52.1044958',
             '52.1047415'],
        lon=['5.0986251',
             '5.0984616'],
        mode='markers',
        marker=go.scattermapbox.Marker(
        ),
        text=["Thijmes huis",
              "overkant"],
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
                    dcc.Upload(
                        id='upload-image',
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
                        multiple=True
                    ),
                    html.Div(id='output-image-upload'),
                ]),
                # html.Label('Prijs',
                #            style={'marginLeft': 22.5}),
                # dcc.Dropdown(
                #     options=[
                #         {'label': 'Boven', 'value': 'boven'},
                #         {'label': 'Onder', 'value': 'onder'},
                #     ],
                #     value='prijs',
                #     id='reparatieMaanden',
                #     style={'marginLeft': 11,
                #            'marginBottom': 11,
                #            'width':'50%'}),

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
                dcc.Graph(figure=fig),
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

    def parse_contents(contents, filename):
        return html.Div([
            html.H5(filename),

            # HTML images accept base64 encoded strings in the same format
            # that is supplied by the upload
            html.Img(src=contents)],
            style= {'marginLeft':22}
        )

    @app.callback(Output('output-image-upload', 'children'),
                  Input('upload-image', 'contents'),
                  State('upload-image', 'filename'))

    def update_output(list_of_contents, list_of_names):
        if list_of_contents is not None:
            children = [
                parse_contents(c, n) for c, n in
                zip(list_of_contents, list_of_names)]
            return children

    #verkrijgen van de input values
    @app.callback(Output('output_div', 'children'),
                  Input('submitButton', 'n_clicks'),
                  State('upload-image', 'contents'),
                  State('scenario', 'value'))

    def update_output(clicks, uploadimage, scenario):
        antwoorden = [uploadimage, scenario]
        #zorgen dat alles ingevuld is voordat je op submit kan drukken en resultaten krijgt
        if uploadimage != 'None':
            print(uploadimage)
            content_type, content_string = uploadimage[0].split(',')
            decoded = base64.b64decode(content_string)
        if 'Initial Value' not in antwoorden and None not in antwoorden:
            return create_data(decoded, scenario, ['gebruiksdo', 'oppervlakt', 'MAX'])
        else:
            return 'Vul de nodige gegevens in'


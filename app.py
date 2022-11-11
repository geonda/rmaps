import rmaps
import direction
import plotly.graph_objects as go
import dash
import dash_bootstrap_components as dbc


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

left_jumbotron = dash.html.Div(
    [
        dash.html.H2("Locate your next whiskey bar", className="display-3"),
        dash.html.Hr(className="my-2"),
        dash. html.P(
            "go ahead and press the button "
        ),
        dbc.Button("show the way", id='submit-val',
                   color="light", outline=True),
        dbc.Button("refresh", id='submit-val-2', color="light", outline=True),
    ],
    className="h-100 p-5 text-white bg-dark rounded-3",
)
import rmaps_test

@app.callback(
    dash.Output('container-button-timestamp', 'children'),
    dash.Input('submit-val', 'n_clicks'),
    dash.Input('submit-val-2', 'n_clicks'),
)
def displayClick(n1, n2):
    if 'submit-val-2' == dash.ctx.triggered_id:
        fig = go.Figure()
        ws1 = rmaps.maps(fig)
        output = dash.dcc.Graph(figure=ws1.fig, style={'height': '100vh'})
    elif 'submit-val' == dash.ctx.triggered_id:
        fig = go.Figure()
        ws2 = rmaps_test.maps(fig)  # direction.maps(fig)
        output = dash.dcc.Graph(figure=ws2.fig, style={'height': '100vh'})
    else:
        fig = go.Figure()
        ws1 = rmaps.maps(fig)
        output = dash.dcc.Graph(figure=ws1.fig, style={'height': '100vh'})
    return dash.html.Div(output)


app.layout = dbc.Row(
    [
        dbc.Col(left_jumbotron, md=3,),
        dbc.Col(dash.html.Div(id='container-button-timestamp'), md=9,)
    ],
    className="align-items-md-stretch"
)

app.run_server(debug=True, use_reloader=True)

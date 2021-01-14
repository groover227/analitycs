import dash
import dash_core_components as dcc
import plotly.graph_objs as go
import dash_html_components
import dash.dependencies
import pandas as pd
import dash_html_components as html

data = pd.read_csv("C:\\Users\\Александр\\PycharmProjects\\microblog-0.5\\AlexanderEx13\\AlexanderEx13_clients.csv", encoding='windows-1251')
print(data.head())

html.Div(children=[
	html.Div([
    	dcc.Graph(
        	id='example-graph',
        	figure={
            	'data': [ {'x': data['date'],'y': data['Sales'],'type': 'line'} ],
            	'layout': go.Layout(
                        	xaxis={"title":"Time"}, yaxis={"title":"Sales"}) } )
    		], style={"display":"inline-block", "width":"35%"})
	])
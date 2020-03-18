import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas_datareader.data as web
import datetime

#Here is where the headr of the python program start
app = dash.Dash()

#app.layout can assign part of tbe soon to be page
#as a section of the page, with children =() 
#each comma represenct another section isn the code
app.layout = html.Div(children=[
#first section of code children
        
    html.Div(children='''
        symbol to graph
    '''),
#second section of code children
#the data in Figure has mutli parts, 
#the x,y and type
#layout holds garah important contextual info
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph'),
    dcc.Input(id='upperinput', value='', type='text'),
    html.Div(id='top-graph'),
   
])

#here is where the headr of the python program stops
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# this is a section of the of the page,
@app.callback(
    Output(component_id='top-graph', component_property='children'),
    [Input(component_id='upperinput', component_property='value')]
    )

def ticke(you_data):     
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(you_data, 'yahoo', start, end)
   
    return dcc.Graph(
        id='topper-graph',
        figure={
            'data': [
              {'x':df.index, 'y':df.Close, 'type': 'bar', 'name': you_data},
            ],
            'layout':{
                'title': you_data
            }
        }
   )
# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# this is a section of the of the page

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )
def update_graph(input_data):
      
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
      
    return dcc.Graph(
        id='example-graph',
        figure={
            'data': [
              {'x':df.index, 'y':df.Close, 'type': 'line', 'name': input_data},
            ],
            'layout':{
                'title': input_data
            }
        }
   )
    

if __name__ == '__main__':
    app.run_server(debug=True)
    
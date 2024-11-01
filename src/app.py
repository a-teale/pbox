import numpy, dash, math
import plotly.graph_objects as go
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__,external_stylesheets=external_stylesheets)

server = app.server

ColorWay = ["#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52",
            "#636efa", "#EF553B", "#00cc96", "#ab63fa", "#FFA15A", "#19d3f3", "#FF6692", "#B6E880", "#FF97FF", "#FECB52",
            "#636efa", "#EF553B"]

nVLabel = {0: '0', 5: '5', 10: '10', 15: '15', 20: '20'}

app.layout = html.Div([
    html.H1('Particle in an Infinite Well',style={'font-family': 'sans-serif',"margin-top": "20","margin-bottom": "10", 'padding-left': '2.5%','padding-right': '2.5%'}),
    html.Div([
        html.Div([html.Div(html.H5('Range Of Eigenstates',style={'font-family': 'sans-serif','textAlign': 'center'}),id='max_v_lab'),
                dcc.RangeSlider(id='nrng',min=1,max=10,step=1,value=[1,1],marks=nVLabel,updatemode='drag',tooltip=dict(always_visible=False,placement='bottom'),dots=False)],style={'width': '80%', 'display': 'inline-block', 'padding-left': '10%','padding-right': '10%'})
        ],style={'width': '100%', 'display': 'inline-block','vertical-align': 'middle'}),
        html.Br(),html.Br(),
        html.Div([
            html.Div([html.H5('Wavefunction ψ',style={'font-family': 'sans-serif',"margin-top": "10","margin-bottom": "5",'textAlign': 'center'}),dcc.Graph(id='pbox_psi',config={'displayModeBar': False})],style={'width': '45%', 'padding-left': '2.5%','padding-right': '2.5%', 'display': 'inline-block'}),
            html.Div([html.H5('Probability Density |ψ|²',style={'font-family': 'sans-serif',"margin-top": "10","margin-bottom": "5",'textAlign': 'center'}),dcc.Graph(id='pbox_psi2',config={'displayModeBar': False})],style={'width': '45%', 'padding-left': '2.5%','padding-right': '2.5%', 'display': 'inline-block'})
        ],style={'width': '100%', 'display': 'inline-block','vertical-align': 'middle'})
])

@app.callback(
    Output('pbox_psi', 'figure'),
    [Input('nrng'  , 'value')])
def UpdateWfn(nrng):
    nmin, nmax = nrng[0], nrng[1]
    L = 5.0
    h = 1.0 #6.62607004e-34 
    m = 1.0 #9.10938356e-31
    q = numpy.linspace(0,L,num=501)
    w = numpy.zeros((501))
    fig = go.Figure()
    #Add the well
    #fig.add_trace(go.Scatter(x=q,y=Vofq,mode='lines',line_shape='spline',line_color='black',line_width=1.0,name='V(q)',hoverinfo='name'))
    for n in range(nmin,nmax+1):
        w[:] = ((n*n)*(h*h))/(8.0*m*L*L)
        Phi =  0.025*numpy.sqrt(2.0/L)*numpy.sin((n*numpy.pi*q)/L) + w 
        #Energy Level
        fig.add_trace(go.Scatter(x=q,y=w,mode='lines',line_shape='spline',line_width=1.0,line_dash='dash',line_color='black',hoverinfo='none'))
        #Wavefunction
        fig.add_trace(go.Scatter(x=q,y=Phi,mode='lines',line_shape='spline',line_width=2.0,name='&#968;<sub>{0:d}</sub>'.format(n),hoverinfo='name',fill='tonexty',line_color=ColorWay[n]))
        
    fig.update_layout(template='plotly_white',margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},hovermode='closest',autosize=True,legend=dict(orientation='h',yanchor='middle',y=1.0,xanchor='center',x=0.5,bgcolor="rgba(0,0,0,0)",font=dict(size=12)),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(title='x',tickformat = 'd',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=10),showticklabels=False,range=[0,L]),yaxis=dict(tickformat = 'd',showgrid=False,showline=False,linewidth=2,linecolor='black',anchor='free',position=0.0,ticks="outside",tickwidth=2,ticklen=0,title_font=dict(size=12),tickfont=dict(size=10),showticklabels=False,range=[0,0.6]),showlegend=False) 
    fig.add_vline(x=5.0, line_width=3, line_color="black")
    fig.add_vline(x=0.0, line_width=3, line_color="black")
    return fig

@app.callback(
    Output('pbox_psi2','figure'),
    [Input('nrng'  , 'value')])
def UpdateWfn2(nrng):
    nmin, nmax = nrng[0], nrng[1]
    L = 5.0
    h = 1.0 #6.62607004e-34 
    m = 1.0 #9.10938356e-31
    q = numpy.linspace(0,L,num=501)
    w = numpy.zeros((501))
    fig = go.Figure()
    #Add the well
    #fig.add_trace(go.Scatter(x=q,y=Vofq,mode='lines',line_shape='spline',line_color='black',line_width=1.0,name='V(q)',hoverinfo='name'))
    for n in range(nmin,nmax+1):
        w[:] = ((n*n)*(h*h))/(8.0*m*L*L)
        Phi =  0.025*numpy.sqrt(2.0/L)*numpy.sin((n*numpy.pi*q)/L)* (numpy.sqrt(2.0/L)*numpy.sin((n*numpy.pi*q)/L)) + w 
        #Energy Level
        fig.add_trace(go.Scatter(x=q,y=w,mode='lines',line_shape='spline',line_width=1.0,line_dash='dash',line_color='black',hoverinfo='none'))
        #Wavefunction
        fig.add_trace(go.Scatter(x=q,y=Phi,mode='lines',line_shape='spline',line_width=2.0,name='&#968;<sub>{0:d}</sub>'.format(n),hoverinfo='name',fill='tonexty',line_color=ColorWay[n]))
        
    fig.update_layout(template='plotly_white',margin={'t': 0, 'l': 0, 'r': 0, 'b': 0},hovermode='closest',autosize=True,legend=dict(orientation='h',yanchor='middle',y=1.0,xanchor='center',x=0.5,bgcolor="rgba(0,0,0,0)",font=dict(size=12)),paper_bgcolor='rgba(0,0,0,0)',plot_bgcolor='rgba(0,0,0,0)',xaxis=dict(title='x',tickformat = 'd',showgrid=False,showline=True,linewidth=2,linecolor='black',ticks="outside",tickwidth=2,ticklen=6,title_font=dict(size=12),tickfont=dict(size=10),showticklabels=False,range=[0,L]),yaxis=dict(tickformat = 'd',showgrid=False,showline=True,linewidth=2,linecolor='black',anchor='free',position=0.0,ticks="outside",tickwidth=2,ticklen=0,title_font=dict(size=12),tickfont=dict(size=10),showticklabels=False,range=[0,0.6]),showlegend=False) 
    fig.add_vline(x=5.0, line_width=3, line_color="black")
    fig.add_vline(x=0.0, line_width=3, line_color="black")
    return fig

    
if __name__ == '__main__':
    app.run_server(debug=False)

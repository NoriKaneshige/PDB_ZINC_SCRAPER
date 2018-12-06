"""for plotly,dash"""
import plotly
plotly.tools.set_credentials_file(username='nori-kaneshige', api_key='0fNsdJGLmxNwbfBL0l8f')
import plotly.plotly as py
import plotly.graph_objs as go
#mapbox_access_token = 'pk.eyJ1Ijoibm9yaS1rYW5lc2hpZ2UiLCJhIjoiY2pvbmJ1ZnB6MWE1ZjN2bnZ5ZXFpYzUzNSJ9.3wRYA_HNrpFi9tw1OullOg'
"""this is the end of setting for plotly"""

import numpy as np

#x, y, z = np.random.multivariate_normal(np.array([300,50,3]), np.eye(3), 400).transpose()
#x,y,z = [450,60,3],[389,70,5],[350,45,2]
x,y,z = [450,389,350],[60,70,45],[3,2,2]

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color=z,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.6
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='3d-scatter-colorscale')

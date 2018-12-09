"""for plotly,dash"""
import plotly
plotly.tools.set_credentials_file(username='nori-kaneshige', api_key='0fNsdJGLmxNwbfBL0l8f')
import plotly.plotly as py
import plotly.graph_objs as go
#mapbox_access_token = 'pk.eyJ1Ijoibm9yaS1rYW5lc2hpZ2UiLCJhIjoiY2pvbmJ1ZnB6MWE1ZjN2bnZ5ZXFpYzUzNSJ9.3wRYA_HNrpFi9tw1OullOg'
"""this is the end of setting for plotly"""

import numpy as np
from final_project_functions_for_compounds import *

#x, y, z = np.random.multivariate_normal(np.array([300,50,3]), np.eye(3), 400).transpose()
#x,y,z = [450,60,3],[389,70,5],[350,45,2]
x,y,z,info= [float(el.mw) for el in get_data_from_each_zinc_page(1)],[int(el.tpsa) for el in get_data_from_each_zinc_page(1)],[float(el.logp) for el in get_data_from_each_zinc_page(1)],[el.structure for el in get_data_from_each_zinc_page(1)]

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    hovertext=info,
    mode='markers',
    marker=dict(
        size=12,
        color=y,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.6
    )
)

data = [trace1]
# layout = go.Layout(
#     margin=dict(
#         l=0,
#         r=0,
#         b=0,
#         t=0
#     )
# )
# fig = go.Figure(data=data, layout=layout)

layout = go.Layout(
                    scene = dict(
                    xaxis = dict(
                        title='Molecular Weight'),
                    yaxis = dict(
                        title='Polar Surface Area'),
                    zaxis = dict(
                        title='LogP'),),
                    width=700,
                    margin=dict(
                    r=20, b=10,
                    l=10, t=10)
                  )
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='SI508_final_project')
#plot_url = py.plot(fig, filename='SI508_final_project')
print('Please go to plotly site to see the visual!')

"""for plotly,dash"""
import plotly
plotly.tools.set_credentials_file(username='nori-kaneshige', api_key='0fNsdJGLmxNwbfBL0l8f')
import plotly.plotly as py
import plotly.graph_objs as go
"""Setting numpy"""
import numpy as np
from final_project_functions_for_compounds import *
"""Setting webbrowser"""
import webbrowser


def plot_compounds_plotly(compound_inst_lst_for_visual):
    x,y,z,info= [float(el.mw) for el in compound_inst_lst_for_visual],[int(el.tpsa) for el in compound_inst_lst_for_visual],[float(el.logp) for el in compound_inst_lst_for_visual],[el.structure for el in compound_inst_lst_for_visual]

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
#py.iplot(fig, filename='SI508_final_project')
    plot_url = py.plot(fig, filename='SI508_final_project')
    #print('Please go to plotly site to see the visual!')
    pass
#plot_compounds_plotly(get_data_from_each_zinc_page(1))

"""open zinc site"""
def open_zinc_site(zinc_code_input):
    base_url = "http://zinc15.docking.org/substances/search/?q="
    unique_url = base_url+str(zinc_code_input)
    webbrowser.open(unique_url)

"""open pdb site"""
def open_pdb_site(pdb_id_input):
    base_url = "http://www.rcsb.org/structure/"
    unique_url = base_url+str(pdb_id_input)
    webbrowser.open(unique_url)

# open_zinc_site('zinc76')
# open_pdb_site('5Y64')

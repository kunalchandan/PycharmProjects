import plotly
from plotly.graph_objs import Layout, Scatter
import numpy as np

int_list = []
with open('input.txt') as f:
    for line in f:
        int_list.append([int(i) for i in line.split()])

arr = np.array(int_list)
print(arr)

plotly.offline.plot({
    "data": [Scatter(x = arr[:,0], y = arr[:,1])],
    "layout": Layout(title="Scatter of X and Y Values")
})


f.close()
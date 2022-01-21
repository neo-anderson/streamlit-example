from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
import sys
from time import time

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

import platform
print(platform.processor())
print(platform.architecture())
print(platform.machine())
print(platform.node())
print(platform.system())
print(platform.dist())

print("Processors:")
with open("/proc/cpuinfo", "r")  as f:
    info = f.readlines()

cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
for index, item in enumerate(cpuinfo):
    print("    " + str(index) + ": " + item)

print("Memory Info: ")
with open("/proc/meminfo", "r") as f:
    lines = f.readlines()
print("     " + lines[0].strip())
print("     " + lines[1].strip())

n = 10000
m = 4000
np.random.seed(100)
a = np.random.random((n,m))
b = np.random.random((n,m))
start = time()
adotb = a.dot(b.T)
meanval = adotb.mean()
print(time() - start)
print(meanval)
sys.stdout.flush()
st.text(f"Mean value is {meanval}. It took {time()-start} seconds to calculate this.")

with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))

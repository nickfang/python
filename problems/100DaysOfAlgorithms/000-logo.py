#!python3

import numpy as np
from bokeh.plotting import figure, show, output_notebook

xs, ys, cs = [], [], []

for x in range(0, 30):
   for y in range(0, 30):
      up = np.random.randint(0, 2)
      xs.append([x, x + .8])
      ys.append([y + .8 * (up >= .5), y + .8 * (up < .5)])

      col = np.random.randint(0, 4)
      cs.append({0: 'blue', 1: 'red', 2: 'white', 3: 'white'}[col])

output_notebook()
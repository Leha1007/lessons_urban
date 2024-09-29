import time
from typing import List, Any

import matplotlib.pyplot as plt
from math import sin, cos, pi
import numpy as np


def coordinates_beginner():
    set_abscisses = []
    set_ordinates = []
    x = -1
    for _ in range(200):
        set_abscisses += [x] * 2
        set_ordinates += [1 - abs(x), abs(x) - 1]
        x += 0.01

    return set_abscisses, set_ordinates


def rotation_matrix(list_x, list_y, alpha):
    x_new = []
    y_new = []
    for i in range(len(list_x)):
        x_new.append(list_x[i] * cos(alpha) + list_y[i] * sin(alpha))
        y_new.append(-list_x[i] * sin(alpha) + list_y[i] * cos(alpha))
    return x_new, y_new


x, y = coordinates_beginner()
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-')
for phase in np.linspace(0, 10*np.pi, 500):
    x_new, y_new = rotation_matrix(x, y, phase)
    line1.set_xdata(x_new)
    line1.set_ydata(y_new)
    fig.canvas.draw()
    fig.canvas.flush_events()


# Author: Damian Archer
# Course: Machine Learning COS 575
# Date: 9-6-23
# Assignment: Lab 1 data_visualization.py
import numpy as np
import matplotlib.pylab as plt


# example pulled from numpy sin function use documentation
x = np.linspace(-np.pi, np.pi, 201)

plt.plot(x, np.sin(x))

plt.xlabel('Angle [rad]')

plt.ylabel('sin(x)')

plt.axis('tight')

plt.show()
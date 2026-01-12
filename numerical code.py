import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.interpolate import UnivariateSpline

np.random.seed(42)

x = np.linspace(0, 4 * np.pi, 200)
dx = x[1] - x[0]
y_clean = np.sin(x) + 0.5* np.cos(2 * x)

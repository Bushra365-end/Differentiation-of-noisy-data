import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
from scipy.interpolate import UnivariateSpline

np.random.seed(42)

x = np.linspace(0, 4 * np.pi, 200)
dx = x[1] - x[0]
y_clean = np.sin(x) + 0.5* np.cos(2 * x)
dy_clean = np.cos(x) - np.sin(2 * x)
noise_level = 0.15
noise = np.random.normal(0, noise_level, size=len(x))
y_noisy = y_clean + noise
dy_noisy  = np.gradient(y_noisy, dx)

window_length  =31
poly_order  = 3


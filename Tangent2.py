import matplotlib.pyplot as plt
import numpy as np
# from piscale import *


def format_func2(value, tick_number):
    # find number of multiples of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0:
        return "0"
    elif N == 1:
        return r"$\pi/2$"
    elif N == -1:
        return r"$-\pi/2$"
    elif N == 2:
        return r"$\pi$"
    elif N == -2:
        return r"$-\pi$"
    elif N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    else:
        return r"${0}\pi$".format(N // 2)


# Plot a sine and cosine curve
fig, ax = plt.subplots()
# x = np.linspace(-2*np.pi, 2*np.pi, 1000)
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)
y[np.abs(np.cos(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where sin(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
ax.plot(x, y, lw=2, color="blue", label='tangent')
# ax.plot(x, np.cos(x), lw=2, label='Cosine')
# threshold = 10000
# y[y>threshold] = np.inf
# y[y<-threshold] = np.inf
# ax.plot(x, yy, linewidth=1.2, color="black")
# y[np.abs(np.cos(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# y = 1/np.tan(x)
# y[np.abs(np.sin(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where sin(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
#
# Set up grid, legend, and limits
ax.grid(True)
ax.legend(frameon=False)
# ax.axis('equal')
ax.set_xlim(-2 * np.pi, 2 * np.pi)
ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 4))
# fig


ax.xaxis.set_major_formatter(plt.FuncFormatter(format_func2))
fig
plt.show()
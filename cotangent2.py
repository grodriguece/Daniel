import matplotlib.pyplot as plt
import numpy as np
from matplot_fmt_pi import MultiplePi

fig, ax = plt.subplots()
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = 1/np.tan(x)
y[np.abs(np.sin(x)) <= np.abs(np.sin(x[1]-x[0]))] = np.nan
# This operation inserts a NaN where cos(x) is reaching 0
# NaN means "Not a Number" and NaNs are not plotted or connected
ax.plot(x, y, lw=2, color="blue", label='Cotangent')
# Set up grid, legend, and limits
ax.grid(True)
ax.axhline(0, color='black', lw=.75)
ax.axvline(0, color='black', lw=.75)
ax.set_title("Trigonometric Functions")
ax.legend(frameon=False)
ax.set_xlim(-2 * np.pi, 2 * np.pi)
pi_manager = MultiplePi(8)
ax.xaxis.set_major_locator(pi_manager.locator())
ax.xaxis.set_major_formatter(pi_manager.formatter())
plt.ylim(top=10)  # y axis limit values
plt.ylim(bottom=-10)
y_ticks = np.arange(-10, 10, 1)
plt.yticks(y_ticks)
fig
plt.show()

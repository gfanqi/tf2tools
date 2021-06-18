import numpy as np
from mayavi import mlab
from mayavi.tools.decorations import outline, title, axes, colorbar
from mayavi.tools.helper_functions import points3d, plot3d

n_mer, n_long = 6, 11
dphi = np.pi / 1000.0
phi = np.arange(0.0, 2 * np.pi + 0.5 * dphi, dphi, 'd')
mu = phi * n_mer
x = np.cos(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
y = np.sin(mu) * (1 + np.cos(n_long * mu / n_mer) * 0.5)
z = np.sin(n_long * mu / n_mer) * 0.5

pl = plot3d(x, y, z, np.sin(mu), tube_radius=0.05, colormap='Spectral')

colorbar(orientation='vertical')

t = np.linspace(0, 4 * np.pi, 100)
x = np.sin(2 * t)
y = np.cos(t)
z = np.sin(2 * t)
s = np.sin(t)

pts = points3d(x, y, z, s, colormap="YlGnBu", scale_factor=0.1,
               extent=(-0.3, 0.3, -0.3, 0.3, -0.2, 0.2))

axes(xlabel='X', ylabel='Y', zlabel='Z')
outline(pl)

title('Mayavi rocks', height=0.85)
mlab.show()
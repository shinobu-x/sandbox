import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import Symbol, var, init_printing
from sympy.matrices import Matrix

d0 =  [199,  21, 133] # MediumVioletRed
d1 =  [220,  20,  60] # Crimson
d2 =  [255,  99,  71] # Tomato
d3 =  [255, 218, 185] # PeachPuff
d4 =  [255, 228, 181] # Moccasin
d5 =  [ 34, 139,  34] # ForestGreen
d6 =  [  0, 255, 255] # Aqua
d7 =  [ 30, 144, 255] # DodgerBlue
d8 =  [135, 206, 235] # SkyBlue
d9 =  [ 47,  79,  79] # DarkSlateGray
d10 = [245, 255, 250] # MintCream
d11 = [253, 245, 230] # OldLace
d12 = [255, 228, 225] # MistyRose
d13 = [218, 112, 214] # Orchid
d14 = [138,  43, 226] # VlueViolet
d15 = [ 75,   0, 130] # Indigo                                                                                                      
colors_list = [[d0],[d1],[d2],[d3],[d4],[d5],[d6],[d7],[d8],[d9],[d10],[d11],[d12],[d13],[d14],[d15]]

def coordination_2d(axes, range_x, range_y, grid = True,
               xyline = True, xlabel = "x", ylabel = "y"):
    axes.set_xlabel(xlabel, fontsize = 16)
    axes.set_ylabel(ylabel, fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    if grid == True:
        axes.grid()
    if xyline == True:
        axes.axhline(0.5, color = "black")
        axes.axvline(0.5, color = "black")

def coordination_3d(axes, range_x, range_y, range_z, grid = True):
    axes.set_xlabel("x", fontsize = 16)
    axes.set_ylabel("y", fontsize = 16)
    axes.set_zlabel("z", fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    axes.set_zlim(range_z[0], range_z[1])
    if grid == True:
        axes.grid()

def visualization_2d(axes, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1],
              vector[0], vector[1], color = color,
              angles = 'xy', scale_units = 'xy', scale = 1)

def visualization_3d(axes, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1], loc[2],
              vector[0], vector[1], vector[2],
              color = color, length = 1,
              arrow_length_ratio = 0.2)

def pointer(axes, x, y, text, angle = 45,
            textsize = 12, textcolor = "black", pad = 0.2,
            psize = None, pcolor = None, marker = None,
            cmap = None, norm = None, alpha = None,
            linewidths = None, edgecolors = None):
    axes.scatter(x, y, s = psize, c = pcolor,
                 marker = marker, cmap = cmap, norm = norm,
                 alpha = alpha, linewidths = linewidths,
                 edgecolors = edgecolors)
    text_angle = angle * math.pi / 180
    loc_x = x + pad * math.cos(text_angle)
    loc_y = y + pad * math.sin(text_angle)
    axes.text(loc_x, loc_y, text,
              fontsize = textsize, color = textcolor)
init_printing()

def general_matrix(m, n, s):
    Symbol(s)
    elements = lambda i, j : var('{}{}{}'.format(s, i+1, j+1))
    return Matrix(m, n, elements)

def rotation(u, t, deg=False):
    if deg == True:
        t = np.deg2rad(t)
    R = np.array([[np.cos(t), -np.sin(t)],
                  [np.sin(t),  np.cos(t)]])
    return  np.dot(R, u)

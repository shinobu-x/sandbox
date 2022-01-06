import numpy as np
import matplotlib.pyplot as plt

d0 =  [199,  21, 133] # MediumVioletRed
d1 =  [220,  20,  60] # Crimson
d2 =  [255,  99,  71] # Tomato
d3 =  [255, 218, 185] # PeachPuff
d4 =  [255, 228, 181] # Moccasin
d5 =  [ 34, 139,  34] # ForestGreen
d6 =  [  0, 255, 255] # Aua
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

def coordination_2d(axes, range_x, range_y, grid = True, xyline = True,
                    xlabel = "x", ylabel = "y"):
    axes.set_xlabel(xlabel, fontsize = 16)
    axes.set_ylabel(ylabel, fontsize = 16)
    axes.set_xlim(range_x[0], range_x[1])
    axes.set_ylim(range_y[0], range_y[1])
    if grid == True:
        axes.grid()
    if xyline == True:
        axes.axhline(0, linewidth=0.1, color = "gray")
        axes.axvline(0, linewidth=0.1, color = "gray")

def visualization_2d(axes, loc, vector, color = "red"):
    axes.quiver(loc[0], loc[1],
              vector[0], vector[1], color = color,
              angles = 'xy', scale_units = 'xy', scale = 1)

def rotation(unit_vector, transformation, use_radian=False):
    transformation = np.deg2rad(transformation) if use_radian==True \
        else transformation
    cos = np.cos(transformation)
    sin = np.sin(transformation)
    rotation_matrix = np.array([[cos,-sin],
                                [sin,cos]])
    transformed_matrix = np.dot(rotation_matrix,unit_vector)
    return  transformed_matrix

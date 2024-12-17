import sympy as sp

import sympy as sp
import math
import sympy as sp

import sympy as sp

import sympy as sp

import math

def solution():
    # Coordinates of the first point (x2, y2, z2)
    x2, y2, z2 = 5, 8, -3
    
    # Coordinates of the second point (x3, y3, z3)
    x3, y3, z3 = 2, -1, 4

    # Define the midpoint coordinates of the line segment between point (x2, y2, z2) and point (x3, y3, z3)
    mx, my, mz = (x2 + x3) / 2, (y2 + y3) / 2, (z2 + z3) / 2

    # Define another midpoint (mx1, my1, mz1) between (x1, y1, z1) and the new midpoint (mx, my, mz)
    mx1, my1, mz1 = (mx + x2) / 2, (my + y2) / 2, (mz + z2) / 2

    # Calculate the distance between (x2, y2, z2) and (x3, y3, z3) using the distance formula
    distance_between_points = math.sqrt((x3 - x2)**2 + (y3 - y2)**2 + (z3 - z2)**2)
    
    # Calculate the distance between the two midpoints (mx1, my1, mz1) and (mx, my, mz)
    distance_between_midpoints = math.sqrt((mx - mx1)**2 + (my - my1)**2 + (mz - mz1)**2)

    # Combine both distances as the new result to create a more complex solution
    result = distance_between_points + distance_between_midpoints
    return result




print(solution())




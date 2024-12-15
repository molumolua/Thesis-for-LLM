import sympy as sp

import sympy as sp
import math
def solution():
    # Given values
    focus_y = 6  # y-coordinate of the focus
    vertex_y = -3  # y-coordinate of the vertex

    # Intermediate step: Calculate k (center's y-coordinate) as the midpoint of focus_y and vertex_y
    k = (focus_y + vertex_y) / 2

    # Distance from center to focus (c) and center to vertex (a)
    c = abs(focus_y - k)
    a = abs(vertex_y - k)

    # For a hyperbola, c^2 = a^2 + b^2
    b_squared = c**2 - a**2
    b = math.sqrt(b_squared)

    # Calculate the sum h + k + a + b
    h = 2  # center's x-coordinate
    result = h + k + a + b
    return result



print(solution())




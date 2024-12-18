import sympy as sp

import sympy as sp
import math
import sympy as sp

import sympy as sp

import sympy as sp

import math

import math
def solution():
    # Conversion factor from kilograms to pounds
    kg_to_pound = 1 / 0.4536
    
    # Weight of the steer in kilograms
    steer_weight_kg = 200
    
    # Convert the weight to pounds
    steer_weight_pounds = steer_weight_kg * kg_to_pound
    
    # Round to the nearest whole pound
    rounded_weight = round(steer_weight_pounds)
    
    # Additional step: calculate the approximate feed cost based on weight
    feed_cost_per_pound = 0.12  # cost per pound of steer weight for feed
    total_feed_cost = rounded_weight * feed_cost_per_pound
    
    # Final result: rounded weight and feed cost
    result = (rounded_weight, total_feed_cost)
    
    return result

print(solution())




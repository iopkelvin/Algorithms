# Uses python3
import sys
import numpy as np

def get_optimal_value(capacity, weights, values):
    value = 0 #starts value count of looting
    prop = [x/y for x,y in zip(values, weights)] #Finds best value per weight  (vpw)
    for i in range(len(weights)): #goes over all weights available
        if capacity == 0: #Returns value, once capacity reaches 0
            return value
            break
        valuable = max(prop) #selects the highest value per weight (vpw)
        index = prop.index(valuable) #Locates index of the highest (vpw)
        prop[index] = -1 #Deletes best vpw so that it is not counted again
        weight_to_add = weights[index] #Selects weight based on index of best (vpw)
        minimum = min(weight_to_add, capacity) #Makes sure capacity does not go to zero
        value += minimum * valuable #Chooses value to add based on the minimum value and weight
        weights[index] -= minimum #Takes out weight to be added from weights
        capacity -= minimum #takes out capacity to be added from capacity
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

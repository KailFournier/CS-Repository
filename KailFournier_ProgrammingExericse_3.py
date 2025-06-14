

from functools import reduce #Imports reduce from functools

#User inputs requested cost data
costs = [float(x) for x in input("Enter costs separated by spaces: ").split()]
# Initializes accumulator for results
initial = {'sum': 0, 'max': float('-inf'), 'min': float('inf')}


# Custom reduction function using a dictionary
def cost_processor(acc, x):
    return {
        'sum': acc['sum'] + x, #Adds all costs together
        'max': max(acc['max'], x), #Returns the highest cost
        'min': min(acc['min'], x) #Returns the lowest cost
    }

#Calls cost processor and passes it values
result = reduce(cost_processor, costs, initial)

# Display results
print(f"Total (Sum): {result['sum']}")  # Output: Total (Sum)
print(f"Highest (Max): {result['max']}")  # Output: Highest (Max)
print(f"Lowest (Min): {result['min']}")  # Output: Lowest (Min)
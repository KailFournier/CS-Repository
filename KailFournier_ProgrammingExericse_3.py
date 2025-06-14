

from functools import reduce #Imports reduce from functools

#User inputs requested cost data
costs_input = input("Enter costs and their sources separated by spaces and commas: ")
# Initializes accumulator and dictionary
initial = {'sum': 0, 'max': float('-inf'), 'min': float('inf'), 'max_cost': '', 'min_cost': ''}

#Functions
def cost_assembler(ui): #Assembles the user input costs into a dictionary for the program to use
    cost = ui.split(',') #Splits the input by commas
    costs_dict = {}
    for pair in cost:
        word, number = pair.strip().split() #splits the input again by spaces
        costs_dict[word] = float(number) #turns each pair into a key and a value
    return costs_dict

# Processes the costs and the records
def cost_processor(acc, item):
    word, number = item
    return {
        'sum': acc['sum'] + number, #Adds all costs together
        'max': max(acc['max'], number), #Returns the highest cost
        'min': min(acc['min'], number), #Returns the lowest cost
        'max_cost': word if number > acc['max'] else acc['max_cost'], #Records the highest cost item
        'min_cost': word if number < acc['min'] else acc['min_cost'] #records the lowest cost item
    }

# Displays the results
def show_results(r):
    print(f"Total cost: {r['sum']}")
    print(f"Highest cost: {r['max_cost']} {r['max']}")
    print(f"Lowest: {r['min_cost']} {r['min']}")

def main(): #the main use of the program, contained in a function
    try: #error handling
        costs_dict = cost_assembler(costs_input)  #creates the costs_dict dictionary
        if not costs_dict:
            raise ValueError("No valid input provided.") #error handling
        result = reduce(cost_processor, costs_dict.items(), initial)  #calls the various functions and passes them data
        show_results(result)  #calls the results function and passes it data
    except ValueError as e:
        print(f"Error: Invalid input format. {e}")  #error handling
    except Exception as e:
        print(f"Error: {e}") #error handling

main() #calls the main function
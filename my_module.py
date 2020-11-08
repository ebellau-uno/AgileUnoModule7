'''
Eugene Bellau
11/7/2020
my_module
'''

# pip install prettyprint "This will install the pretty print package and will need to be ran in the terminal"

import json # This command will import the json module which will cause serialization and deserialization.


# This will define the variable and return a string
def greeting(name): 
    return(f"Hello {name}")


'''
This will define the variable and pass named arguments to the function using kwargs and use an if/else statement to return a string whether  the correct parameters are supplied
kwargs allow the passing of an unspecified number of arguments to  a function
'''
def letter_text(**kwargs):
    if "name" and "amount" and "denomination" in kwargs.keys():
        return(f"Hello {kwargs['name']}, this letter is to inform you that you have won {kwargs['amount']} {kwargs['denomination']}")
    else:
        return("incorrect parameters supplied")


my_json_data = {} # This is a dictonary to store the data from the JSON file

with open("input.json", "r") as input: # This will open the JSON file with read permissions
    my_json_data = json.load(input) # This will store the data from the JSON file into the dictonary
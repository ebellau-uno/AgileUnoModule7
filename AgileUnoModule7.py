'''
Eugene Bellau
11/6/2020
AgileUnoModule7
'''


# 1. import my_module and the pretty print module
import pprint

import my_module

# 2. Use the gretting method from my_module to print out your name
greet = my_module.greeting("Eugene")
print(greet)


# 3. Use the letter_text module to print out a string
letter = my_module.letter_text(name="Sam", amount="10,000", denomination="dollars")
print(letter)

# 4. Use the my_module.my_json.data and print it out
from my_module import my_json_data

print(my_json_data)


# 5. Import the my_json_data as my_data and print out the my_data using pretty print
from my_module import my_json_data as my_data

pprint.pprint(my_json_data)


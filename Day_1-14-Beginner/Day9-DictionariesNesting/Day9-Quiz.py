"""
Which line of code will change the starting_dictionary to the final_dictionary?
"""

starting_dictionary = {
    "a": 9,
    "b": 8,
}


final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

# starting_dictionary["c"] = 7
# final_dictionary = starting_dictionary


"""Which line of code will produce an error?
"""
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}

# dict["c"] = [1, 2, 3]

# for key in dict:
#     dict[key] += 1

# dict[1] = 4

"""
There is no key that matches 1, this will give you a KeyError. Unlike with a Python List, using the [1] square bracket notation on a dictionary will *not* retrieve the second item. 
"""
# print(dict[1])


# Which line of code will print "Steak"?

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}

print(order["main"][2][0])

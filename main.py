# Data Structures - A data structure is a way of organizing and storing data in Python.

# Lists are a data structure that can be used to store many pieces of related data.

fruits = ["apple", "banana", "cherry"]

states = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee"]

states.append("Puerto Rico")
states.extend(["Bunkland, Skunkland, Banjo Town"])

# For length, pass the list as an argument to the len() function.
# Unlike JavaScript, where you just do .length()

print(len(states))
print(states[len(states) - 1])

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
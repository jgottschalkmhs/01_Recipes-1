import csv

# open file
groceries = open('01_ingredients_ml_to_g.csv')

# Read data into a list
csv_groceries = csv.reader(groceries)

# create a dictionary to hold the data
food_dictionary = {}

# Add the data from the list into the dictionary
# (first item in row is key ,next is definition)

for row in csv_groceries:
    food_dictionary[row[0]]= row[1]

print(food_dictionary)

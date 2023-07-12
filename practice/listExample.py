# List
# - an object that can contain one or more elements
# - dynamic structures, we can add or remove elements from them
# - mutable, we can change the values of the elements
# - ordered collections and can have duplicate elements
import random

name_list = ["Bubbles", "Rocco", "Daisy"]
numbers_list = [8, 9, 10, 11, 12]
print(name_list)
print(numbers_list)

print(name_list[1])
print(numbers_list[0])

print(name_list[0] + " was born on: " + str(numbers_list[0]) + "." + str(numbers_list[1]))

list_OfLists = [["Summer", "Winter"], ["White", "Black"], ["Sunrise", "Sunset"]]
list_OfFruits = [
    ["apple", 10],
    ["kiwi", 10],
    ["watermelon", 2],
    ["strawberry", 15],
    ["orange", 10],
    ["banana", 10],
    ["mango", 8],
    ["grapefruit", 6],
    ["pear", 12],
    ["blueberry", 20]]
print(list_OfFruits)

print(list_OfFruits[0])
watermelon_List = list_OfFruits[2]
print(watermelon_List)
print(watermelon_List[0])

print(list_OfFruits[0][0])
print(list_OfFruits[4][0])

print("The price of " + list_OfFruits[7][0] + " is " + str(list_OfFruits[7][1]) + ".")

list_OfFruits.append(["pear", 12])
list_OfFruits.append(["blueberry", 20])
print(list_OfFruits)
print()
# --------------------------------------------------------------------


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list)
random.shuffle(list)
print(list)

# Type Casting - converting a data type

# The purpose is to help us use data in multiple operations, not just those dedicated to a single
# data type.

text = 'Python'
textStr = "Hello world"
numberInt = 10
numberFlo = 5.8

# print(type(text))
# print(type(textStr))
# print(type(numberInt))

# -----------------------------------------------------------------------
# str() function

print(type(numberInt))
numberInt = str(numberInt)
print(type(numberInt))
print()

print(type(numberFlo))
numberFlo = str(numberFlo)
print(type(numberFlo))
print()

# also
numberStr = str(numberInt)
print(type(numberStr))
print()

# # Concatenation: string + numeric type
text1 = "In the summer, the sun rises at"
hour = 5
text2 = "AM"

# Error
# print(text1 + hour + text2)

# Works
print(text1 + " " + str(hour) + " " + text2)
print()

# -----------------------------------------------------------------------
# int() function - works only if we have digits, not letter

text = "30"
print(type(text))
text = int(text)
print(type(text))
print()

textFlo = "5.8"
print(type(textFlo))
textFlo = float(textFlo)
print(type(textFlo))

number = "25"
# print(number + 10)  --> error
print(int(number) + 10)
# -----------------------------------------------------------------------


# Homework
# Requesting user's name and age
# Calculating and informing the user how many years they have left until they turn 100 years old.

print(">> Enter your name << ")
name = input("Name: ")
print(">> Enter your age << ")
age = input("Age: ")

print("Your name is " + name + " and your age is " + age + ".")
print("You have " + str(100 - int(age)) + " years left until you turn 100 years old. ")
print()

# or
years_left = 100 - int(age)
years_left_str = str(years_left)
print("You have " + years_left_str + " years left until you turn 100 years old.")
print()

# Or, we can perform the conversion first
age_int = int(age)
result = 100 - age_int
result_str = str(result)

print("You have " + result_str + " years left until you turn 100 years old.")
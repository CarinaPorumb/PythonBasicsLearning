# Concatenation: using the + operator and form a sentence

text1 = "Vibrant summer vibes"
text2 = "serene ocean waves"
concatenated = text1 + " and " + text2 + " make for a perfect summer experience."

print(text1 + " and " + text2)
print()
print(concatenated)

# Alternatively, you can use the join() method of strings
result2 = " ".join([text1, "and", text2, "make for a perfect summer experience."])
print("Concatenated (using join() method):", result2)
print()

# Multiplication

text4 = """
Hello, world!"""
print(text4 * 10)
print()

# number1 = 5
# number2 = 3
# print(5 + 3 + text2)
# print(text2 + 5 + 3)
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# Methods
upperText = text1.upper()
print(upperText)
lowerText = text1.lower()
print(lowerText)

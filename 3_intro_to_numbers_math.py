"""
Lesson 3: Numbers and Math

Learning goals:
- Work with integers and floats.
- Use arithmetic operators in Python.
- Understand order of operations.
- Apply helpful math functions in real examples.
"""

print("Welcome to Lesson 3: Numbers and Math")

items = 7            # int
price = 3.5          # float
total = items * price
print("Items:", items)
print("Price each:", price)
print("Total:", total)

# Arithmetic operators
a = 10
b = 3
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)      # regular division
print("a // b =", a // b)    # floor division
print("a % b =", a % b)      # remainder
print("a ** b =", a ** b)    # exponent

# Order of operations: parentheses first.
without_parentheses = 2 + 3 * 4
with_parentheses = (2 + 3) * 4
print("2 + 3 * 4 =", without_parentheses)
print("(2 + 3) * 4 =", with_parentheses)

# Useful built-in helpers.
numbers = [2.2, 9.1, 4.8, 1.5]
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Rounded 4.8:", round(4.8))
print("Absolute value of -12:", abs(-12))

print("\n--- Practice ---")
print("1) Create two variables and print all arithmetic operations.")
print("2) Calculate the area of a rectangle using width * height.")
print("3) Try one expression with and without parentheses and compare.")

print("\n--- Questions (short answer) ---")
print("Q1: What is the difference between / and // ?")
print("Q2: What does the % operator return?")
print("Q3: Why do parentheses matter in math expressions?")
print("Q4: Name one built-in function that helps with numbers.")

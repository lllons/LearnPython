"""
Lesson 3: Numbers and Math

Learning goals:
- Work with integers and floats.
- Use arithmetic operators in Python.
- Understand order of operations.
- Apply helpful math functions in real examples.
"""

print("Welcome to Lesson 3: Numbers and Math")

# int is for whole numbers (like item counts).
items = 7            # int
# float is for numbers with decimals (like money, measurements, ratings).
price = 3.5          # float
# Multiply quantity by price to get a total (common in shopping/billing apps).
total = items * price
print("Items:", items)
print("Price each:", price)
print("Total:", total)

# Arithmetic operators
# Use small variables to focus on the operators themselves.
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
# Without parentheses, multiplication happens before addition.
without_parentheses = 2 + 3 * 4
# With parentheses, 2 + 3 happens first, then result is multiplied by 4.
with_parentheses = (2 + 3) * 4
print("2 + 3 * 4 =", without_parentheses)
print("(2 + 3) * 4 =", with_parentheses)

# Useful built-in helpers.
# Lists can hold many numbers that you want to analyze together.
numbers = [2.2, 9.1, 4.8, 1.5]
# min()/max() are useful in reports: lowest/highest score, cheapest/most expensive item.
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
# round() helps when you want simpler display values.
print("Rounded 4.8:", round(4.8))
# abs() gives distance from zero; useful for differences and error margins.
print("Absolute value of -12:", abs(-12))

# Practice section: edit numbers and observe output changes.
print("\n--- Practice ---")
print("1) Create two variables and print all arithmetic operations.")
print("2) Calculate the area of a rectangle using width * height.")
print("3) Try one expression with and without parentheses and compare.")

# Questions turn the run output into quick self-checks.
print("\n--- Questions (short answer) ---")
print("Q1: What is the difference between / and // ?")
print("Q2: What does the % operator return?")
print("Q3: Why do parentheses matter in math expressions?")
print("Q4: Name one built-in function that helps with numbers.")

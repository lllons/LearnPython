"""
Lesson 1: Python Basics

Learning goals:
- Understand what Python code looks like.
- Use variables to store simple values.
- Run print statements and basic expressions.
- Read and write beginner-friendly comments.
"""

# Welcome to your first Python lesson script.
# print() shows text in the terminal so you can see what your program is doing.
# In real life, developers print values while learning/debugging.
print("Welcome to Lesson 1: Python Basics")

# Variables store data you can reuse later.
# Think of a variable like a labeled box: name on the left, value inside.
# This matters because most real programs reuse data many times.
name = "Learner"
age = 18
favorite_tool = "Python"

# You can print labels with values to make output easier to read.
print("Name:", name)
print("Age:", age)
print("Favorite tool:", favorite_tool)

# Python is case-sensitive: score and Score are different names.
# This is important in real projects: one wrong capital letter can break code.
score = 10
Score = 25
print("score =", score)
print("Score =", Score)

# You can update variables.
# Here we take the old score, add 5, and store the new value back into score.
# Real-world example: adding points in a game or adding items to a cart total.
score = score + 5
print("Updated score:", score)

# Basic expression examples.
# Concatenation (+) combines text values into one string.
greeting = "Hello, " + name
# Comparison (>=) creates a boolean (True/False), useful for decisions later.
is_adult = age >= 18
print(greeting)
print("Is adult?", is_adult)

# \n creates a blank line before the section title for cleaner output.
print("\n--- Practice ---")
print("1) Change the value of 'name' and run again.")
print("2) Add a new variable called 'city' and print it.")
print("3) Create 'study_hours' and increase it by 2, then print.")

# These questions help check understanding after running the script.
print("\n--- Questions (short answer) ---")
print("Q1: What is a variable?")
print("Q2: Why are score and Score different?")
print("Q3: What does age >= 18 return?")
print("Q4: How do you update a variable value?")

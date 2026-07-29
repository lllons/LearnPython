"""
Lesson 1: Python Basics

Learning goals:
- Understand what Python code looks like.
- Use variables to store simple values.
- Run print statements and basic expressions.
- Read and write beginner-friendly comments.
"""

# Welcome to your first Python lesson script.
print("Welcome to Lesson 1: Python Basics")

# Variables store data you can reuse later.
name = "Learner"
age = 18
favorite_tool = "Python"

print("Name:", name)
print("Age:", age)
print("Favorite tool:", favorite_tool)

# Python is case-sensitive: score and Score are different names.
score = 10
Score = 25
print("score =", score)
print("Score =", Score)

# You can update variables.
score = score + 5
print("Updated score:", score)

# Basic expression examples.
greeting = "Hello, " + name
is_adult = age >= 18
print(greeting)
print("Is adult?", is_adult)

print("\n--- Practice ---")
print("1) Change the value of 'name' and run again.")
print("2) Add a new variable called 'city' and print it.")
print("3) Create 'study_hours' and increase it by 2, then print.")

print("\n--- Questions (short answer) ---")
print("Q1: What is a variable?")
print("Q2: Why are score and Score different?")
print("Q3: What does age >= 18 return?")
print("Q4: How do you update a variable value?")

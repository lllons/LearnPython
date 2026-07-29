"""
Lesson 5: Lists and Tuples

Learning goals:
- Store multiple values in lists and tuples.
- Read, update, and iterate through list items.
- Understand the key difference: mutable vs immutable.
- Use common list operations for real tasks.
"""

print("Welcome to Lesson 5: Lists and Tuples")

# A list is ordered and mutable (changeable).
tools = ["Python", "Git", "VS Code"]
print("Original list:", tools)
print("First item:", tools[0])

tools.append("Terminal")
print("After append:", tools)

tools[1] = "GitHub"
print("After update:", tools)

removed = tools.pop()
print("Removed item:", removed)
print("After pop:", tools)
print("List length:", len(tools))

print("\nLoop through the list:")
for tool in tools:
    print("-", tool)

# A tuple is ordered and immutable (cannot be changed).
rgb_color = (255, 120, 40)
print("\nTuple example:", rgb_color)
print("Red value:", rgb_color[0])

# You can create a new tuple, but not edit an existing item.
updated_rgb_color = (200, rgb_color[1], rgb_color[2])
print("New tuple version:", updated_rgb_color)

print("\n--- Practice ---")
print("1) Create a list of 3 foods and print each one with a loop.")
print("2) Add one food and remove one food, then print the final list.")
print("3) Create a tuple with 3 numbers and print the middle value.")

print("\n--- Questions (short answer) ---")
print("Q1: What is one difference between a list and a tuple?")
print("Q2: Which method adds an item to a list?")
print("Q3: What does pop() do?")
print("Q4: How do you access the first item in a list?")

"""
Lesson 2: Working with Strings

Learning goals:
- Create and print strings.
- Combine strings with concatenation and f-strings.
- Use common string methods for cleanup and checks.
- Access characters using index positions.
"""

print("Welcome to Lesson 2: Strings")

first_name = "Ava"
last_name = "Patel"

# Concatenation joins strings.
full_name_concat = first_name + " " + last_name
print("Concatenation:", full_name_concat)

# f-strings are a clean way to format text.
full_name_f = f"{first_name} {last_name}"
print("f-string:", full_name_f)

message = "  Python is practical and fun.  "
print("Original:", repr(message))
print("Stripped:", repr(message.strip()))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Replace:", message.replace("fun", "powerful"))

word = "coding"
print("First letter:", word[0])
print("Last letter:", word[-1])
print("Length:", len(word))
print("Contains 'din'?", "din" in word)

print("\n--- Practice ---")
print("1) Create a variable called 'hobby' and print a sentence with an f-string.")
print("2) Make a messy string with extra spaces and clean it with .strip().")
print("3) Print the second character of a new word variable.")

print("\n--- Questions (short answer) ---")
print("Q1: What is the difference between concatenation and an f-string?")
print("Q2: What does .strip() do?")
print("Q3: How do you get the last character of a string?")
print("Q4: What does len(word) return?")

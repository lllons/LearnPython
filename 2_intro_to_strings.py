"""
Lesson 2: Working with Strings

Learning goals:
- Create and print strings.
- Combine strings with concatenation and f-strings.
- Use common string methods for cleanup and checks.
- Access characters using index positions.
"""

print("Welcome to Lesson 2: Strings")

# Strings store text data such as names, messages, email subjects, and addresses.
first_name = "Ava"
last_name = "Patel"

# Concatenation joins strings.
# You manually add a space here so the first and last name do not stick together.
full_name_concat = first_name + " " + last_name
print("Concatenation:", full_name_concat)

# f-strings are a clean way to format text.
# f-strings are common in real apps for readable messages and logs.
full_name_f = f"{first_name} {last_name}"
print("f-string:", full_name_f)

# This string has extra spaces on purpose so .strip() has something to remove.
message = "  Python is practical and fun.  "
# repr() shows quotes/spaces clearly, which helps beginners "see" invisible spaces.
print("Original:", repr(message))
# .strip() removes spaces from the start and end (great for cleaning user input).
print("Stripped:", repr(message.strip()))
# .upper() and .lower() are useful for standardizing text before comparisons.
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
# .replace(old, new) swaps text; useful for simple cleanup or templating.
print("Replace:", message.replace("fun", "powerful"))

# Indexing lets you read specific characters from a string.
word = "coding"
# Index 0 means "first character" in Python.
print("First letter:", word[0])
# Negative index -1 means "last character", helpful when checking file extensions.
print("Last letter:", word[-1])
# len() counts characters, often used for validation rules (like password length).
print("Length:", len(word))
# "in" checks whether a substring exists (useful for search/filter checks).
print("Contains 'din'?", "din" in word)

# Practice prompts encourage active learning by editing and rerunning code.
print("\n--- Practice ---")
print("1) Create a variable called 'hobby' and print a sentence with an f-string.")
print("2) Make a messy string with extra spaces and clean it with .strip().")
print("3) Print the second character of a new word variable.")

# Reflection questions reinforce core string concepts.
print("\n--- Questions (short answer) ---")
print("Q1: What is the difference between concatenation and an f-string?")
print("Q2: What does .strip() do?")
print("Q3: How do you get the last character of a string?")
print("Q4: What does len(word) return?")

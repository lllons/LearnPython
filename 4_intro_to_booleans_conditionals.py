"""
Lesson 4: Booleans and Conditionals

Learning goals:
- Understand True and False values.
- Use comparison and logical operators.
- Write if, elif, and else decision blocks.
- Build practical branching examples.
"""

print("Welcome to Lesson 4: Booleans and Conditionals")

# Boolean values are True or False.
# Booleans model yes/no states in real systems (logged in? paid? verified?).
is_logged_in = True
has_paid = False
print("is_logged_in:", is_logged_in)
print("has_paid:", has_paid)

# Comparison operators return booleans.
# This allows programs to "check conditions" before taking actions.
temperature = 22
print("temperature > 20:", temperature > 20)
print("temperature == 22:", temperature == 22)
print("temperature != 18:", temperature != 18)

# Logical operators: and, or, not.
# and: both must be True. Example: user must log in AND subscribe.
can_access_premium = is_logged_in and has_paid
# or: at least one True. Example: show content to logged-in users OR trial users.
can_view_content = is_logged_in or has_paid
print("can_access_premium:", can_access_premium)
print("can_view_content:", can_view_content)
# not flips True/False, useful when blocking an opposite condition.
print("not has_paid:", not has_paid)

# Conditionals choose different code paths based on data.
score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    # elif means "else if": only checked when earlier if condition was False.
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    # else catches every remaining case.
    grade = "D"
print("Score:", score, "Grade:", grade)

age = 16
if age >= 18:
    # Practical use: age checks for permissions or legal requirements.
    print("You can vote in many countries.")
else:
    print("You are not old enough to vote yet.")

# Practice tasks: change values and rerun to watch branches change.
print("\n--- Practice ---")
print("1) Change score and observe the grade result.")
print("2) Create your own if/elif/else for weather advice.")
print("3) Write a condition using and or or with two booleans.")

# Quick review questions strengthen boolean and conditional thinking.
print("\n--- Questions (short answer) ---")
print("Q1: What type of value does a comparison produce?")
print("Q2: When is 'and' True?")
print("Q3: What is the role of 'elif'?")
print("Q4: What does 'not' do to a boolean?")

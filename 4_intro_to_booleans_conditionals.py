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
is_logged_in = True
has_paid = False
print("is_logged_in:", is_logged_in)
print("has_paid:", has_paid)

# Comparison operators return booleans.
temperature = 22
print("temperature > 20:", temperature > 20)
print("temperature == 22:", temperature == 22)
print("temperature != 18:", temperature != 18)

# Logical operators: and, or, not.
can_access_premium = is_logged_in and has_paid
can_view_content = is_logged_in or has_paid
print("can_access_premium:", can_access_premium)
print("can_view_content:", can_view_content)
print("not has_paid:", not has_paid)

score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "D"
print("Score:", score, "Grade:", grade)

age = 16
if age >= 18:
    print("You can vote in many countries.")
else:
    print("You are not old enough to vote yet.")

print("\n--- Practice ---")
print("1) Change score and observe the grade result.")
print("2) Create your own if/elif/else for weather advice.")
print("3) Write a condition using and or or with two booleans.")

print("\n--- Questions (short answer) ---")
print("Q1: What type of value does a comparison produce?")
print("Q2: When is 'and' True?")
print("Q3: What is the role of 'elif'?")
print("Q4: What does 'not' do to a boolean?")

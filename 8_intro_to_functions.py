"""Lesson 8: Functions and reusable code.

Learning goals:
- Define and call functions to avoid repeated code.
- Use parameters and return values.
- Understand default parameters and simple docstrings.
- Build small tools that can be reused in later lessons.
"""


def greet(name):
    """Return a friendly greeting string."""
    return f"Hello, {name}!"


def add_numbers(a, b):
    """Return the sum of two numbers."""
    return a + b


def power(base, exponent=2):
    """Return base raised to exponent (default exponent is 2)."""
    return base ** exponent


def function_examples():
    print("=== Function examples ===")

    print(greet("Mia"))
    print("3 + 5 =", add_numbers(3, 5))

    print("Square of 4:", power(4))
    print("Cube of 4:", power(4, 3))

    # Functions work well with loops.
    names = ["Luca", "Noah", "Aria"]
    for name in names:
        print(greet(name))


def classify_score(score):
    """Return a simple grade label for a numeric score."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "Needs practice"


def mini_task_examples():
    print("\n=== mini task examples ===")

    for score in [95, 83, 71, 60]:
        print(f"Score {score}: {classify_score(score)}")


def practice_section():
    print("\n=== Practice section ===")
    print("1) Write a function called is_even(n) that returns True/False.")
    print("2) Write a function called area_rectangle(width, height).")
    print("3) Write a function called shout(text) with a default suffix='!'.")
    print("4) Call each function with at least two test values.")

    # Starter example:
    # def is_even(n):
    #     return n % 2 == 0


def questions_section():
    print("\n=== Questions ===")
    print("1) Why are functions useful in larger programs?")
    print("2) What is the difference between print and return?")
    print("3) What happens when an argument is omitted but has a default value?")
    print("4) When should you add a short docstring to a function?")


if __name__ == "__main__":
    function_examples()
    mini_task_examples()
    practice_section()
    questions_section()

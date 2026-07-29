"""Lesson 9: Scope and modules.

Learning goals:
- Understand local and global scope.
- Avoid accidental name conflicts.
- Use __name__ == "__main__" for script entry points.
- Import from Python's standard library to build modular programs.
"""

import math
from datetime import date


LANGUAGE = "Python"  # Global variable for this module.
# A global is defined outside functions, so many functions can read it.
# Why this matters: shared constants (tax rates, app names) are common.


def scope_example():
    print("=== Scope example ===")

    topic = "scope"  # Local variable (inside function only).
    # Local variables help prevent accidental changes in other functions.
    # This keeps code easier to debug in larger projects.
    print("Local topic:", topic)
    print("Global language:", LANGUAGE)


def area_circle(radius):
    """Return area of a circle using math.pi."""
    # We import math.pi instead of typing 3.14 manually
    # so calculations are more accurate and readable.
    return math.pi * radius * radius


def module_examples():
    print("\n=== Module examples ===")

    # Modules are ready-made toolboxes.
    # Real-world use: date/time, file handling, random numbers, and more.
    print("Circle area (r=3):", round(area_circle(3), 2))
    print("Square root of 81:", math.sqrt(81))
    print("Today's date:", date.today())


def name_conflict_note():
    print("\n=== Naming note ===")
    # Naming conflicts happen when your variable name matches a module name.
    # Then Python "forgets" the module reference in that scope.
    print("Avoid using names like 'math' for your own variables.")
    print("If you write math = 10, then math.sqrt will break.")


def practice_section():
    print("\n=== Practice section ===")
    print("1) Create a global constant called TAX_RATE = 0.15.")
    print("2) Write calculate_total(price) that uses TAX_RATE.")
    print("3) Import random and print a random integer 1 to 10.")
    print("4) Add your own if __name__ == '__main__' test calls.")

    # Starter code (edit this):
    # This shows using a global constant inside a function.
    # Common business example: applying tax or discount rules app-wide.
    # TAX_RATE = 0.15
    # def calculate_total(price):
    #     return price * (1 + TAX_RATE)


def questions_section():
    print("\n=== Questions ===")
    print("1) What is local scope?")
    print("2) What is global scope?")
    print("3) Why is __name__ == '__main__' useful?")
    print("4) What can go wrong with variable names that match module names?")


if __name__ == "__main__":
    # This block runs only when this file is executed directly.
    # It does NOT run when imported into another file.
    # This is useful for quick tests and examples.
    scope_example()
    module_examples()
    name_conflict_note()
    practice_section()
    questions_section()

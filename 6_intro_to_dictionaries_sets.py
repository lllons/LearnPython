"""Lesson 6: Dictionaries and sets.

Learning goals:
- Store paired data with dictionaries (key -> value).
- Read, add, update, and remove dictionary items.
- Use sets for unique values and simple set operations.
- Connect loops from earlier lessons to dictionary and set data.
"""


def dictionary_examples():
    print("=== Dictionary examples ===")

    # A dictionary maps keys to values.
    student = {"name": "Ava", "age": 13, "grade": "8th"}
    print("Original:", student)

    # Read values by key.
    print("Name:", student["name"])

    # Add or update values.
    student["age"] = 14
    student["city"] = "Wellington"
    print("After updates:", student)

    # Safe read with .get() avoids errors for missing keys.
    print("Favorite color:", student.get("favorite_color", "not set"))

    # Loop through keys and values.
    for key, value in student.items():
        print(f"{key} -> {value}")

    # Remove an item.
    removed = student.pop("city")
    print("Removed city:", removed)
    print("Now:", student)


def set_examples():
    print("\n=== Set examples ===")

    # Sets keep unique values only.
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = set(numbers)
    print("Original list:", numbers)
    print("Unique set:", unique_numbers)

    a = {"apple", "banana", "pear"}
    b = {"banana", "pear", "kiwi"}

    print("Union (all):", a | b)
    print("Intersection (shared):", a & b)
    print("Difference (in a, not b):", a - b)


def practice_section():
    print("\n=== Practice section ===")
    print("1) Create a dictionary called book with keys: title, author, pages.")
    print("2) Add a new key: read (True or False).")
    print("3) Print each key and value using a loop.")
    print("4) Make a set from this list: [3, 3, 5, 7, 7, 9].")
    print("5) Try one set operation between two sets you create.")

    # Starter code (edit this):
    # book = {"title": "Example", "author": "You", "pages": 100}
    # book["read"] = False
    # for k, v in book.items():
    #     print(k, v)


def questions_section():
    print("\n=== Questions ===")
    print("1) What is the main difference between a list and a dictionary?")
    print("2) Why might you use dict.get() instead of dict[key]?")
    print("3) What is special about values stored in a set?")
    print("4) Which set operation finds values shared by two sets?")


if __name__ == "__main__":
    dictionary_examples()
    set_examples()
    practice_section()
    questions_section()

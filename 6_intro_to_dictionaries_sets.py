"""Lesson 6: Dictionaries and sets.

Learning goals:
- Store paired data with dictionaries (key -> value).
- Read, add, update, and remove dictionary items.
- Use sets for unique values and simple set operations.
- Connect loops from earlier lessons to dictionary and set data.
"""


def dictionary_examples():
    print("=== Dictionary examples ===")

    # A dictionary maps keys to values (like labels on a form).
    # Why this matters: real apps store related details together
    # (for example: a user profile with name, age, and email).
    student = {"name": "Ava", "age": 13, "grade": "8th"}
    print("Original:", student)

    # Read values by key when you know the label you want.
    # Real-world example: getting "email" from a customer record.
    print("Name:", student["name"])

    # Add or update values by assigning to a key.
    # You use this when data changes, like a new address or phone number.
    student["age"] = 14
    student["city"] = "Wellington"
    print("After updates:", student)

    # Safe read with .get() avoids errors for missing keys.
    # If the key is missing, we can provide a fallback value.
    # This is useful with incomplete data from files/APIs.
    print("Favorite color:", student.get("favorite_color", "not set"))

    # Loop through keys and values to process every field.
    # Common use: printing reports or validating all inputs.
    for key, value in student.items():
        print(f"{key} -> {value}")

    # Remove an item when you no longer need it.
    # pop() also returns the removed value, which can be logged.
    removed = student.pop("city")
    print("Removed city:", removed)
    print("Now:", student)


def set_examples():
    print("\n=== Set examples ===")

    # Sets keep unique values only.
    # Why this matters: duplicates are common in real data
    # (like repeated IDs, tags, or names from imports).
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = set(numbers)
    print("Original list:", numbers)
    print("Unique set:", unique_numbers)

    # Here we compare two sets of fruit names.
    # Think of this like comparing two shopping lists or two user groups.
    a = {"apple", "banana", "pear"}
    b = {"banana", "pear", "kiwi"}

    # Union: everything in either set (combined list of unique items).
    print("Union (all):", a | b)
    # Intersection: items both sets share (overlap).
    print("Intersection (shared):", a & b)
    # Difference: items only in the first set.
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

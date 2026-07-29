"""Lesson 10: Error handling basics.

Learning goals:
- Understand common runtime errors in Python.
- Use try/except to handle expected problems.
- Use else and finally blocks in a clear way.
- Write safer functions that validate input.
"""


def divide_numbers(a, b):
    """Return a / b, handling division by zero."""
    # try: run code that might fail.
    # Why this matters: real user input is unpredictable.
    try:
        result = a / b
    except ZeroDivisionError:
        # except: handle a specific known error safely.
        # We return None so the rest of the program can continue.
        print("Cannot divide by zero.")
        return None
    else:
        # else runs only if no exception happened in try.
        print("Division successful.")
        return result


def parse_integer(text):
    """Convert text to int, returning None on invalid input."""
    # Converting text to numbers is common with forms and config files.
    try:
        return int(text)
    except ValueError:
        # ValueError means the text wasn't a valid whole number.
        print(f"'{text}' is not a valid integer.")
        return None


def error_examples():
    print("=== Error examples ===")

    # First call succeeds, second call triggers the handled error path.
    print("10 / 2 =", divide_numbers(10, 2))
    print("10 / 0 =", divide_numbers(10, 0))

    # Same idea here: one valid conversion and one invalid conversion.
    print("parse '42' ->", parse_integer("42"))
    print("parse 'hello' ->", parse_integer("hello"))


def finally_example():
    print("\n=== finally example ===")

    file_obj = None
    try:
        # Resource example: files should always be closed after use.
        file_obj = open("lesson10_temp.txt", "w", encoding="utf-8")
        file_obj.write("Temporary lesson file.\n")
        print("Wrote lesson10_temp.txt")
    except OSError as error:
        print("File write failed:", error)
    finally:
        # finally runs whether an error happened or not.
        # This is a safe place for cleanup work.
        if file_obj is not None:
            file_obj.close()
            print("File closed safely.")


def practice_section():
    print("\n=== Practice section ===")
    print("1) Write a function safe_index(items, index).")
    print("   - Return items[index] in try.")
    print("   - Catch IndexError and return None.")
    print("2) Improve parse_integer to strip spaces first.")
    print("3) Add a test that triggers each except block.")

    # Starter code:
    # IndexError is common when users request invalid list positions.
    # Catching it prevents app crashes and allows friendly feedback.
    # def safe_index(items, index):
    #     try:
    #         return items[index]
    #     except IndexError:
    #         return None


def questions_section():
    print("\n=== Questions ===")
    print("1) What is the purpose of try/except?")
    print("2) When does the else block in try/except run?")
    print("3) What is finally used for?")
    print("4) Why is catching specific exceptions better than a bare except?")


if __name__ == "__main__":
    error_examples()
    finally_example()
    practice_section()
    questions_section()

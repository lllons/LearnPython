"""
Lesson 11: Introduction to File I/O

Learning goals:
- Read text from files safely.
- Write and append text to files.
- Understand file modes and context managers.
- Handle common file-related errors.
"""

from pathlib import Path


def example_write_and_read(file_path: Path) -> None:
    """Write text to a file, then read it back."""
    # Real-world use: apps often save logs, settings, reports, or user notes to files.
    # This example shows the full "save data, then load data" workflow.
    print("\nExample 1: write and read")
    # "w" means "write mode": create the file if missing, or replace old content.
    # The with-block auto-closes the file, even if an error happens.
    with file_path.open("w", encoding="utf-8") as file:
        # \n makes each write appear on its own line in the text file.
        file.write("Line 1: Hello, file!\n")
        file.write("Line 2: Learning Python file I/O.\n")

    # "r" means "read mode": open existing file content for reading.
    with file_path.open("r", encoding="utf-8") as file:
        # read() returns one string containing the entire file.
        content = file.read()
    # Printing confirms what was actually stored on disk.
    print(content)


def example_append(file_path: Path) -> None:
    """Append new text without removing existing content."""
    # Why this matters: append mode is useful for adding new logs/history entries.
    print("Example 2: append")
    # "a" means "append mode": keep old content and add new content at the end.
    with file_path.open("a", encoding="utf-8") as file:
        file.write("Line 3: This line was appended.\n")

    # Re-read the file so we can verify all lines are still present.
    with file_path.open("r", encoding="utf-8") as file:
        # enumerate(..., start=1) gives friendly line numbers starting at 1.
        for line_number, line in enumerate(file, start=1):
            # strip() removes trailing newline so output looks clean.
            print(f"{line_number}: {line.strip()}")


def example_error_handling(file_path: Path) -> None:
    """Show a simple try/except pattern for file operations."""
    # In real programs, users may delete/move files, so missing paths are common.
    # try/except lets your program fail gracefully instead of crashing.
    print("\nExample 3: error handling")
    # Build a path in the same folder but with a name that should not exist.
    missing_file = file_path.with_name("does_not_exist.txt")
    try:
        # This line will raise FileNotFoundError if the file is missing.
        with missing_file.open("r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        # Friendly messages help users understand what went wrong.
        print(f"Could not find {missing_file.name}.")


def practice_section(file_path: Path) -> None:
    # Practice gives learners safe places to experiment with file tasks they
    # will use in scripts like note apps, CSV preprocessors, and log analyzers.
    print("\n--- Practice ---")
    print("1) Edit this function to write your own 3 favorite foods to the file.")
    print("2) Add code that counts how many lines are in the file.")
    print("3) Add code that creates a backup copy with a new name.")
    # Starter code:
    with file_path.open("r", encoding="utf-8") as file:
        # readlines() returns a list where each item is one line of text.
        lines = file.readlines()
    print(f"Starter line count: {len(lines)}")


def questions_section() -> None:
    # Reflection questions help beginners connect syntax to practical decisions.
    print("\n--- Questions ---")
    questions = [
        "1) Why is 'with open(...)' safer than open() without with?",
        "2) What is the difference between 'w' mode and 'a' mode?",
        "3) When would you use readlines() instead of read()?",
        "4) What error is raised when a file path does not exist in read mode?",
    ]
    for question in questions:
        print(question)


def main() -> None:
    # Path(...) points to a file in the current working folder.
    # Using a variable makes it easy to reuse the same file in each example.
    lesson_file = Path("lesson11_sample.txt")
    example_write_and_read(lesson_file)
    example_append(lesson_file)
    example_error_handling(lesson_file)
    practice_section(lesson_file)
    questions_section()


if __name__ == "__main__":
    # This pattern means the lesson runs when executed directly, but not when imported.
    main()

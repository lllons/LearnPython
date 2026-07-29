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
    print("\nExample 1: write and read")
    with file_path.open("w", encoding="utf-8") as file:
        file.write("Line 1: Hello, file!\n")
        file.write("Line 2: Learning Python file I/O.\n")

    with file_path.open("r", encoding="utf-8") as file:
        content = file.read()
    print(content)


def example_append(file_path: Path) -> None:
    """Append new text without removing existing content."""
    print("Example 2: append")
    with file_path.open("a", encoding="utf-8") as file:
        file.write("Line 3: This line was appended.\n")

    with file_path.open("r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, start=1):
            print(f"{line_number}: {line.strip()}")


def example_error_handling(file_path: Path) -> None:
    """Show a simple try/except pattern for file operations."""
    print("\nExample 3: error handling")
    missing_file = file_path.with_name("does_not_exist.txt")
    try:
        with missing_file.open("r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print(f"Could not find {missing_file.name}.")


def practice_section(file_path: Path) -> None:
    print("\n--- Practice ---")
    print("1) Edit this function to write your own 3 favorite foods to the file.")
    print("2) Add code that counts how many lines are in the file.")
    print("3) Add code that creates a backup copy with a new name.")
    # Starter code:
    with file_path.open("r", encoding="utf-8") as file:
        lines = file.readlines()
    print(f"Starter line count: {len(lines)}")


def questions_section() -> None:
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
    lesson_file = Path("lesson11_sample.txt")
    example_write_and_read(lesson_file)
    example_append(lesson_file)
    example_error_handling(lesson_file)
    practice_section(lesson_file)
    questions_section()


if __name__ == "__main__":
    main()

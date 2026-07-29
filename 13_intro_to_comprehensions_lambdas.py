"""
Lesson 13: Comprehensions and Lambda Functions

Learning goals:
- Build lists, sets, and dictionaries with comprehensions.
- Use conditions inside comprehensions.
- Write small anonymous functions with lambda.
- Combine lambda with sorted and map.
"""


def example_list_set_dict_comprehensions() -> None:
    print("\nExample 1: comprehensions")
    # Comprehensions are a compact way to build new collections from existing data.
    # Real-world use: cleaning lists, filtering records, and building quick lookups.
    numbers = [1, 2, 3, 4, 5, 6]
    # List comprehension: "for each n in numbers, store n*n".
    squares = [n * n for n in numbers]
    # Add an if-condition to keep only values that match a rule.
    # Here we keep squares for even numbers only.
    even_squares = [n * n for n in numbers if n % 2 == 0]
    # Set comprehension removes duplicates automatically.
    # Useful when you need unique tags, categories, or IDs.
    unique_last_digits = {n * n % 10 for n in numbers}
    # Dict comprehension creates key-value mappings quickly.
    # Great for lookup tables (e.g., product_id -> product_name).
    square_lookup = {n: n * n for n in numbers}

    print(f"numbers: {numbers}")
    print(f"squares: {squares}")
    print(f"even_squares: {even_squares}")
    print(f"unique_last_digits: {unique_last_digits}")
    print(f"square_lookup: {square_lookup}")


def example_lambda_with_sorted() -> None:
    print("\nExample 2: lambda with sorted")
    words = ["pear", "banana", "fig", "apple"]
    # lambda defines a tiny throwaway function.
    # key= tells sorted() what value to compare.
    by_length = sorted(words, key=lambda word: len(word))
    # Another key example: sort by the last character of each word.
    by_last_char = sorted(words, key=lambda word: word[-1])
    print(f"Original: {words}")
    print(f"Sorted by length: {by_length}")
    print(f"Sorted by last character: {by_last_char}")


def example_lambda_with_map() -> None:
    print("\nExample 3: lambda with map")
    prices = [9.99, 15.0, 20.5]
    # map applies a function to every item.
    # Here we simulate applying 10% tax to each price.
    # round(..., 2) keeps money values to 2 decimal places.
    taxed = list(map(lambda p: round(p * 1.1, 2), prices))
    print(f"Prices: {prices}")
    print(f"After 10% tax: {taxed}")


def practice_section() -> None:
    # These tasks match real coding scenarios:
    # filtering text, transforming values, and custom sort rules.
    print("\n--- Practice ---")
    print("1) Create a comprehension that keeps only words longer than 4 letters.")
    print("2) Build a dictionary mapping each word to its uppercase version.")
    print("3) Use lambda and sorted to sort names by the number of vowels.")
    # Starter code:
    words = ["code", "python", "ai", "lesson", "data"]
    # Example filter rule beginners can modify.
    long_words = [word for word in words if len(word) > 4]
    print(f"Starter long_words: {long_words}")


def questions_section() -> None:
    # Reflection helps learners decide when each tool is the right choice.
    print("\n--- Questions ---")
    questions = [
        "1) What is one benefit of a list comprehension over a loop?",
        "2) How do you add an if-condition to a comprehension?",
        "3) When is lambda useful?",
        "4) What does key= in sorted(...) control?",
        "5) Why should lambda functions usually stay short?",
    ]
    for question in questions:
        print(question)


def main() -> None:
    example_list_set_dict_comprehensions()
    example_lambda_with_sorted()
    example_lambda_with_map()
    practice_section()
    questions_section()


if __name__ == "__main__":
    # Runs the lesson demo when executed directly.
    main()

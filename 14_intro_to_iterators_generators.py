"""
Lesson 14: Iterators and Generators

Learning goals:
- Understand the iterator protocol: iter() and next().
- Build custom iterators with classes.
- Create generators with yield.
- Compare list creation versus lazy generation.
"""


class CountDown:
    """Custom iterator that counts down to 1."""

    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


def square_generator(limit: int):
    """Yield squares from 1 up to limit."""
    for number in range(1, limit + 1):
        yield number * number


def example_iterator_protocol() -> None:
    print("\nExample 1: iterator protocol")
    colors = ["red", "green", "blue"]
    color_iterator = iter(colors)
    print(next(color_iterator))
    print(next(color_iterator))
    print(next(color_iterator))


def example_custom_iterator() -> None:
    print("\nExample 2: custom iterator class")
    for value in CountDown(5):
        print(value, end=" ")
    print()


def example_generators() -> None:
    print("\nExample 3: generator function")
    squares = square_generator(5)
    print(f"Generator object: {squares}")
    for value in squares:
        print(value, end=" ")
    print()


def practice_section() -> None:
    print("\n--- Practice ---")
    print("1) Change CountDown so it can count down by steps of 2.")
    print("2) Write a generator that yields only even numbers up to a limit.")
    print("3) Add code that turns your generator output into a list.")
    # Starter code:
    starter_values = list(square_generator(3))
    print(f"Starter values: {starter_values}")


def questions_section() -> None:
    print("\n--- Questions ---")
    questions = [
        "1) What is returned by iter(some_list)?",
        "2) What signals the end of iteration?",
        "3) What does yield do in a function?",
        "4) Why can generators be more memory efficient than lists?",
    ]
    for question in questions:
        print(question)


def main() -> None:
    example_iterator_protocol()
    example_custom_iterator()
    example_generators()
    practice_section()
    questions_section()


if __name__ == "__main__":
    main()

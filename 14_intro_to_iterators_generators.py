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
    # Why iterators matter:
    # They let you process one item at a time, which is useful for large data.
    # Example: reading millions of rows without loading them all at once.

    def __init__(self, start: int) -> None:
        # Store current state on the object so next() can continue from last value.
        self.current = start

    def __iter__(self):
        # An iterator returns itself from __iter__.
        return self

    def __next__(self) -> int:
        # __next__ returns the next item or raises StopIteration when done.
        if self.current <= 0:
            raise StopIteration
        value = self.current
        # Move internal state forward so next() gives a new value next time.
        self.current -= 1
        return value


def square_generator(limit: int):
    """Yield squares from 1 up to limit."""
    # Generators are like pause/resume functions.
    # yield sends out one value, then remembers where to continue.
    for number in range(1, limit + 1):
        yield number * number


def example_iterator_protocol() -> None:
    print("\nExample 1: iterator protocol")
    colors = ["red", "green", "blue"]
    # iter(list) creates an iterator object from a normal list.
    color_iterator = iter(colors)
    # next(...) asks for one item at a time.
    print(next(color_iterator))
    print(next(color_iterator))
    print(next(color_iterator))


def example_custom_iterator() -> None:
    print("\nExample 2: custom iterator class")
    # for-loops automatically call iter() and next() behind the scenes.
    for value in CountDown(5):
        print(value, end=" ")
    print()


def example_generators() -> None:
    print("\nExample 3: generator function")
    # Calling a generator function does not run it fully yet.
    # It returns a generator object that produces values on demand.
    squares = square_generator(5)
    print(f"Generator object: {squares}")
    # Iterating consumes values one by one (lazy evaluation).
    for value in squares:
        print(value, end=" ")
    print()


def practice_section() -> None:
    # Practice mirrors common data tasks: custom stepping, filtering,
    # and converting lazy results to concrete lists when needed.
    print("\n--- Practice ---")
    print("1) Change CountDown so it can count down by steps of 2.")
    print("2) Write a generator that yields only even numbers up to a limit.")
    print("3) Add code that turns your generator output into a list.")
    # Starter code:
    # list(...) consumes the generator and stores all produced values.
    starter_values = list(square_generator(3))
    print(f"Starter values: {starter_values}")


def questions_section() -> None:
    # These questions check understanding of both mechanics and benefits.
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
    # Standard script entry point.
    main()

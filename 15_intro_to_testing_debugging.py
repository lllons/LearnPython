"""
Lesson 15: Testing and Debugging Basics

Learning goals:
- Write small test functions with assert.
- Group tests and run them from one script.
- Read assertion failures to find bugs.
- Use print-debugging and function tracing.
"""


def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def buggy_is_even(number: int) -> bool:
    """Intentional bug for debugging practice."""
    return number % 2 == 1


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide() -> None:
    assert divide(10, 2) == 5
    try:
        divide(5, 0)
        assert False, "Expected ValueError for divide by zero."
    except ValueError:
        pass


def test_buggy_is_even() -> None:
    assert buggy_is_even(4) is True
    assert buggy_is_even(5) is False


def run_tests() -> None:
    print("\nExample 1: running tests")
    tests = [test_add, test_divide, test_buggy_is_even]
    passed = 0
    for test in tests:
        try:
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError as error:
            print(f"FAIL: {test.__name__} -> {error}")
    print(f"{passed}/{len(tests)} tests passed")


def debugging_demo() -> None:
    print("\nExample 2: print-debugging")
    sample = 4
    remainder = sample % 2
    print(f"Debug -> sample={sample}, remainder={remainder}")
    print("If remainder is 0, the number is even.")


def practice_section() -> None:
    print("\n--- Practice ---")
    print("1) Fix buggy_is_even so tests pass.")
    print("2) Add a new function and write at least 2 tests for it.")
    print("3) Add one failing test first, then change code to make it pass.")


def questions_section() -> None:
    print("\n--- Questions ---")
    questions = [
        "1) What does assert check?",
        "2) Why are small, focused tests useful?",
        "3) What can an assertion error message tell you?",
        "4) When should you raise an exception in your code?",
        "5) What is one simple debugging technique besides a debugger?",
    ]
    for question in questions:
        print(question)


def main() -> None:
    run_tests()
    debugging_demo()
    practice_section()
    questions_section()


if __name__ == "__main__":
    main()

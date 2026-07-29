"""
Lesson 15: Testing and Debugging Basics

Learning goals:
- Write small test functions with assert.
- Group tests and run them from one script.
- Read assertion failures to find bugs.
- Use print-debugging and function tracing.
"""


def add(a: int, b: int) -> int:
    # Small pure functions are easy to test because output depends only on input.
    return a + b


def divide(a: float, b: float) -> float:
    # Raising clear errors helps users and other developers debug faster.
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def buggy_is_even(number: int) -> bool:
    """Intentional bug for debugging practice."""
    # This intentionally wrong logic helps learners practice reading failed tests.
    # Correct logic should check number % 2 == 0.
    return number % 2 == 1


def test_add() -> None:
    # assert checks that the expression is True.
    # If not, Python raises AssertionError.
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_divide() -> None:
    # Test normal behavior first.
    assert divide(10, 2) == 5
    try:
        # Then test error behavior (important for robust code).
        divide(5, 0)
        # If we reach here, divide did not raise as expected.
        assert False, "Expected ValueError for divide by zero."
    except ValueError:
        # pass means "expected exception happened, test succeeds".
        pass


def test_buggy_is_even() -> None:
    # These will fail until buggy_is_even is fixed in practice.
    assert buggy_is_even(4) is True
    assert buggy_is_even(5) is False


def run_tests() -> None:
    print("\nExample 1: running tests")
    # Store test functions in a list so we can run them in a simple loop.
    tests = [test_add, test_divide, test_buggy_is_even]
    passed = 0
    for test in tests:
        try:
            # Calling each test executes its assertions.
            test()
            print(f"PASS: {test.__name__}")
            passed += 1
        except AssertionError as error:
            # Error message points to what assumption failed.
            print(f"FAIL: {test.__name__} -> {error}")
    # Summary gives quick feedback, like lightweight test runners do.
    print(f"{passed}/{len(tests)} tests passed")


def debugging_demo() -> None:
    print("\nExample 2: print-debugging")
    # Print-debugging is simple but very effective for beginners.
    # You expose intermediate values to verify assumptions.
    sample = 4
    remainder = sample % 2
    print(f"Debug -> sample={sample}, remainder={remainder}")
    print("If remainder is 0, the number is even.")


def practice_section() -> None:
    # Real-world flow: write a failing test, fix code, rerun tests.
    # This is the core of test-driven and bug-fix workflows.
    print("\n--- Practice ---")
    print("1) Fix buggy_is_even so tests pass.")
    print("2) Add a new function and write at least 2 tests for it.")
    print("3) Add one failing test first, then change code to make it pass.")


def questions_section() -> None:
    # Reflection encourages test habits, not just syntax memorization.
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
    # Run this file directly to execute demos and tests.
    main()

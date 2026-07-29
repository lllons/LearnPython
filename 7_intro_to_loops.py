"""Lesson 7: Loop patterns and control flow.

Learning goals:
- Review for and while loops with clearer patterns.
- Use break, continue, and else in loops.
- Build simple loop-based mini tasks.
- Prepare for writing reusable logic in functions.
"""


def for_loop_examples():
    print("=== for loop examples ===")

    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
        print("Fruit:", fruit)

    # range(start, stop, step)
    for number in range(2, 11, 2):
        print("Even number:", number)

    # Loop with index and value.
    for index, fruit in enumerate(fruits):
        print(f"Index {index}: {fruit}")


def while_loop_examples():
    print("\n=== while loop examples ===")

    count = 1
    while count <= 5:
        print("Count:", count)
        count += 1

    # break exits loop early.
    for value in range(1, 10):
        if value == 4:
            print("Stopping at 4")
            break
        print("Value:", value)

    # continue skips this iteration.
    for value in range(1, 6):
        if value == 3:
            continue
        print("Without 3:", value)

    # for-else runs else only if loop did NOT break.
    target = 7
    for value in [2, 4, 6, 8]:
        if value == target:
            print("Found target")
            break
    else:
        print("Target not found")


def mini_task_examples():
    print("\n=== mini task examples ===")

    scores = [88, 72, 95, 67, 81]
    total = 0
    for score in scores:
        total += score
    average = total / len(scores)
    print("Average score:", average)

    # Count vowels in a word.
    word = "education"
    vowels = "aeiou"
    vowel_count = 0
    for letter in word:
        if letter in vowels:
            vowel_count += 1
    print(f"Vowels in '{word}':", vowel_count)


def practice_section():
    print("\n=== Practice section ===")
    print("1) Print numbers 1 to 20, but skip multiples of 3.")
    print("2) Find the first number over 50 in a list and stop.")
    print("3) Use a while loop to count down from 5 to 1.")
    print("4) Write a loop that sums only odd numbers from 1 to 15.")

    # Starter list for task 2:
    # numbers = [12, 31, 49, 52, 70]


def questions_section():
    print("\n=== Questions ===")
    print("1) What is the difference between break and continue?")
    print("2) When would you choose a while loop over a for loop?")
    print("3) What does range(2, 11, 2) produce?")
    print("4) When does a loop's else block run?")


if __name__ == "__main__":
    for_loop_examples()
    while_loop_examples()
    mini_task_examples()
    practice_section()
    questions_section()

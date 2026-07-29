# Answers to Lesson Questions

## intro_to_python_basics_1.py
1. A variable is a named reference to a value stored in memory.
2. Python is case-sensitive, so score and Score are different names.
3. `age >= 18` returns a boolean (`True` or `False`).
4. Reassign it, for example: `score = score + 1`.

## intro_to_strings_2.py
1. Concatenation joins strings with `+`; an f-string embeds variables directly in a formatted string.
2. `.strip()` removes leading and trailing whitespace.
3. Use index `-1`, for example `word[-1]`.
4. `len(word)` returns the number of characters.

## intro_to_numbers_math_3.py
1. `/` does true division (float result), while `//` does floor division.
2. `%` returns the remainder after division.
3. Parentheses change evaluation order and can change the result.
4. Example: `round()`, `abs()`, `min()`, or `max()`.

## intro_to_booleans_conditionals_4.py
1. A comparison produces a boolean value (`True` or `False`).
2. `and` is True only when both sides are True.
3. `elif` adds another condition check if earlier `if` or `elif` checks fail.
4. `not` flips a boolean (`True` to `False`, `False` to `True`).

## intro_to_lists_tuples_5.py
1. Lists are mutable; tuples are immutable.
2. `append()` adds an item to the end of a list.
3. `pop()` removes and returns an item (default is the last item).
4. Use index `0`, for example `my_list[0]`.

## intro_to_dictionaries_sets_6.py
1. A list stores ordered values by position; a dictionary stores key-value pairs by key.
2. `dict.get()` can return a default instead of raising an error for missing keys.
3. Set values are unique (no duplicates).
4. Intersection (`a & b`) finds shared values.

## intro_to_loops_7.py
1. `break` exits the loop completely; `continue` skips to the next iteration.
2. Use `while` when the number of iterations is not known in advance.
3. `range(2, 11, 2)` produces 2, 4, 6, 8, 10.
4. A loop `else` block runs only if the loop finishes without `break`.

## intro_to_functions_8.py
1. Functions reduce repetition, improve organization, and make code reusable.
2. `print` displays output; `return` sends a value back to the caller.
3. The default value is used.
4. Add a docstring when a function's purpose, inputs, or behavior need quick clarification.

## intro_to_scope_modules_9.py
1. Local scope means a name exists only inside the function or block where it is defined.
2. Global scope means a name is defined at module level and can be read broadly in that module.
3. `if __name__ == '__main__'` lets code run only when the file is executed directly.
4. You can shadow the module name and break access to its functions (for example `math.sqrt`).

## intro_to_error_handling_10.py
1. `try/except` handles expected runtime errors so the program can fail gracefully.
2. `else` runs when no exception is raised in the `try` block.
3. `finally` is used for cleanup that should always happen.
4. Specific exceptions avoid hiding unrelated bugs and make error handling clearer.

## intro_to_file_io_11.py
1. `with open(...)` auto-closes the file, even if an error happens.
2. `w` overwrites or creates a file; `a` appends to the end.
3. Use `readlines()` when you want a list of lines for per-line processing.
4. `FileNotFoundError`.

## intro_to_oop_12.py
1. `__init__` initializes a new object and sets its starting state.
2. An instance attribute belongs to the object; a local variable exists only inside a function call.
3. Inheritance reuses attributes and methods from a parent class.
4. Overriding `__str__` gives a readable string representation for printing and debugging.

## intro_to_comprehensions_lambdas_13.py
1. List comprehensions are often shorter and clearer for simple transformations and filters.
2. Add `if condition` at the end, for example `[x for x in data if x > 0]`.
3. Lambda is useful for short, one-off functions, often as arguments (for example sort keys).
4. `key=` controls the value used to compare items during sorting.
5. Short lambdas are easier to read and maintain.

## intro_to_iterators_generators_14.py
1. `iter(some_list)` returns an iterator object.
2. `StopIteration` signals the end.
3. `yield` produces a value and pauses function state until the next request.
4. Generators produce values lazily, so they usually use less memory.

## intro_to_testing_debugging_15.py
1. `assert` checks that a condition is True and raises `AssertionError` if not.
2. Small, focused tests isolate problems and are easier to understand and fix.
3. An assertion error message shows what failed and helps locate the bug quickly.
4. Raise an exception when inputs or state are invalid and normal execution cannot safely continue.
5. Print-debugging (logging variable values and flow) is a simple technique.

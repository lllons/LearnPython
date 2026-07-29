"""
Lesson 12: Introduction to Object-Oriented Programming (OOP)

Learning goals:
- Define classes and create objects.
- Use instance attributes and methods.
- Understand inheritance and method overriding.
- Use __str__ for readable object output.
"""


class BankAccount:
    """A simple class for account balance behavior."""
    # Why classes matter:
    # In real systems (banking, games, inventory apps), you model "things"
    # with both data (attributes) and actions (methods).

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        # __init__ runs when creating a new object, e.g. BankAccount("Ava", 100.0).
        # It sets each account's starting state.
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        # Input validation protects your object from invalid state.
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        # Updating self.balance changes this specific account instance.
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        # Return True/False so calling code can react (show success/failure message).
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            # Real-world analogy: declined payment due to insufficient funds.
            return False
        self.balance -= amount
        return True

    def __str__(self) -> str:
        # __str__ controls how the object looks when printed.
        # Helpful for debugging, logs, and readable terminal output.
        return f"BankAccount(owner={self.owner}, balance={self.balance:.2f})"


class SavingsAccount(BankAccount):
    """Savings account adds interest behavior."""
    # Inheritance lets us reuse BankAccount behavior (deposit/withdraw/etc.)
    # and then add savings-specific features.

    def apply_interest(self, rate_percent: float) -> None:
        # Banks often apply monthly or yearly interest.
        # Example: 5% on 200 gives 10, so balance becomes 210.
        if rate_percent < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.balance += self.balance * (rate_percent / 100)

    def __str__(self) -> str:
        # Overriding __str__ makes the subclass print with its own label.
        return f"SavingsAccount(owner={self.owner}, balance={self.balance:.2f})"


def example_basic_class_usage() -> None:
    print("\nExample 1: class and object usage")
    # Create an object from the class (this is called "instantiation").
    account = BankAccount("Ava", 100.0)
    # Call methods to perform operations on the object.
    account.deposit(50.0)
    success = account.withdraw(20.0)
    print(account)
    print(f"Withdraw success: {success}")


def example_inheritance() -> None:
    print("\nExample 2: inheritance")
    # SavingsAccount automatically has inherited behavior from BankAccount.
    savings = SavingsAccount("Noah", 200.0)
    savings.apply_interest(5.0)
    print(savings)


def practice_section() -> None:
    # These exercises mirror common fintech features:
    # transfers, fees, and interactions between multiple accounts.
    print("\n--- Practice ---")
    print("1) Add a transfer_to(other_account, amount) method in BankAccount.")
    print("2) Add a class named CheckingAccount with a small transaction fee.")
    print("3) Create two accounts and test transferring money between them.")


def questions_section() -> None:
    # Questions reinforce the "why" behind OOP design choices.
    print("\n--- Questions ---")
    questions = [
        "1) What is the role of the __init__ method?",
        "2) How is an instance attribute different from a local variable?",
        "3) What does inheritance let you reuse?",
        "4) Why might you override __str__ in a class?",
    ]
    for question in questions:
        print(question)


def main() -> None:
    example_basic_class_usage()
    example_inheritance()
    practice_section()
    questions_section()


if __name__ == "__main__":
    # Standard entry point pattern for runnable lesson scripts.
    main()

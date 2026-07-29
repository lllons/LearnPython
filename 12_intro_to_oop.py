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

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner}, balance={self.balance:.2f})"


class SavingsAccount(BankAccount):
    """Savings account adds interest behavior."""

    def apply_interest(self, rate_percent: float) -> None:
        if rate_percent < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.balance += self.balance * (rate_percent / 100)

    def __str__(self) -> str:
        return f"SavingsAccount(owner={self.owner}, balance={self.balance:.2f})"


def example_basic_class_usage() -> None:
    print("\nExample 1: class and object usage")
    account = BankAccount("Ava", 100.0)
    account.deposit(50.0)
    success = account.withdraw(20.0)
    print(account)
    print(f"Withdraw success: {success}")


def example_inheritance() -> None:
    print("\nExample 2: inheritance")
    savings = SavingsAccount("Noah", 200.0)
    savings.apply_interest(5.0)
    print(savings)


def practice_section() -> None:
    print("\n--- Practice ---")
    print("1) Add a transfer_to(other_account, amount) method in BankAccount.")
    print("2) Add a class named CheckingAccount with a small transaction fee.")
    print("3) Create two accounts and test transferring money between them.")


def questions_section() -> None:
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
    main()

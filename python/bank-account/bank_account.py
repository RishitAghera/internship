from enum import Enum
from threading import Lock


class State(Enum):
    UNOPENED = "unopened"
    OPEN = "open"
    CLOSED = "closed"


class BankAccount(object):

    def __init__(self) -> None:
        self._balance = 0
        self._state = State.UNOPENED
        self._lock = Lock()

    def _error_if_not_open(self) -> None:
        if self._state is State.UNOPENED:
            raise ValueError("Account never opened!")
        if self._state is State.CLOSED:
            raise ValueError("Account not open!")

    def open(self) -> None:

        with self._lock:
            if self._state is State.OPEN:
                raise ValueError("Account already open!")
            self._state = State.OPEN
            self._balance = 0

    def close(self) -> None:

        with self._lock:
            self._error_if_not_open()
            self._state = State.CLOSED

    def get_balance(self) -> int:

        with self._lock:
            self._error_if_not_open()
            return self._balance

    def deposit(self, amount: int) -> None:
        with self._lock:
            self._error_if_not_open()
            if amount < 0:
                raise ValueError("Cannot make a negative deposit!")
            self._balance += amount

    def withdraw(self, amount: int) -> None:
        with self._lock:
            self._error_if_not_open()
            if amount < 0:
                raise ValueError("Cannot make a negative withdrawl!")
            elif amount > self._balance:
                raise ValueError("withdrawl amount is greater than balance!")
            self._balance -= amount

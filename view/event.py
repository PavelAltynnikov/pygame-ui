from typing import Any, Callable


class Event:
    def __init__(self):
        self._functions: list[Callable[[str], Any]] = []

    def __iadd__(self, other: Callable):
        self._functions.append(other)
        return self

    def __call__(self, message):
        for function in self._functions:
            function(message)

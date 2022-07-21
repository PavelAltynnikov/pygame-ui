from typing import Callable


class EventArgs:
    pass


class Event:
    def __init__(self, sender: object, event_args: EventArgs):
        self._sender = sender
        self._event_args = event_args
        self._functions: list[Callable[[object, EventArgs], None]] = []

    def __iadd__(self, other: Callable[[object, EventArgs], None]):
        self._functions.append(other)
        return self

    def __call__(self) -> None:
        for function in self._functions:
            function(self._sender, self._event_args)

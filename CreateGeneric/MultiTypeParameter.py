from typing import TypeVar, Generic

T = TypeVar("T")
U = TypeVar("U")


class Pair(Generic[T, U]):

    def __init__(self, first: T, second: U):
        self.first = first
        self.second = second


pair = Pair[int, str](101, "Avadhut")

print(pair.first)
print(pair.second)
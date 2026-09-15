from typing import Generic,TypeVar

T = TypeVar("T")

def get_first_item(items : list[T]) -> T:
    return items[0]


numbers = [10,20,30]

result = get_first_item(numbers)

print(result)

names = ['A','B','C']

result1 = get_first_item(names)

print(result1)
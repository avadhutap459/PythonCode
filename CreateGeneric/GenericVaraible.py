from typing import Generic , TypeVar

T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self,value : T):
        self.value = value
        
    def get_value(self) -> T:
        return self.value
    

int_box = Box[int](1000)

print(int_box.get_value())

str_box = Box[str]("Avadhut")

print(str_box.get_value())


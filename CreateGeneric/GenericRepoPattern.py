from typing import Generic ,TypeVar
from abc import ABC, abstractmethod

T = TypeVar("T")

class IRepo(Generic[T],ABC):
    @abstractmethod
    def get_by_id(self,id : int) -> T:
        pass
    
    @abstractmethod
    def get_all(self) -> list[T]:
        pass
    
    @abstractmethod
    def add(self,entity : T) -> T :
        pass

class EmployeeModel:
    def __init__(self , id :int ,name :str):
        self.Id = id
        self.Name = name
        

class EmployeeRepo(IRepo[EmployeeModel]):
    def get_by_id(self, id) -> EmployeeModel:
        return EmployeeModel(101,"Avadhut")
    
    def get_all(self) -> list[EmployeeModel]:
        return [
            EmployeeModel(101,"Ab"),
            EmployeeModel(102,"xy")
        ]
    
    def add(self, entity : EmployeeModel) ->EmployeeModel:
        return entity


class Customer:

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        

class CustomerRepository(IRepo[Customer]):

    def get_by_id(self, id: int) -> Customer:
        return Customer(id, "ABC Customer")

    def get_all(self) -> list[Customer]:
        return [
            Customer(1, "ABC"),
            Customer(2, "XYZ")
        ]

    def add(self, entity: Customer) -> Customer:
        return entity
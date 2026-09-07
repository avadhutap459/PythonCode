# Creation of abstract factory in Python
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def get_details(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"Full-Time Employee: {self.name}, Salary: {self.salary}"


class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate):
        self.name = name
        self.hourly_rate = hourly_rate

    def get_details(self):
        return f"Part-Time Employee: {self.name}, Hourly Rate: {self.hourly_rate}"


class EmployeeFactory(ABC):
    @abstractmethod
    def create_employee(self, name, compensation):
        pass


class FullTimeEmployeeFactory(EmployeeFactory):
    def create_employee(self, name, salary):
        return FullTimeEmployee(name, salary)


class PartTimeEmployeeFactory(EmployeeFactory):
    def create_employee(self, name, hourly_rate):
        return PartTimeEmployee(name, hourly_rate)


if __name__ == "__main__":
    full_time_factory = FullTimeEmployeeFactory()
    part_time_factory = PartTimeEmployeeFactory()

    full_time_emp = full_time_factory.create_employee("Alice", 60000)
    part_time_emp = part_time_factory.create_employee("Bob", 25)

    print(full_time_emp.get_details())
    print(part_time_emp.get_details())



# Example 2
from abc import ABC, abstractmethod


# =========================
# Abstract Products
# =========================

class Connection(ABC):

    @abstractmethod
    def connect(self):
        pass


class Repository(ABC):

    @abstractmethod
    def get_data(self):
        pass


# =========================
# SQL Server Products
# =========================

class SqlConnection(Connection):

    def connect(self):
        print("Connected to SQL Server")


class SqlRepository(Repository):

    def get_data(self):
        print("Getting data from SQL Server")


# =========================
# PostgreSQL Products
# =========================

class PostgreSqlConnection(Connection):

    def connect(self):
        print("Connected to PostgreSQL")


class PostgreSqlRepository(Repository):

    def get_data(self):
        print("Getting data from PostgreSQL")


# =========================
# Abstract Factory
# =========================

class DatabaseFactory(ABC):

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_repository(self):
        pass


# =========================
# SQL Factory
# =========================

class SqlServerFactory(DatabaseFactory):

    def create_connection(self):
        return SqlConnection()

    def create_repository(self):
        return SqlRepository()


# =========================
# PostgreSQL Factory
# =========================

class PostgreSqlFactory(DatabaseFactory):

    def create_connection(self):
        return PostgreSqlConnection()

    def create_repository(self):
        return PostgreSqlRepository()


# =========================
# Client
# =========================

class DatabaseService:

    def __init__(self, factory):
        self.factory = factory

    def execute(self):

        connection = self.factory.create_connection()
        repository = self.factory.create_repository()

        connection.connect()
        repository.get_data()


factory = SqlServerFactory()

service = DatabaseService(factory)

service.execute()
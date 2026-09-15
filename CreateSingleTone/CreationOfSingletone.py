# Singletone Design Pattern in Python
class Singleton:
    _instance = None  # Class variable to hold the single instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value  # Instance variable
    
# Example usage
singleton1 = Singleton("First Instance")
singleton2 = Singleton("Second Instance")

print(singleton1.value)  # Output: First Instance
print(singleton2.value)  # Output: First Instance

# Check if both instances are the same
print(singleton1 is singleton2)  # Output: True


# what is this def __new__(cls, *args, **kwargs):
# The `__new__` method in Python is a special method that is responsible for creating a new instance of a class. 
# It is called before the `__init__` method and is used to control the creation of new instances.


# Singleton Design Pattern Another Example
class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Example usage
singleton1 = Singleton("First Instance")    
singleton2 = Singleton("Second Instance")
print(singleton1.value)  # Output: First Instance
print(singleton2.value)  # Output: First Instance

print(singleton1 is singleton2)  # Output: True

# Explian above code :- The code above demonstrates the Singleton Design Pattern in Python, 
# which ensures that a class has only one instance and provides a global point of access 
# to that instance.


# Example 3
class Singleton:

    _instance = None
    _initialized = False

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):

        if self._initialized:
            return

        print("Initializing object")

        self._initialized = True
        
obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton() # Output only once "Initializing object"


# Static Methods and static class variables in Python
class Example:
    static_variable = "I am a static variable"

    @staticmethod
    def static_method():
        return "I am a static method"

# Example usage
print(Example.static_variable)  # Output: I am a static variable
print(Example.static_method())  # Output: I am a static method

# Static methods can be called without creating an instance of the class, and they do not have access to instance variables or methods. They are used for utility functions that are related to the class but do not require access to instance-specific data.

class ExampleWithInstance:
    def __init__(self, value):
        self.instance_variable = value

    @staticmethod
    def static_method():
        return "I am a static method"

    def instance_method(self):
        return f"I am an instance method. Instance variable: {self.instance_variable}"

example = ExampleWithInstance("I am an instance variable")
print(example.static_method())  # Output: I am a static method
print(example.instance_method())  # Output: I am an instance method. Instance variable: I am an instance variable

# Static in inheritance
class Parent:
    @staticmethod
    def static_method():
        return "I am a static method from Parent class"

class Child(Parent):
    @staticmethod
    def static_method():
        return "I am a static method from Child class"

# Example usage
print(Parent.static_method())  # Output: I am a static method from Parent class
print(Child.static_method())   # Output: I am a static method from Child class

# Difference between Static Method and Class Method 
class Example:
    class_variable = "I am a class variable"

    @staticmethod
    def static_method():
        return "I am a static method"

    @classmethod
    def class_method(cls):
        return f"I am a class method. Class variable: {cls.class_variable}"
    
# Example usage
print(Example.static_method())  # Output: I am a static method
print(Example.class_method())   # Output: I am a class method. Class variable: I am a class variable    

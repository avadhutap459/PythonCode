print("-------------Example 1")
try:
    number = 10
    result = number / 0

except:
    print("Something went wrong")
    
print("-------------Example 2 :: Specific Exception")    
try:
    number = 10
    result = number / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
    

print("-------------Example 3 :: Actual Error Message")
try:
    number = 10
    result = number / 0

except ZeroDivisionError as ex:
    print(ex)
    
print("-------------Example 4 :: Multiple Exception")
try:

    number = int(input("Enter number:"))

    result = 100 / number

except ValueError:
    print("Please enter a valid number")

except ZeroDivisionError:
    print("Number cannot be zero")
    
print("-------------Example 5 :: Generic Exception")
try:
    x = 10 / 0

except Exception as ex:
    print(ex)
    

print("-------------Example 6 :: Finally Block")
try:

    result = 10 / 2

except Exception as ex:

    print(ex)

finally:

    print("Closing database connection")


print("-------------Example 7 :: Else Block")
try:

    result = 10 / 2

except Exception as ex:

    print(ex)

else:

    print("Operation successful")

print("-------------Example 8 :: Raise Exception")
age = 15

if age < 18:
    raise Exception(
        "Age must be 18 or above"
    )

print("-------------Example 9 :: Custom Exception")
class InvalidAgeException(Exception):
    pass

try:

    age = 15

    if age < 18:
        raise InvalidAgeException(
            "Age must be 18 or above"
        )

except InvalidAgeException as ex:

    print(ex)

print("-------------Example 10 :: Exception Handling Inside Method")

class UserRepository:

    def get_user(self, user_id):

        try:

            # Database logic

            return user

        except Exception as ex:

            print(ex)

            raise


class UserService:

    def __init__(self, repository):
        self.repository = repository

    def get_user(self, user_id):

        try:

            return self.repository.get_user(
                user_id
            )

        except Exception:

            raise Exception(
                "Unable to get user"
            )

from fastapi import HTTPException


@app.get("/users/{user_id}")
def get_user(user_id: int):

    user = repository.get_user(user_id)

    if user is None:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


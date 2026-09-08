# Creation of unit of work in python
print("-----------------Unit Of Work Example---------------")

class UnitOfWork:

    def __enter__(self):
        print("Transaction started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:
            print("Transaction committed")
        else:
            print("Transaction rolled back")
            

with UnitOfWork():
    print("Operation 1")
    print("Operation 2")
    
# Output
# Transaction started
# Operation 1
# Operation 2
# Transaction committed



print("-----------------Unit Of Work Excption---------------")

with UnitOfWork():
    print("Operation 1")
    
    raise Exception("Something went wrong")

    print("Operation 2")

print("-----------------Repository + Unit of Work---------------")

class UserRepository:

    def create(self, user):
        print("Create user")

    def update(self, user):
        print("Update user")

class AccountRepository:

    def update_balance(self, account_id, amount):
        print("Update account balance")

class UnitOfWork:

    def __init__(self):

        self.users = UserRepository()
        self.accounts = AccountRepository()

    def __enter__(self):
        print("Transaction started")
        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:
            self.commit()
        else:
            self.rollback()

    def commit(self):
        print("COMMIT")

    def rollback(self):
        print("ROLLBACK")

with UnitOfWork() as uow:

    uow.users.create("Avadhut")

    uow.accounts.update_balance(
        101,
        -10000
    )

print("-----------------Repository + Unit of Work + Exception---------------")

with UnitOfWork() as uow:

    uow.users.create("Avadhut")

    raise Exception("Database error")

    uow.accounts.update_balance(101, -10000)
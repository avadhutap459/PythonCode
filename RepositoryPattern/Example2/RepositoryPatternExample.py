from abc import ABC, abstractmethod

from RepositoryPattern.Model import User


class IUserRepository(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self, user_id):
        pass

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def delete(self, user_id):
        pass
    

class UserRepository(IUserRepository):

    def __init__(self):
        self.users = []

    def get_all(self):
        return self.users

    def get_by_id(self, user_id):

        for user in self.users:

            if user.user_id == user_id:
                return user

        return None

    def create(self, user):
        self.users.append(user)
        return user

    def update(self, user):

        existing_user = self.get_by_id(user.user_id)

        if existing_user is None:
            return None

        existing_user.name = user.name
        existing_user.email = user.email

        return existing_user

    def delete(self, user_id):

        user = self.get_by_id(user_id)

        if user is None:
            return False

        self.users.remove(user)

        return True
    

class UserService:

    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def create_user(self, user):
        return self.repository.create(user)

    def update_user(self, user):
        return self.repository.update(user)

    def delete_user(self, user_id):
        return self.repository.delete(user_id)

repository = UserRepository()

service = UserService(repository)

user = User(
    1,
    "Avadhut",
    "avadhut@example.com"
)

service.create_user(user)

user = service.get_user(1)

print(user.name)


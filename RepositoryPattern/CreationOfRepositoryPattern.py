from RepositoryPattern import UserRepository, UserService
from RepositoryPattern.Model import User# Creation of Repository Pattern in python



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
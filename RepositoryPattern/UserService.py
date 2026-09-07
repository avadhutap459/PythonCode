class UserService:

    def __init__(self, repository):
        self.repository = repository

    def get_users(self):
        return self.repository.get_all()

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def create_user(self, user):
        return self.repository.create(user)

    def update_user(self, user):
        return self.repository.update(user)

    def delete_user(self, user_id):
        return self.repository.delete(user_id)
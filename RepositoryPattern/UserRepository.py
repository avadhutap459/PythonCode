class UserRepository:

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
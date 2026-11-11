"""Classes representing administrator privileges."""

from user import User


class Privileges:
    """Store and display administrator privileges."""

    def __init__(self):
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """Represent an administrator."""

    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
        self.privileges = Privileges()
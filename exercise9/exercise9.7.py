class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")


class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]

    def show_privileges(self):
        print("Hak akses administrator:")
        for privilege in self.privileges:
            print(f"- {privilege}")


admin = Admin("Kayla", "Nafisa", 19, "Kebumen")

admin.describe_user()
admin.show_privileges()
class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Nama depan: {self.first_name}")
        print(f"Nama belakang: {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name} {self.last_name}! Selamat datang.")


user1 = User("Kayla", "Kafka", 19, "Kebumen")
user2 = User("Kahla", "Asila", 20, "Yogyakarta")

user1.describe_user()
user1.greet_user()

print()

user2.describe_user()
user2.greet_user()
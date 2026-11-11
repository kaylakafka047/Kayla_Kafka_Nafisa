class User:
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nama: {self.first_name} {self.last_name}")
        print(f"Umur: {self.age}")
        print(f"Lokasi: {self.location}")

    def greet_user(self):
        print(f"Halo, {self.first_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User("Kayla", "Kafka", 19, "Kebumen")

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

print(f"Jumlah percobaan login: {user.login_attempts}")

user.reset_login_attempts()

print(f"Jumlah percobaan login setelah direset: {user.login_attempts}")
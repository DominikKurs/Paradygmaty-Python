import string

class User:
    def __init__(self, name: string, surname: string, isActive: bool):
        self.name = name
        self.surname = surname
        self.isActive = isActive

    def print(self):
        print(f"Imie: {self.name} | Nazwisko: {self.surname} | Czy aktywny: {self.isActive}")

    def setActive(self, active):
        self.isActive = active

class Book:
    def __init__(self, users):
        self.users = users

    def add_user(self, user):
        self.users.append(user)

    def print_users(self):
        print("Wszyscy użytkownicy w książce: ")
        for user in self.users:
            user.print()

    def print_active_users(self):
        print("Aktywni użytkownicy w książce: ")
        for user in self.users:
            if user.isActive:
                user.print()

    def find_by_name(self, name):
        for user in self.users:
            if user.name == name:
                return user

    def get_count(self):
        counter = len(self.users)
        print(f"Liczba użytkowników: {counter}")


user1 = User("Karol", "Wojtyła", False)
user2 = User("Jarosław", "Kaczyński", True)
user3 = User("Orzeł", "Jabol", True)
user4 = User("Student", "Piwo", False)

ksiazka = Book([user1, user2, user3, user4])

ksiazka.print_users()
ksiazka.print_active_users()

znaleziony = ksiazka.find_by_name("Karol")
znaleziony.print()

ksiazka.get_count()
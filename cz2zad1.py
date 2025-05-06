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


user = User("Karol", "Wojtyła", False)
user.print()
user.setActive(True)
user.print()
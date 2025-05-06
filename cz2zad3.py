class Osoba:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Imie: {self.name}, nazwisko: {self.surname}'

    def imie(self):
        print(f"Imie: {self.name}")

    def nazwisko(self):
        print(f"Nazwisko: {self.surname}")

czlek = Osoba("Tego", "Typu")

czlek.imie()
czlek.nazwisko()
print(czlek)
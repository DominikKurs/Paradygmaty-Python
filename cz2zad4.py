class Osoba:
    def __init__(self, name, surname, rodzic = None):
        self.name = name
        self.surname = surname
        self.rodzic = rodzic

    def czydziadek(self):
        if self.rodzic and self.rodzic.rodzic:
            dziadek = self.rodzic.rodzic
            print(f"Dziadkiem {self.name} jest {dziadek.name}")
        else:
            print("Ni ma dziada.")

dziadek = Osoba("Stachu", "Nowak")
ojciec = Osoba("Kuba", "Kowalski", dziadek)
wnuk = Osoba("Marcin", "Kowalski", ojciec)

wnuk.czydziadek()

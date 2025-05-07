dziennik = {}

def dodaj(przedmiot, ocena):
    if przedmiot not in dziennik:
        dziennik[przedmiot] = []
    dziennik[przedmiot].append(ocena)

def wyswietl(przedmiot):
    if przedmiot in dziennik:
        print("Oceny z", przedmiot + ":", dziennik[przedmiot])
    else:
        print("Nima ocen.")

def liczsrednia(przedmiot):
    if przedmiot in dziennik and len(dziennik[przedmiot]) > 0:
        srednia = sum(dziennik[przedmiot]) / len(dziennik[przedmiot])
        print("Średnia z", przedmiot + ":", srednia)
    else:
        print("Nima ocen.")

dodaj("matematyka", 4)
dodaj("matematyka", 5)
dodaj("matematyka", 3)
dodaj("biologia", 5)
dodaj("biologia", 4)

wyswietl("matematyka")
liczsrednia("matematyka")

wyswietl("biologia")
liczsrednia("biologia")
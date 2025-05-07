def czypalindrom(slowo):
    slowo = slowo.lower()
    if slowo == slowo[::-1]:
        return True
    else:
        return False

print(czypalindrom("oko"))
print(czypalindrom("kajak"))
print(czypalindrom("dom"))
print(czypalindrom("papiez"))

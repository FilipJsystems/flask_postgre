class Osoba:
    pass


osoba1 = Osoba()


class Osoba:
    gatunek = "człowiek"


class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

# atrybuty
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        return f"Cześć, jestem {self.imie}!"

# metody magiczne
class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return f"Osoba o imieniu {self.imie}"

    def __repr__(self):
        return f"Osoba('{self.imie}')"


# 1. Deklaracja klas
class Osoba:
    gatunek = "człowiek"

    # 3. Atrybuty instancji
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    # 4. Metody
    def przedstaw_sie(self):
        return f"Cześć, jestem {self.imie} {self.nazwisko}!"

    # 5. Najczęściej używane metody magiczne
    def __str__(self):
        return f"Osoba o imieniu {self.imie}"

    def __repr__(self):
        return f"Osoba('{self.imie}', '{self.nazwisko}')"


# 2. Tworzenie obiektów
osoba1 = Osoba("Filip", "Kowalski")
osoba2 = Osoba("Anna", "Nowak")

print(osoba1.gatunek)        # Wydruk: człowiek
print(osoba2.gatunek)        # Wydruk: człowiek
print(osoba1.imie)          # Wydruk: Filip
print(osoba2.nazwisko)      # Wydruk: Nowak

# 4. Wywołanie metody
print(osoba1.przedstaw_sie())  # Wydruk: C

# 5. Używając metod magicznych
print(osoba1)  # Wydruk: Osoba o imieniu Filip, dzięki metodzie __str__
print(repr(osoba2))  # Wydruk: Osoba('Anna', 'Nowak') dzięki metodzie __repr


class Dziecko(Osoba):
    def __init__(self, wiek):
        self.wiek = wiek

    def podaj_wiek(self):
        return f"Osoba o imieniu {self.imie}"


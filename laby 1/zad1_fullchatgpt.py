import math
from datetime import datetime

def calculate_biorhythms(year, month, day):
    # Obliczanie wieku w dniach
    birth_date = datetime(year, month, day)
    today = datetime.now()
    age_in_days = (today - birth_date).days

    # Obliczanie biorytmów
    physical_biorhythm = math.sin(2 * math.pi / 23 * age_in_days)
    emotional_biorhythm = math.sin(2 * math.pi / 28 * age_in_days)
    intellectual_biorhythm = math.sin(2 * math.pi / 33 * age_in_days)

    return physical_biorhythm, emotional_biorhythm, intellectual_biorhythm

def main():
    # Pobranie danych od użytkownika
    name = input("Podaj swoje imię: ")
    year = int(input("Podaj rok urodzenia: "))
    month = int(input("Podaj miesiąc urodzenia (w formacie liczbowym): "))
    day = int(input("Podaj dzień urodzenia: "))

    # Obliczenie biorytmów
    physical, emotional, intellectual = calculate_biorhythms(year, month, day)

    # Wydrukowanie powitania
    print(f"Witaj {name}!")

    # Obliczenie aktualnej daty życia użytkownika
    birth_date = datetime(year, month, day)
    today = datetime.now()
    days_alive = (today - birth_date).days
    print(f"Dziś jest {days_alive} dzień Twojego życia.")

    # Wydrukowanie wyników biorytmów
    print("Twoje wyniki biorytmów:")
    print(f"Fizyczny: {physical}")
    print(f"Emocjonalny: {emotional}")
    print(f"Intelektualny: {intellectual}")

if __name__ == "__main__":
    main()

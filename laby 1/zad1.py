from datetime import date, timedelta
import math
from typing import Callable
def calc_days_old(birthdate: date) -> int:
    return (date.today() - birthdate).days

def physical_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/23)

def emotional_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/28)

def intellectual_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/33)

def check_biorythm(birthdate: date, biorythm: Callable) -> str:
    if biorythm(birthdate) > 0.5:
        return "Świetnie!"
    else:
        if biorythm(birthdate - timedelta(days=1)) > 0.5:
            return "Jutro bedzie lepiej"
        else:
            return "Nie za dobrze"

def main():
    name: str = input("Podaj imię: ")
    birthyear = int(input("Podaj rok urodzenia: "))
    birthmonth = int(input("Podaj miesiąc urodzenia: "))
    birthday = int(input("Podaj dzień urodzenia: "))
    print(f"Hello {name}.")
    print(f"Jesteś już {calc_days_old(date(birthyear, birthmonth, birthday))} dni na świecie.")
    print(f"Twój fizyczny biorytm wynosi {physical_biorythm(date(birthyear, birthmonth, birthday)):.2f}.")
    print(check_biorythm(date(birthyear, birthmonth, birthday), physical_biorythm))
    print(f"Twój emocjonalny biorytm wynosi {emotional_biorythm(date(birthyear, birthmonth, birthday)):.2f}.")
    print(check_biorythm(date(birthyear, birthmonth, birthday), emotional_biorythm))
    print(f"Twój intelektualny biorytm wynosi {intellectual_biorythm(date(birthyear, birthmonth, birthday)):.2f}.")
    print(check_biorythm(date(birthyear, birthmonth, birthday), intellectual_biorythm))

    


if __name__ == "__main__":
    main()
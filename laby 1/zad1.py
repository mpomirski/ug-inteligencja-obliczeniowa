from datetime import date
import math
def calc_days_old(birthdate: date) -> int:
    return (date.today() - birthdate).days

def physical_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/23)

def emotional_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/28)

def intellectual_biorythm(birthdate: date) -> float:
    return math.sin(2*math.pi*calc_days_old(birthdate)/33)

    

def main():
    name: str = input("Podaj imię: ")
    birthyear = int(input("Podaj rok urodzenia: "))
    birthmonth = int(input("Podaj miesiąc urodzenia: "))
    birthday = int(input("Podaj dzień urodzenia: "))
    print(f"Hello {name}.")
    print(f"Jesteś już {calc_days_old(date(birthyear, birthmonth, birthday))} dni na świecie.")
    print(f"Twój fizyczny biorytm wynosi {physical_biorythm(date(birthyear, birthmonth, birthday))}.")
    print(f"Twój emocjonalny biorytm wynosi {emotional_biorythm(date(birthyear, birthmonth, birthday))}.")
    print(f"Twój intelektualny biorytm wynosi {intellectual_biorythm(date(birthyear, birthmonth, birthday))}.")
    



if __name__ == "__main__":
    main()
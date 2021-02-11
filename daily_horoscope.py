from bs4 import BeautifulSoup
import requests

"""
   this check_sign function checks and returns the zodiac sign
   by day and month of your birth

"""


def check_sign():
    your_birth_day = input("enter your birthday day number> ")
    your_birth_month = input("cool, and the month number, please> ")
    if (int(your_birth_month) == 12 and int(your_birth_day) >= 22) or (
        int(your_birth_month) == 1 and int(your_birth_day) <= 19
    ):
        sign = "Capricorn"
    elif (int(your_birth_month) == 1 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 2 and int(your_birth_day) <= 17
    ):
        sign = "Aquarium"
    elif (int(your_birth_month) == 2 and int(your_birth_day) >= 18) or (
        int(your_birth_month) == 3 and int(your_birth_day) <= 19
    ):
        sign = "Pices"
    elif (int(your_birth_month) == 3 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 4 and int(your_birth_day) <= 19
    ):
        sign = "Aries"
    elif (int(your_birth_month) == 4 and int(your_birth_day) >= 20) or (
        int(your_birth_month) == 5 and int(your_birth_day) <= 20
    ):
        sign = "Taurus"
    elif (int(your_birth_month) == 5 and int(your_birth_day) >= 21) or (
        int(your_birth_month) == 6 and int(your_birth_day) <= 20
    ):
        sign = "Gemini"
    elif (int(your_birth_month) == 6 and int(your_birth_day) >= 21) or (
        int(your_birth_month) == 7 and int(your_birth_day) <= 22
    ):
        sign = "Cancer"
    elif (int(your_birth_month) == 7 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 8 and int(your_birth_day) <= 22
    ):
        sign = "Leo"
    elif (int(your_birth_month) == 8 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 9 and int(your_birth_day) <= 22
    ):
        sign = "Virgo"
    elif (int(your_birth_month) == 9 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 10 and int(your_birth_day) <= 22
    ):
        sign = "Libra"
    elif (int(your_birth_month) == 10 and int(your_birth_day) >= 23) or (
        int(your_birth_month) == 11 and int(your_birth_day) <= 21
    ):
        sign = "Scorpio"
    elif (int(your_birth_month) == 11 and int(your_birth_day) >= 22) or (
        int(your_birth_month) == 12 and int(your_birth_day) <= 21
    ):
        sign = "Sagittarius"

    return sign


def horoscope(zodiac_sign: int, day: str) -> str:
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
    except:
        return "Connection Error"
    return soup.find("div", class_="main-horoscope").p.text




from bs4 import BeautifulSoup
import requests
import sys

"""
   this check_sign function checks and returns the zodiac sign
   by day and month of your birth

"""


def check_sign(your_birth_day,your_birth_month):
    """Function Helps users to discover their Sign based on
    day of birth(1-31) in str and month of birth(1-12) in int
    """
    
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
    """Helper Fuction to fetch the horoscope data
    """
    url = (
        "https://www.horoscope.com/us/horoscopes/general/"
        f"horoscope-general-daily-{day}.aspx?sign={zodiac_sign}"
    )
    try:
        soup = BeautifulSoup(requests.get(url).content, "html.parser")
    except:
        return "Internet Connection Error, Check connection and Try Again!!"
    return soup.find("div", class_="main-horoscope").p.text


def date_selector():
    
    """
    This function helps fetch hoscropes based on date and is parsed 
    into the function above
    """
    try:
        options = f"""
        choose a day(1-3)
        --------------------
        1.Yesterday
        2.Today
        3.Tomorrow"""

        print(options)
        day = int(input("Enter the number representation of the options :"))

        if day == 1:
            str_day = 'yesterday'
        elif day == 2:
            str_day = 'today'
        elif day == 3:
            str_day = 'tomorrow'
        else:
            print("Enter valid option")
    except (TypeError,ValueError,NameError):
        sys.exit("Try agin with a valid input")

    return str_day





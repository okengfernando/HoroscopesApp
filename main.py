import daily_horoscope
from bs4 import BeautifulSoup
import requests
import sys


def value_validator(value,lower_limit,upper_limit):
    if value >= lower_limit and value <= upper_limit:
        pass
    elif value == 0:
        pass
    else:
        sys.exit("Enter a number and Try Again in the range {} to {}".format(lower_limit,upper_limit))
    

if __name__ == "__main__":
    print("Daily Horoscope. \n")
    print(
        "enter your Zodiac sign number:\n",
        "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n",
        "\nor if you're not sure about you sign, type 0",
    )
try:
    zodiac_sign = int(input("Please Enter valid number from the options given : "))
 

except (NameError,TypeError):
    sys.exit("Enter valid message")

value_validator(zodiac_sign,1,12) #check if the input is in range 1 to 12

if zodiac_sign != 0:
    selected_day = daily_horoscope.date_selector()
    

    horoscope_text = daily_horoscope.horoscope(zodiac_sign, selected_day)
    print(horoscope_text)

elif zodiac_sign == 0:
    print("\nOk, don't worry. Soon you'll get it just pass this tiny quiz")

    your_birth_day = input("Enter your birthday day number (1-31): ")
    value_validator(int(your_birth_day),1,31)

    your_birth_month = int(input("Cool, and the month number, please (1-12) :"))
    value_validator(1-12)

    print("\nCongratulations! you are definately", daily_horoscope.check_sign(your_birth_day,your_birth_month))
    new_day = daily_horoscope.date_selector()
    horoscope_text = daily_horoscope.horoscope(your_birth_month, new_day)
    print(horoscope_text)


    


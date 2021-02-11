import daily_horoscope
from bs4 import BeautifulSoup
import requests



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
        "\nor if you're not sure about you sign, type 'calculate'",
    )

zodiac_sign = input("Please Enter valid number from the options given : ")

if zodiac_sign != "calculate":
        print("choose some day:\n", "yesterday\n", "today\n", "tomorrow\n")
        day = input("enter the day> ")
        horoscope_text = daily_horoscope.horoscope(zodiac_sign, day)
        print(horoscope_text)
else:
    print("\nOk, don't worry. Soon you'll get it just pass this tiny quiz")
    print("\nCongratulations! you are defenetly", daily_horoscope.check_sign()) 
    
    
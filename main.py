from engine import Weather,Image
import cv2
import os
from screeninfo import get_monitors
import numpy as np
import ctypes
import time

API_KEY = "" #put ur api here or create one >>>https://openweathermap.org/api
IMAGE_API = ""  # same here >>> https://unsplash.com/developers

while True:
    try:
        country_code = str(input("Enter your Country code :- "))
        zip_code = int(input("Enter your postal code :- "))  
        weather = Weather(country_code=country_code,zip_code=zip_code,API_KEY=API_KEY)

        lat,lon,city = weather.get_coords()

        res = str(input(f"{city}.... is it right ? (Y/N)"))
        if res == "y":
            break
        elif res== "n":
            pass
        else:
            print("Error")
            exit()
    except:
        print("incorrect")

prev_weather = None
weather_copy = weather
while True:
    try:
        weather = weather_copy.get_weather(lat,lon)
        print(f"current weather is {weather}")
        if prev_weather != weather:

            image = Image(IMAGE_API)
            img = image.get_url(weather)
            img_url = img["results"][0]["urls"]["full"]

            img = image.get_image(img_url)
            np_arr = np.frombuffer(img, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            for m in get_monitors():
                width,height = m.width, m.height

            img = cv2.resize(img,(width,height))

            if not os.path.exists("temp"):
                os.makedirs("temp")

            IMG_PATH = os.path.join("temp","image.jpg")
            IMG_PATH = os.path.abspath(IMG_PATH)

            cv2.imwrite(IMG_PATH,img)

            SPI_SETDESKWALLPAPER = 20
            SPIF_UPDATEINIFILE = 1
            SPIF_SENDCHANGE = 2

            ctypes.windll.user32.SystemParametersInfoW(
                SPI_SETDESKWALLPAPER,
                0,
                IMG_PATH,
                SPIF_UPDATEINIFILE | SPIF_SENDCHANGE
            )
            print("wallpaper changed")
            prev_weather = weather
        else:
            print("Weather is the same. No need to change wallpaper.")
        print("waiting 5min")
        time.sleep(5*60)

    except:
        print("Error waiting 1min")
        time.sleep(1*60)



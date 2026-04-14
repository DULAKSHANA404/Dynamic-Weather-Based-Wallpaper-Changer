import requests

class Weather():
    def __init__(self,country_code,zip_code,API_KEY):
        self.country_code = country_code
        self.zip_code = zip_code
        self.API_KEY = API_KEY

    def get_coords(self):
        city_link = f"http://api.openweathermap.org/geo/1.0/zip?zip={self.zip_code},{self.country_code}&appid={self.API_KEY}"
  
        result = requests.get(city_link)

        if result.status_code==200:
            result = result.json()
            lat,lon,city = result["lat"],result["lon"],result["name"]

            return lat,lon,city


    def get_weather(self,lat,lon):
            weather_link = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.API_KEY}"
            response = requests.get(weather_link)
            if response.status_code==200:
                result = response.json()
                weather = result["weather"][0]["description"]

                return weather
            
class Image():
    def __init__(self,api):
        self.api = api

    def get_url(self,weather):
        url = f"https://api.unsplash.com/search/photos?client_id={self.api}&query={weather}&per_page=1&page=1"
        responce = requests.get(url)

        if responce.status_code==200:
            result = responce.json()

            return result
         
    def get_image(self,url):
        respose = requests.get(url)
        if respose.status_code==200:
            result = respose.content
            return result
import requests
import json   

cityName = str(input("Enter City Name: "))
apiKey = "7be5004a9e54394423ab731f3a1f1007"  
 
def get_weather(api_key, city):
    try:
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" 
        response=requests.get(url).json() 
        temp_in_kelvin=response["main"]["temp"] 
        temp_in_degree=round(temp_in_kelvin - 273.15)  
        pressure=response["main"]["pressure"]
        humidity=response["main"]["humidity"] 
        wind_speed=response["wind"]["speed"] 
    except:
        raise IOError("Enter the correct city name")
    else:
        return { "temp":temp_in_degree, "pressure":pressure, "humidity":humidity, "wind_speed":wind_speed } 

print(get_weather(apiKey, cityName))  





    # return { "temp":temp_in_degree, "pressure":pressure, "humidity":humidity, "wind_speed":wind_speed } 

# print(get_weather(apiKey, cityName))  


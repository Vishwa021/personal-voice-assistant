import requests
API_Key = "f77a108a92a4c8c28adf9a1cb6967fb3"

def weather(address) -> str:
    #once we create the GUI we will replace the city input:
    city = address
    Base_url = "http://api.openweathermap.org/data/2.5/weather"

    #Creating the full URL 
    request_url = f"{Base_url}?appid={API_Key}&q={city}"

    # we'll store the response code here in get_weather
    response = requests.get(request_url)
    #extracting the Json file
    if response.status_code == 200:
        data = response.json() # Extract relevant weather information
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2) # Convert from Kelvin to Celsius
        feels_like = round(data['main']['feels_like'] - 273.15, 2)
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        # Print the results
        return f"Weather is {weather}, Temperature is {temperature} degree Celsius , Feels Like is {feels_like} degree Celsius, Humidity is {humidity} percentage, Wind Speed is {wind_speed} meter per second"
        
    else:
        return "City not found or error in the request."
    
# weath = weather("")
# print(weath)
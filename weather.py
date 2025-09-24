import requests
API_Key = "f77a108a92a4c8c28adf9a1cb6967fb3"

#once we create the GUI we will replace the city input:
city = input("Enter a city name: ")
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
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("City not found or error in the request.")
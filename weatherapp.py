import requests
api_key='1f95f041a54de2f4d981a6e92b44a8ce'
user_input=input("Enter city:")
weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&appid={api_key}")
weather=weather_data.json()['weather'][0]['main']
temp=weather_data.json()['main']['temp']
print(f"The weather in {user_input} is:{weather}")
print(f"The temperature in {user_input} is:{temp}F")

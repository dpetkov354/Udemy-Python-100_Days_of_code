import requests
import html
from datetime import datetime
from twilio.rest import Client

# Variables
time_now = datetime.now().hour
today_weather = []
rainy = False

# WEATHER PAI INFO
OWM_END_POINT = "https://api.openweathermap.org/data/2.5/onecall?"
api_key = 'INSERT HERE'

# TWILIO SMS API INFO
account_sid = 'INSERT HERE'
auth_token = 'INSERT HERE'

# API PARAMETERS

params = {
    "lat": 42.430894,
    "lon": 25.622741,
    "appid": 'INSERT HERE',
    "exclude": "current,minutely,daily"
}

# API WEATHER DATA

response = requests.get(OWM_END_POINT, params=params)
response.raise_for_status()
weather_data = response.json()

# MAKING A LIST OF WEATHER DATA

for hour in range(5, 18):
    current_weather = weather_data["hourly"][hour]["weather"][0]["id"]
    today_weather.append(current_weather)

# CHECKING IF THE WEATHER IS RAINING

for hourly_condition in today_weather:
    if hourly_condition < 700:
        rainy = True

# SMS sending with TWILIO
if rainy:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="From 06:00 to 18:00 it might rain, so bring an umbrella!☔",
        from_='PHONE NUMBER HERE',
        to='PHONE NUMBER HERE'
    )
    print(message.status)


######################### FOR PYTHON ANYWHERE ##############################
# import requests
# import os
# from datetime import datetime
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient
#
# # Variables
# time_now = datetime.now().hour
# today_weather = []
# rainy = False
#
# # WEATHER PAI INFO
# OWM_END_POINT = "https://api.openweathermap.org/data/2.5/onecall?"
# api_key = 'INSERT HERE'
#
# # TWILIO SMS API INFO
# account_sid = 'INSERT HERE'
# auth_token = 'INSERT HERE'
#
# # API PARAMETERS
#
# params = {
#     "lat": 42.430894,
#     "lon": 25.622741,
#     "appid": 'INSERT HERE',
#     "exclude": "current,minutely,daily"
# }
#
# # API WEATHER DATA
#
# response = requests.get(OWM_END_POINT, params=params)
# response.raise_for_status()
# weather_data = response.json()
#
# # MAKING A LIST OF WEATHER DATA
#
# for hour in range(5, 18):
#     current_weather = weather_data["hourly"][hour]["weather"][0]["id"]
#     today_weather.append(current_weather)
#
# # CHECKING IF THE WEATHER IS RAINING
#
# for hourly_condition in today_weather:
#     if hourly_condition < 700:
#         rainy = True
#
# # SMS sending with TWILIO
# if rainy:
#     proxy_client = TwilioHttpClient()
#     proxy_client.session.proxies = {'https': os.environ['https_proxy']}
#     client = Client(account_sid, auth_token, http_client=proxy_client)
#     message = client.messages.create(body="From 06:00 to 18:00 it might rain, so bring an umbrella!☔", from_='+18647635176', to='+359896877082')
#     print(message.status)

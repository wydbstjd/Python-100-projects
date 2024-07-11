import requests
from twilio.rest import Client

account_sid = 'ACe49cc55f2445da1c1b100a8b25040a5b'
auth_token = '62395b0f5000d20e7207f74a9ddcde0e'

api_key = "26b2690c05559a7396f701113f306e9f"
MY_LAT = 30.592850
MY_LONG = 114.305542

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.8/onecall", params=parameters)
response.raise_for_status()
data = response.json()

will_rain = False
for hour in data['hourly'][:12]:
    hour_weather = hour['weather']
    condition_code = hour_weather[0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today, Remember to bring an umbrella☔",
        from_='+15673392106',
        to='+821089207640'
    )

    print(message.sid)



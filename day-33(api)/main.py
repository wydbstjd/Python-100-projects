import requests

#1
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# #print(response.status_code)
# response.raise_for_status()
#
# data = response.json()
#
# longitude = data['iss_position']['longitude']
# latitude = data['iss_position']['latitude']
#
# iss_position = (longitude, latitude)

#
from datetime import datetime

MY_LAT = 37.610264
MY_LONG = 126.955245

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Seoul"
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"].split("T")[1].split(":")
sunset = data["results"]["sunset"].split("T")[1].split(":")

print(f"{sunrise[0]}:{sunrise[1]}")
print(f"{sunset[0]}:{sunset[1]}")\

time_now = datetime.now()

print(time_now)
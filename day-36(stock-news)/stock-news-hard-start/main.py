import requests
from twilio.rest import Client

account_sid = 'ACe49cc55f2445da1c1b100a8b25040a5b'
auth_token = '62395b0f5000d20e7207f74a9ddcde0e'

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = "5MRC9WM5VXLIX8KS"
NEWS_API_KEY = "f7f47988e56d4ebbbdac24c2cd69d7da"

STOCK_parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK_NAME,
    'apikey':STOCK_API_KEY
}

response = requests.get(STOCK_ENDPOINT, params=STOCK_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
day_list = [value for (key, value) in data.items()]

yesterday_data = day_list[0]
yesterday_closing_price = yesterday_data['4. close']

day_before_yesterday_data = day_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data['4. close']

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "🔼"
else:
    up_down = "🔽"
diff_percent = round(difference / float(yesterday_closing_price) * 100)

if abs(diff_percent) > 5:
    NEWS_parameters = {
        'q': STOCK_NAME,
        'apiKey': NEWS_API_KEY
    }

    response = requests.get(NEWS_ENDPOINT, params=NEWS_parameters)
    response.raise_for_status()
    articles = response.json()['articles']

    three_articles = articles[:3]
    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%H\neadline: {article['title']}, \nBrief: {article['content']}" for article in three_articles]

    print(formatted_articles)
    # client = Client(account_sid, auth_token)
    #
    # for article in formatted_articles:
    #     message = client.messages.create(
    #         body=article,
    #         from_='+15673392106',
    #         to='+821089207640'
    #     )
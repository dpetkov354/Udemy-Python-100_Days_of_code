import requests
import html2text
from datetime import datetime, timedelta
from twilio.rest import Client

# TWILIO ACCOUNT INFO #
account_sid = 'INSERT HERE'
auth_token = 'INSERT HERE'

# STOCK INFO TESLA FROM#
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "datatype": "json",
    "apikey": "INSERT HERE"
}
response = requests.get(STOCK_ENDPOINT, params=params)
response.raise_for_status()
stock_data = response.json()

# YESTERDAY DATA #

yesterday_time = str(datetime.today() - timedelta(days=3))  # trial with 3days delay because data is delayed
yesterday_time_list = yesterday_time.split(" ")
yesterday = yesterday_time_list[0]
yesterday_closing = float(stock_data["Time Series (Daily)"][yesterday]["4. close"])

# BEFORE YESTERDAY DATA #

before_yesterday_date = str(datetime.today() - timedelta(days=4))
before_yesterday_time_list = before_yesterday_date.split(" ")
before_yesterday = before_yesterday_time_list[0]
before_yesterday_closing = float(stock_data["Time Series (Daily)"][before_yesterday]["4. close"])

# ABS DIFF BETWEEN BEFORE_YESTERDAY AND YESTERDAY AND PERCENTAGE#
abs_diff = abs(yesterday_closing - before_yesterday_closing)
percentage = round(((abs_diff / yesterday_closing) * 100), 2)


# If % is > 5 THEN SEND NEWS TO PHONE#
if percentage > 5:
    # NEWS INFO TESLA OF THE TOP # ARTICLES #
    NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
    param_news = {
        "q": STOCK_NAME,
        "from": yesterday,
        "sortBy": "popularity",
        "apiKey": "ef7bae61ba564d9a925c56165ad90ace",
        "language": "en"
    }

    response = requests.get(NEWS_ENDPOINT, params=param_news)
    response.raise_for_status()
    news_data = response.json()
    top_three_articles_data = news_data["articles"][0:3]

    # LIST OF HEADLINES, DESCRIPTION and URL's #
    published = []
    top_three_articles_headlines_list = []
    description_list = []
    list_of_url = []
    for i in range(0, 3):
        publish_date = news_data["articles"][i]["publishedAt"].split("T")[0]
        published.append(publish_date)
        headline = news_data["articles"][i]["title"]
        top_three_articles_headlines_list.append(headline)
        url = news_data["articles"][i]["url"]
        list_of_url.append(url)

        # FORMATTING DESCRIPTION #
        description = news_data["articles"][i]["description"]
        description_escape_html = html2text.html2text(description)
        description_escape_html_final = description_escape_html.replace("\n", " ")
        description_list.append(description_escape_html_final)

    # CREATE A MESSAGE WITH URLS and SMS sending with TWILIO #

    for j in range(0, 3):
        date = published[j]
        heading = top_three_articles_headlines_list[j]
        descr = description_list[j]
        exact_url = list_of_url[j]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{date}-{heading}\n{descr}\n{exact_url}",
            from_='PHONE NUMBER HERE',
            to='PHONE NUMBER HERE'
        )
        print(message.status)

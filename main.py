import requests
from twilio.rest import Client

# STOCK NAME
STOCK = "MSFT"
# COMPANY NAME
COMPANY_NAME = "Microsoft Corporation"

# Alphavantage api key
STOCK_PRICE_API_KEY = "YOUR API KEY HERE"
# Newsapi.org api key
NEWS_API_KEY = "YOUR API KEY HERE"

# Your Twilio Credentials
account_sid = "YOUR ACCOUNT SID HERE"
auth_token = "YOUR AUTH TOKEN HERE"
twilio_phone_number = 'YOUR TWILIO VIRTUAL PHONE NUMBER HERE'

# Your actual phone number which you used to register to twilio
your_phone_number = "YOUR ACTUAL PHONE NUMBER FOR RECEIVING SMS"


# ************************ Don't make any changes below **************************
# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price_api_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_PRICE_API_KEY,
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_price_api_params)
response.raise_for_status()
data = response.json()
minimized_data = data['Time Series (Daily)']
date_list = list(minimized_data)

yesterday_close = float(minimized_data[date_list[0]]['4. close'])
day_before_yesterday_close = float(minimized_data[date_list[1]]['4. close'])

difference = yesterday_close - day_before_yesterday_close

is_up = ""
if difference > 0:
    is_up = "🔺"
else:
    is_up = "🔻"

percentage_diff = round(((abs(difference)/yesterday_close) * 100))
print(percentage_diff)


if percentage_diff >= 1:
    print("Get News")
    # STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
    news_api_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_api_params)
    response.raise_for_status()
    news_data = response.json()
    top_3_news = news_data['articles'][:3]
    news_title_list = [i['title'] for i in top_3_news]
    news_description_list = [j['description'] for j in top_3_news]

    # STEP 3: Use https://www.twilio.com
    # Send a separate message with the percentage change and each article's title and description to your phone number.
    for i in range(3):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}{is_up}{percentage_diff}%\n\nHeadline: {news_title_list[i]}\n\nNews: {news_description_list[i]}",
            from_=twilio_phone_number,
            to=your_phone_number)
        print(message.status)

# import requests

# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"

# STOCK_ENDPOINT = "https://www.alphavantage.co/query"
# NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# STOCK_API_KEY = ""
# NEWS_API_KEY = ""
# TWILIO_ACCOUNT_SID = ""
# TWILIO_AUTH_TOKEN = ""


#Get yesterday's closing stock price.
# stock_params = {
#     "function": "TIME_SERIES_DAILY",
#     "symbol": STOCK_NAME,
#     "apikey": STOCK_API_KEY,
# }

# response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()["Time Series (Daily)"]

# data_list = [value for (key, value) in list.items()]

# yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
# print(yesterday_closing_price)


#Get the day before yesterday's closing stock price
# day_before_yesterday_data = data_list[1]
# day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
# print(day_before_yesterday_closing_price)


#Find the positive difference between 1 and 2.
# difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
# print(difference)
# if difference > 0:
#     up_down = "🔼"
# else:
#     up_down = "🔽"


#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
# diff_percentage = round((difference / float(yesterday_closing_price)) * 100)
# print(diff_percentage)
#_____________________________________________________

# SERVER RESPONSE
# {
#   "status": "ok",
#   "totalResults": 12345,
#   "articles": [
#     {
#       "source": {
#         "id": "cnn",
#         "name": "CNN"
#       },
#       "author": "John Doe",
#       "title": "Example News Headline",
#       "description": "A brief description or snippet from the article.",
#       "url": "https://example.com/article-url",
#       "urlToImage": "https://example.com/image.jpg",
#       "publishedAt": "2025-09-01T10:00:00Z",
#       "content": "The unformatted content of the article, truncated to 200 characters..."
#     },
#     // ... more article objects
#   ]
# }

# import requests

# new_response = requests.get(ENDPOINT,PARAMS={
#   'api_key': NEWS_API_KEY,
#   'qInTitle': COMPANY_NAME
# })

# articles = new_response.json('articles')
# three_articles = articles[:3]

# LIST COMPREHENSION

# [new_item for item in list]
# formatted_articles_list = [f"{STOCK_NAME}: {up_down}{diff_percentage}% \nYesterday's closing price: {yesterday_closing_price}$ \nDay before yesterday's closing price: {day_before_yesterday_closing_price}$ \nHeadline: {article['title']}. \nBreif: {article['description']}" for article in three_articles]

# SEND SMS
# client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# for article in formatted_articles:
#   message = client.message.create(
#     body=article,
#     from_='+79092347453'
#     to_='+74532343454'
#   )
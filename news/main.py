'''import requests
import json

query = input("enter your preferred field ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2024-08-13&sortBy=publishedAt&apiKey=f14c53fc782a4c2d8c78fa8f1299708a"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article['author'])
    print(article['title'])
    print(article['description'])
    print("---------------------------------------------------------------")
    '''
# chat gpt code
import requests
import json
from datetime import datetime

# Get the user's preferred field
query = input("Enter your preferred field: ")

# Calculate today's date
today_date = datetime.now().strftime("%Y-%m-%d")

# Construct the URL with the `to` parameter set to today's date and language filter for English
url = f"https://newsapi.org/v2/everything?q={query}&to={today_date}&sortBy=publishedAt&language=en&apiKey=f14c53fc782a4c2d8c78fa8f1299708a"

# Make the API request
r = requests.get(url)

# Check if the request was successful
if r.status_code == 200:
    news = json.loads(r.text)
    # Print the articles
    for article in news["articles"]:
        print(f"Author: {article.get('author', 'N/A')}")
        print(f"Title: {article.get('title', 'N/A')}")
        print(f"Description: {article.get('description', 'N/A')}")
        print("-----------------------------------------------------------------")
else:
    print(f"Failed to fetch news. Status code: {r.status_code}")
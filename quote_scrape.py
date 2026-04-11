import pandas
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

data = []


URL = "https://quotes.toscrape.com/"

response = requests.get(URL)

html_data = response.text

soup = BeautifulSoup(html_data, parser="html.parses", features="lxml")

quotes = soup.find_all(class_="quote")

for quote in quotes:
    text = quote.find(class_="text").get_text()
    author = quote.find(class_="author").get_text()
    tags = [tag.get_text() for tag in quote.find_all(class_="tag")]

    data.append({"quote": text, "author": author, "tags": tags})
#
# print(data)

df = pandas.DataFrame(data)
df.to_csv("quotes.csv", index = False)

print(df.count())
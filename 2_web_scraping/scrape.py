import requests
from bs4 import BeautifulSoup


url = "https://quotes.toscrape.com/"

response = requests.get(url)
# print(response.text)
soup = BeautifulSoup(response.text, "lxml")

# print(soup)

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")

no_of_quotes = len(quotes)

for quote in range(no_of_quotes):
    # print(quotes[quote].text)
    _text = "{} by {}".format(quotes[quote].text, authors[quote].text)
    print(_text)
    quote_tags = tags[quote].find_all("a", class_="tag")
    all_tags =[tag.text for tag in quote_tags]
    print("Tags: " + ", ".join(all_tags))
    print("-" * 20)

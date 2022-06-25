import requests
from bs4 import BeautifulSoup

base_url = "https://scrapingclub.com/exercise/list_basic/"

response = requests.get(base_url)
soup = BeautifulSoup(response.text, "lxml")

page_bar = soup.find("ul", class_="pagination")
pages = page_bar.find_all("a", class_="page-link")
urls = [base_url]
for page in pages:
    page_num = int(page.text) if page.text.isdigit() else None
    if page_num is not None:
        url = page["href"]
        urls.append(base_url + url)

print(urls)

item_count = 0
for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    items = soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")

    for item in items:
        item_count += 1
        item_name = item.find("h4", class_="card-title").text.strip()
        price = item.find("h5").text.strip()
        _text = "{}) {} is priced at {}".format(item_count, item_name, price)
        print(_text)
        print("-" * 50)

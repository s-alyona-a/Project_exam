import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.lib.ru/INOOLD/DUMA/")
soup = BeautifulSoup(response.text, 'html.parser')
urls = soup.find_all('a', 'href' == True)
urls = urls[30:31:] + urls[34:65:2]
urls_book = []
for url_book in urls:
    urls_book.append(url_book.get("href"))

# making full text of all books
main_url = "http://www.lib.ru/INOOLD/DUMA/"
full_text = ""
for url_book in urls_book:
    url = main_url + url_book
    response1 = requests.get(url)
    soup1 = BeautifulSoup(response1.text, 'html.parser')
    text = soup1.get_text().replace("\n", " ")
    full_text += text
with open("train_text.txt", "w") as outp_f:
    outp_f.write(full_text)

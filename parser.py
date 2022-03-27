from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
import urllib.parse
ua = UserAgent()
# headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
urls_of_books=[]
names_of_books=[]
url = 'https://briefly.ru/search/?q='
book_name = ''
def get_url(name):
    global book_name, url
    url = 'https://briefly.ru/search/?q='
    book_name = name
    mass = name.split()
    print(mass)
    if len(mass) > 1:
        for i in range(len(mass)):
            url+= urllib.parse.quote_plus(mass[i])
            if i != range(len(mass)-1):
                url += '+'
    elif len(mass) == 1:
        url += urllib.parse.quote_plus(name)
    get_info_books(get_html(url))
    print(urls_of_books)
    print(names_of_books)
    return name



def get_html(urlka):
    response = requests.get(urlka)
    if response.status_code == 200:
        result = requests.get(urlka)
        return result.text

def get_info_books(html):
    soup = BeautifulSoup(html, 'lxml')
    for i in soup.find_all('div', class_="gs-title"):
        urls_of_books.append(i.get('href'))
        names_of_books.append(i.find('b').text)

def debbug():
    print(url)
    get_info_books(get_html(url))
    return book_name



get_info_books(get_html('https://briefly.ru/search/?q=%D0%B2%D0%BE%D0%B9%D0%BD%D0%B0+%D0%B8+%D0%BC%D0%B8%D1%80+'))

print(urls_of_books)
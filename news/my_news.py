import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs


ua = UserAgent()
header = {
    'User-Agent':  str(ua.chrome),
}
# print(ua.chrome)


try:
    r = requests.get(url, headers=header)
except Exception as err:
    print(f'Error fetching the URL {url}')
    print(err)

# soup = bs(r.text, "html.parser")
soup = bs(r.text, "xml")

lst = []
for item in soup.find_all('item'):
    dct = {
            'title': item.title.text, 
            'description': item.description.text,
            'enclosure': item.enclosure.get('url'),
        } 
    lst.append(dct)

print(lst)
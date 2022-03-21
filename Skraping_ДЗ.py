
import requests
import bs4
from attr import attrs

from pprint import pprint




url = 'https://habr.com/ru/all/'

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
response = requests.get(url)
links = []

if not response.ok:
    raise ValueError('No response')

text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')

# pprint(text)
# pprint(soup)
# Ищем все статьи на сайте.
articles = soup.find_all('article')

# pprint(articles)
# Проходим вложенным циклом по всем статьям.
for article_all in articles:
    for hubs in article_all.find_all('a', class_='hub-link'):
        hubs = {hubs, text.lower()}
        if KEYWORDS & hubs:
            href = article_all.find('a', class_='post_title_link').attrs.get('href')
            name = article_all.find('a', class_='post_title_link').text
            pprint(href, name)
            links.append(href)
            pprint('Совпадение в Тэгах:', name, ':', href)

    href = article_all.find('a', class_='post_title_link').attrs.get('href')
    if href not in links:
        response = requests.get(href)
        if not response.ok:
            raise ValueError('No response')
        text = response.text
        soup = BeautifulSoup(text, features='html.parser')
        for words in soup.find_all('div', class_='post_body'):
            words = words.text.lower().split()
            words = set(words)
            if KEYWORDS & words:
                name = article_all.find('a', class_='post_title_link').text
                pprint('Совпадение в тексте:', name, ':', href)




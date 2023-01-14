import requests
import bs4
from fake_useragent import UserAgent
from task_1 import logger


url = 'https://habr.com/ru/all/'
ua = UserAgent()
HEADERS = {'accept': '*/*', 'user-agent': ua.opera}
KEYWORDS = ['JavaScript', 'текст', 'QA', 'python']

@logger
def main():
    response = requests.get(url, headers=HEADERS)
    text = response.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    articles = soup.find_all('article')
    for article in articles:
        hubs = article.find_all(class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
        hubs = [hub.text.strip() for hub in hubs]
        for hub in hubs:
            for keyword in KEYWORDS:
                if keyword in hub:
                    date = article.find('time')['title']
                    href = article.find(class_='tm-article-snippet__title-link')['href']
                    full_url = f'{url}{href}'
                    title = article.find(class_='tm-article-snippet__title-link').find('span')
                    # title = article.find('h2').find('span').text
                    return f'<{date}> - <{title.text}> - <{full_url}>'
                else:
                    pass


if __name__ == '__main__':
    print(main())

from bs4 import BeautifulSoup
import requests


persons_page_urls = []
wordlist = []
alpha = 'А'
for i in range(0, 32):
    wordlist.append(alpha)
    alpha = chr(ord(alpha) + 1)


for word in wordlist:
    url = f"https://urfu.ru/ru/about/personal-pages/Personal/index/?tx_urfupersonal_personal%5Balpha%5D={word}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    q = requests.get(url, headers=headers)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    persons = soup.find_all('p', class_='name')
    for person in persons:
        urls = person.find_all('a')
        persons_page_urls.append(urls[0].get('href'))
        print(urls[0].get('href'))


with open('personal_urls.txt', 'a') as file:
    for line in persons_page_urls:
        file.write(f'{line}\n')
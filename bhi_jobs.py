# pipenv install requests
import requests
# pipenv install beautifulsoup4
from bs4 import BeautifulSoup

url = 'https://bhico.applicantpro.com/jobs/'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537/6',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'origin': url,
    'referer': url
}

page = requests.get(url, headers=HEADERS)

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.find_all('a')

for link in links:

  link_ref = link['href']
  title = link.find('h4')
  if title:
    title = title.text.strip()

  info = link.find('ul', class_='listing-details')
  if info:
    info = info.text.strip()

  print(f'{link_ref}\n{title}\n{info}\n')
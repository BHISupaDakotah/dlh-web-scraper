# pipenv install requests
import requests
# pipenv install beautifulsoup4
from bs4 import BeautifulSoup

# url = 'https://www.groupon.com/browse/salt-lake-city?lat=40.297&lng=-111.695&query=escape+room&address=Orem%2C+UT&division=salt-lake-city&locale=en_US'
url = 'https://www.groupon.com/browse/denver?lat=39.739&lng=-104.99&query=yoga%5D&address=Denver%2C+CO&division=denver&locale=en_US'

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537/6',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'origin': url,
    'referer': url
}

page = requests.get(url, headers=HEADERS)

# with open('group.html', 'wb') as outfile:
#   outfile.write(str(page.content))

# with open('group.html', 'rb') as infile:
#   page = infile.read()
soup = BeautifulSoup(page.content, 'html.parser')

deals = soup.find_all('div', class_='cui-content')

for deal in deals:
  title = deal.find('div', class_="cui-udc-title")
  if title:
    title = title.text.strip()

  location = deal.find('span', class_='cui-location-name')
  if location:
    location = location.text.strip()

  reg_price = deal.find('div', class_='cui-price-original')
  if reg_price:
    reg_price = reg_price.text.strip()

  discount_price = deal.find('div', class_='cui-price-discount')
  if discount_price:
    discount_price = discount_price.text.strip()

  final_price = deal.find('div', class_='cui-verbose-urgency-price')
  if final_price:
    final_price = final_price.text.strip()


    print(f'{title}\n{location}\nRegular Price: {reg_price}\nDiscount Price: {discount_price}\nFinal Price: {final_price}\n\n')
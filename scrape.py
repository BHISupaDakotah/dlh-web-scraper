# pipenv install requests
import requests
# pipenv install beautifulsoup4
from bs4 import BeautifulSoup

url = 'https://realpython.github.io/fake-jobs/'

page = requests.get(url)

# page_text = page.text

soup = BeautifulSoup(page.content, 'html.parser')

# print(soup)
# job_titles = soup.find_all('h2')

# for job in job_titles:
#   print(job.text)

card_content_tags = soup.find_all('div', class_='card-content')

for job in card_content_tags:
  job_title = job.find('h2')
  if job_title:
    job_title = job_title.text.strip()
  
  company = job.find('h3', class_='company')
  if company:
    company = company.text.strip()

  location = job.find('p', class_='location')
  if location:
    location = location.text.strip()
   
  date = job.find('time')
  if date:
    date = date.text.strip()

  footer = job.find('footer')
  links = footer.find_all('a')

  desciption =  ''
  link_href = ''
  for link in links:
    # print(link)
    if link.text =='Apply':
      link_href = link['href']

      # load detail page to get the decription
      detail_page = requests.get(link_href)
      detail_page_soup = BeautifulSoup(detail_page.content, 'html.parser')

      content = detail_page_soup.find('div', class_='content')
      desciption = content.find('p')
      if desciption:
          desciption = desciption.text.strip()

  print(f'{job_title}..{company}\n{location}..{date} \n{desciption}\n{link_href}\n')
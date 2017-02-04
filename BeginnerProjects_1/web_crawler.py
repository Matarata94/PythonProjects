import requests
from bs4 import BeautifulSoup

def spider(max_pages):
     page = 1
     while page <= max_pages:
         url  = 'http://www.downloadha.com/page/' + str(page)
         source_code = requests.get(url)
         plain_text = source_code.text
         soup = BeautifulSoup(plain_text,"html.parser")
         for link in soup.findAll('a',{'class':'more-link'}):
             href = link.get('href')
             #title = link.string
             #print(href,"  ",title)
             get_single_item_data(href)
         page += 1

def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for item_name in soup.findAll('h1', {'class': 'entry-title'}):
        print(item_name.string)



spider(3)
from bs4 import BeautifulSoup

soup = BeautifulSoup("<html> <p>ajkndf <a> Hello </html>","html.parser")
print(soup.prettify())

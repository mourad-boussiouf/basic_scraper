from bs4 import BeautifulSoup

with open('C:\wamp64\www\basic_scraper\webscraping\home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    print(soup.prettify())
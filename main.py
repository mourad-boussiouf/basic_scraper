from cgitb import html
from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, "html.parser")
    print(soup.prettify())
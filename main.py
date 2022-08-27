import re
import requests
from urllib.parse import urlsplit
from collections import deque
from bs4 import BeautifulSoup
import pandas as pd
from google.colab import files

original_url = input("https://laplateforme.io/") 
 
unscraped = deque([original_url])
 
scraped = set()
 
emails = set()

while len(unscraped):
    
    url = unscraped.popleft() 
    scraped.add(url)
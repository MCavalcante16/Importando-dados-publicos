#Dependencies
!pip install bs4
!pip install urllib.request

#Imports
import urllib.request
from bs4 import BeautifulSoup

#Obtem os hrefs
soup = BeautifulSoup(html_string, 'html.parser')
hrefs = []
common_substring = 'DADOS_ABERTOS_CNPJ_'
for a in soup.find_all('a', href=True):
    this = a['href']
    if (common_substring in this):
        hrefs.append(this)


#Baixa os zips
for href in hrefs:
    url = 'http://200.152.38.155/CNPJ/' + href
    urllib.request.urlretrieve(url, href)
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')

j = 7
while j>0:
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    i = 18
    for tag in tags:
        if i>0:
            url = tag.get('href', None)
            i = i - 1
        else: break
    j = j - 1
print(url)

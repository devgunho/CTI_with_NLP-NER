import requests
from bs4 import BeautifulSoup

def start():
    req=requests.get('https://www.microsoft.com/security/blog/')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print(html)

if __name__ == "__main__":
    start()
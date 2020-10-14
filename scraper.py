from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


def url_scrape(url):
    downloadable = []
    req = Request(url, headers={'User-Agent': "Mozilla/5.0"})
    html = urlopen(req).read()
    soup = BeautifulSoup(html, 'lxml')
    all_links = soup.find("div", {'class': 'container divcontent'})
    linker = all_links.find_all("a")
    for l in linker:
        downloadable.append(l.get("href"))
    return  downloadable

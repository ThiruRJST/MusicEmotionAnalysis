from scraper import url_scrape
import numpy as np


def LinkGen(url):
    d = []
    downloads = []

    url1 = "https://www.fesliyanstudios.com"
    links = url_scrape(url)
    # print(links)
    for l in links:
        d.append(str(l.startswith("/download")))
    d = np.asarray(d)
    mask = np.where(d == "True")
    for i in mask:
        for j in i:
            downloads.append(url1 + links[j])
    return downloads

import pandas as pd
from tqdm import tqdm
import requests
import random



def downloader(df):
    link = df.links.values
    for i in tqdm(range(len(link))):
        l = link[i]
        r = requests.get(l, stream=True)
        with open(df.paths.iloc[i] +"/"+ str(random.random()) + ".mp3", "wb") as mus:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    mus.write(chunk)




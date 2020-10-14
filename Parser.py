import pandas as pd
from SubProcess import LinkGen
import numpy as np
from tqdm import tqdm

data = pd.read_csv("/home/thirumalaikumar/PycharmProjects/pythonProject/links", delimiter=",")
FOLDERS = data.label.values
links = data.links.values


def parsed( Path ):

    dlinks = []
    k = []

    for i in range(len(FOLDERS)):
        label = FOLDERS[i]
        dlinks.append(LinkGen(links[i]))
        for j in dlinks[i]:
            k.append([j,label])
    data_csv = pd.DataFrame(index=np.arange(len(k)), columns=['links', 'labels'])
    for m in tqdm(range(len(k))):
        data_csv['links'].iloc[m]=k[m][0]
        data_csv['labels'].iloc[m]=k[m][1]
    print("Saving...")
    data_csv.to_csv(Path+"data_scraped.csv")
    print("Completed :)")






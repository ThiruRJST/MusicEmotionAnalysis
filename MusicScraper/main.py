from Parser import parsed
from Downloader import downloader
import pandas as pd

parsed("/home/thirumalaikumar/EmotionalSpeechAnalysis/Musics/")

data = pd.read_csv("data_scraped.csv")
data = data.drop(["Unnamed: 0"], axis=1)
data['paths'] = "/home/thirumalaikumar/EmotionalSpeechAnalysis/Musics/" + data.labels

downloader(data)

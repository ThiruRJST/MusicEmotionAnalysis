# MusicEmotionAnalysis

**Difference between happy and sad tunes**

![Happy Tune](https://github.com/ThiruRJST/MusicEmotionAnalysis/blob/main/happy_tune.jpg) ![Sad Tune](https://github.com/ThiruRJST/MusicEmotionAnalysis/blob/main/sad_tune.jpg)


### Exploratory Data Analysis: <a>https://www.kaggle.com/kingofarmy/audioeda</a>(*I would regularly update my EDA on the dataset*)

This repository is my trial of emotion analysis using musics. I have uploaded my webscraper for scraping musics from <a>https://www.fesliyanstudios.com/</a>

The scraped data contains seven classes. If you want to scrape the data :
1. Clone the repository
2. Open a terminal
3. `cd` into the repository
4. run `python3 main.py`
5. if you want to increase the speed of the download, just change the buffer size in Downloader.py

## Chunking Large Audio Files into Equal smaller chunks
**There are two methods to divide a large audio files into smaller chunks:**
1. You can write a script using Pydub (<a>https://www.geeksforgeeks.org/audio-processing-using-pydub-and-google-speechrecognition-api/</a>) OR
2. Use ffmpeg package to do this step for you, using CLI version or the python-ffmpeg package(Official Document:<a>https://github.com/kkroening/ffmpeg-python</a>)

**I used the second method with CLI version since I found that simple and easy for me. But, You can go with any of those two methods mentioned above**

  ### Code:
  1. `cd` into the directory where the scraped data is stored.
  2. `for file in *.mp3; do ffmpeg -i "$file" -f segment - segment_time 10 -c copy "${file:0:4}"%02d.mp3; done`
  3. This command will create chunks for all large audio files contained in a directory.
  4. The Chunks of the same song will have continious numbers with which you can identify the chunks of a same song. The original song will be retained separately





**IF YOU WANT TO PLAY WITH THE PERFECT AND PREPROCESSED DATASET VISIT:<a>https://www.kaggle.com/kingofarmy/musical-emotions-classification</a>**




# TO-DO
- [x] Scraping the data
- [x] Chunking the audio files
- [x] Preprocessing and Augmentation
- [ ] Architecture Design
- [ ] Model Training
- [ ] Testing the model
- [ ] Deployment







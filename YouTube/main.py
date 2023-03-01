from pytube import YouTube
from sys import argv
import os

link = argv[1]
path = argv[2]

try:
    yt = YouTube(link=link)

    print(">> Title", yt.title)
    print()
    print(">> Views", yt.views)

    yd = yt.streams.get_highest_resolution()
    yd.download(path)

except:
    print("Error...Check internet connection !")
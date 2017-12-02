from pytube import YouTube
link = input("YouTube Link: ")
yt = YouTube(link)
yt.streams.first().download()

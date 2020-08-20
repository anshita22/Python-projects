from pytube import YouTube
yt  = YouTube("https://www.youtube.com/watch?v=TH3d5cyeer0").streams.first().download("E:/")
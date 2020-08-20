from pytube import YouTube

yt= YouTube("https://www.youtube.com/watch?v=UT58ETAj3cg")

dw= yt.streams.get_by_itag(22)
dw.download("E:/")
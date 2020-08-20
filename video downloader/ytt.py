from pytube import YouTube

video_list= open("sample.txt", "r")

for i in video_list:
    yt= YouTube(i)
    try:
        dw= yt.streams.first()
        dw.download("F:/")
        print("downloaded", i)
    except:
        print ("download failed")

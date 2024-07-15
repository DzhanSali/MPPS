from pytube import YouTube
import os

while True: 
   
    # url input from user
    yt = YouTube(input("Enter the URL of the video you want to download: \n>> "))
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # replace destination with the path where you want to save the downloaded file
    destination = "C:/Users/destination"
    
    out_file = video.download(output_path=destination)
    
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    
    tit = yt.title + " has been successfully downloaded."
    
    print("\033[32m" + tit + "\033[0m")
    #print(yt.title + " has been successfully downloaded.")
    # The most frequent exception thrown by this code is usually related to outdated pytube packages,
    # so you can just run the line below every time before you begin downloading music (just to be sure).
    #pip install --upgrade pytube

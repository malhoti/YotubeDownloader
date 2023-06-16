from pytube import YouTube
from pathlib import Path
import os
from moviepy.editor import *



def Download(link):
    
    youtubeObject = YouTube(link,use_oauth=True, allow_oauth_cache=True)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")

def DownloadAudio():
    # url input from user
    yt = YouTube(
        str(input("Enter the URL of the video you want to download: \n>> ")),use_oauth=True, allow_oauth_cache=True)
    
    # extract only audio
    video = yt.streams.filter(only_audio=True).first()
    
    # check for destination to save file
    #print("Enter the destination (leave blank for current directory)")
    destination = "EDIT INTO DOWNLOAD DESTIONATION"
    
    # download the file
    try:
        mp4_file = video.download(output_path=destination)
    except:
        print("An error has occurred")
    
    
    # save the file
    print(mp4_file)
    base, ext = os.path.splitext(mp4_file)
    mp3_file = base + '.mp3'
    MP4ToMP3(mp4_file,mp3_file)
    os.rename(mp4_file, mp3_file)
    
    # result of success
    print(yt.title + " has been successfully downloaded.")

#url = input("Enter youtube url: ")





def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()

DownloadAudio()


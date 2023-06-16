import os
from moviepy.editor import *
from pathlib import Path

dir = r"C:\Users\malho\Documents\Mal Hoti\Python\pythonProjects\YoutubeVideoDownloader\EDIT INTO DOWNLOAD DESTIONATION" 
arr = os.listdir(dir)
print(arr)

def MP4ToMP3(mp4, mp3):
    FILETOCONVERT = AudioFileClip(mp4)
    FILETOCONVERT.write_audiofile(mp3)
    FILETOCONVERT.close()


def ConvertNameToMP4(mp3_file):
    base, ext = os.path.splitext(mp3_file)
    mp4_file = base + '.mp4'
    print(mp4_file)
    os.rename(mp3_file, mp4_file)


# for file in arr:
#     fullpath = os.path.abspath(os.path.join(dir, file))
#     print(fullpath)
#     ConvertNameToMP4(fullpath)

arr = os.listdir(dir)
for corruptmp3 in arr:
    fullpath = os.path.abspath(os.path.join(dir, corruptmp3))
    
    MP4ToMP3(fullpath, fullpath)


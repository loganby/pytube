import os.path
import subprocess
from os import path
from pytube import YouTube
from pytube import Playlist

#https://pypi.org/project/pytube/
print('PyTube playlist download')

playlist = Playlist("https://www.youtube.com/playlist?list=PLkTWwRz9wG-Mm1lpyDefj8w0pYsaY3ByS")
localFolder = r"C:\mp3"

#Output the song count.  If this is 0, then perhaps your YT playlist is private.
print('Songs in playlist : ', len(playlist))

#Iterate through each item in the playlist
for url in playlist:
    print('Getting metadata for',url)

    #Download the songs locally as MP4, to wherever this script is run from
    ytStream=YouTube(url).streams.filter(only_audio=True).first()
    streampath=os.path.join(localFolder, ytStream.default_filename)
    if not path.exists(streampath):
        print('--Downloading: ',ytStream.default_filename)
        ytStream.download(localFolder)
    else:
        print('--Skipping: ',ytStream.default_filename)

    #Convert MP4 to MP3
    ytStreamNameMp3=ytStream.default_filename.replace("mp4","mp3")
    newFilePath=os.path.join(localFolder , 'mp3' , ytStreamNameMp3)
    if not path.exists(newFilePath):
        print('--Adding mp3 copy: ',ytStreamNameMp3)
        subprocess.run([
            'ffmpeg',
            '-n',
            '-i', os.path.join(localFolder, ytStream.default_filename),
            newFilePath
        ])
    else:
        print('--Skipping mp3 copy: ',ytStreamNameMp3)

#TODO: Update the RekordBox XML database
#https://github.com/Gordonby/rekordbox-scripts

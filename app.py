import os.path
from os import path
from pytube import YouTube
from pytube import Playlist

#https://pypi.org/project/pytube/
print('PyTube playlist download')

playlist = Playlist("https://www.youtube.com/playlist?list=PL_wl2s89QANvoYBull1jx7pqNaiC6n8xl")
localFolder = r"C:\Users\gobyers\OneDrive\DJ"

#Output the song count.  If this is 0, then perhaps your YT playlist is private.
print('Songs in playlist : ', len(playlist))

#Download the songs locally as MP4, to wherever this script is run from
for url in playlist:
    print('Getting metadata for',url)
    ytStream=YouTube(url).streams.filter(only_audio=True).first()
    if not path.exists(localFolder + '\\' + ytStream.default_filename):
        print('--Downloading',ytStream.default_filename)
        ytStream.download(localFolder)

#TODO: Update the RekordBox XML database
#https://github.com/Gordonby/rekordbox-scripts

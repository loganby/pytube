from pytube import YouTube
from pytube import Playlist

#https://pypi.org/project/pytube/
print('PyTube playlist download')

playlist = Playlist("https://www.youtube.com/playlist?list=PL_wl2s89QANvoYBull1jx7pqNaiC6n8xl")

#Output the song count.  If this is 0, then perhaps your YT playlist is private.
print('Songs in playlist : ', len(playlist))

#List the songs in the playlist.
for url in playlist:
    print(url)

#Download the songs locally as MP4, to wherever this script is run from
for url in playlist:
    YouTube(url).streams.filter(only_audio=True).first().download()

#TODO: Update the RekordBox XML database
#https://github.com/Gordonby/rekordbox-scripts
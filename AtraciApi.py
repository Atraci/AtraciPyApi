#!/usr/bin/python
#!/Applications/MAMP/Library/bin/python2.7
import sys
import cgi
import json
import Request
import LastFmApi
import ItunesApi
import SoundCloudApi

#Atraci API, Rest service
requestHandler = Request.requestHandler()

#SearchObject Class
class SearchObject(object):
    _search=_artist=_album=_song= ""

    @property
    def search(self):
        return self._search
    @search.setter
    def search(self, search):
        self._search = search
    
    @property
    def artist(self):
        return self._artist
    @artist.setter
    def artist(self, artist):
        self._artist = artist
    
    @property
    def album(self):
        return self._album
    @album.setter
    def album(self, album):
        self._album = album
    
    @property
    def song(self):
        return self._song
    @song.setter
    def song(self, song):
        self._song = song

form = cgi.FieldStorage()
# print form.keys()
searchObject = SearchObject()

if "search" in form:
    searchObject.search = form["search"].value
    searchObject.search = requestHandler.encode(searchObject.search)
    pass
if "artist" in form:
    searchObject.artist = form["artist"].value
    searchObject.artist = requestHandler.encode(searchObject.artist)
    pass
if "album" in form:
    searchObject.album = form["album"].value
    searchObject.album = requestHandler.encode(searchObject.album)
    pass    
if "song" in form:
    searchObject.song = form["song"].value
    searchObject.song = requestHandler.encode(searchObject.song)
    pass
if "albumsByArtist" in form:
    searchObject.artist = form["albumsByArtist"].value
    searchObject.artist = requestHandler.encode(searchObject.artist)
    pass  

# Use in console
# searchObject.search = requestHandler.encode('Huey Lewis & The News Greatest Hits')
searchObject.artist = requestHandler.encode('Huey Lewis & The News')
searchObject.album = requestHandler.encode('Greatest Hits')

#Global Objects
tracksDict = []

# Last.Fm API
lastFmApi = LastFmApi.Api()
# tracksDict = lastFmApi.getBysearch(searchObject.search)
# tracksDict = lastFmApi.getAlbumsByArtist(searchObject.artist)
tracksDict = lastFmApi.getTracksByArtistAndAlbum(searchObject.artist,searchObject.album)
# tracksDict = lastFmApi.getTracksOfAlbumsbyArtist(searchObject.artist)

#iTunes API
itunesApi = ItunesApi.Api()
# print requestHandler.request(itunesApi.getUrlMedia(searchObject.search))

#SoundCloud API
soundCloudApi = SoundCloudApi.Api()
# print requestHandler.request(soundCloudApi.getUrlTracks(searchObject.search))

if len(tracksDict) > 0:
    print 'Content-Type: application/json'
    print '[' + json.dumps(tracksDict) + ']'
    pass
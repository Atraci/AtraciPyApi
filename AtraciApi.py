#!/usr/bin/python
#!/Applications/MAMP/Library/bin/python2.7
import sys
import cgi
import json
import Request
import LastFmApi
import ItunesApi
import SoundCloudApi
from collections import OrderedDict

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

# Use in console
# form = ''
# searchObject.search = 'metallica'
# searchObject.artist = 'stratovarius'
# searchObject.album = 'destiny'

#Global Objects
tracksDict = []

# Last.Fm API
lastFmApi = LastFmApi.Api()
#Tracks
if searchObject.search != "":
    response = requestHandler.request(lastFmApi.getUrlTracks(searchObject.search))
    jsonObject = requestHandler.encodeJson(response);
    tracks = jsonObject['results']['trackmatches']['track']
    for track in tracks:
    	if 'image' in track:
    		cover_url_medium = ''
    		cover_url_large = ''
    		for image in track['image']:
    			if image['size'] == 'medium' and image['#text'] != '':
    				cover_url_medium = image['#text']
    			elif image['size'] == 'large' and image['#text'] != '':
    				cover_url_large = image['#text']
    				pass
    		pass
    	tracksDict.append(OrderedDict([('title',track['name'].encode('ascii')), ('artist',track['artist'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large)]))
    	pass

#Albums by artist
if searchObject.artist != "" and searchObject.album == "":
    response = requestHandler.request(lastFmApi.getUrlTopAlbumsByArtist(searchObject.artist))
    jsonObject = requestHandler.encodeJson(response);
    albums = jsonObject['topalbums']['album']
    for album in albums:
        if 'image' in album:
            cover_url_medium = ''
            cover_url_large = ''
            for image in album['image']:
                if image['size'] == 'medium' and image['#text'] != '':
                    cover_url_medium = image['#text']
                elif image['size'] == 'large' and image['#text'] != '':
                    cover_url_large = image['#text']
                    pass
            pass
        tracksDict.append(OrderedDict([('artist',album['artist']['name'].encode('ascii')), ('album',album['name'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large)]))
        pass

#Tracks from an albums and artist
if searchObject.artist != "" and searchObject.album != "":
    response = requestHandler.request(lastFmApi.getUrlTracksByArtistAndAlbum(searchObject.artist,searchObject.album))
    jsonObject = requestHandler.encodeJson(response);
    album = jsonObject['album']
    tracks = album['tracks']['track']
    cover_url_medium = ''
    cover_url_large = ''

    if 'image' in album:
        for image in album['image']:
            if image['size'] == 'medium' and image['#text'] != '':
                cover_url_medium = image['#text']
            elif image['size'] == 'large' and image['#text'] != '':
                cover_url_large = image['#text']
                pass
        pass

    for track in tracks:
        tracksDict.append(OrderedDict([('artist',album['artist'].encode('ascii')), ('album',album['name'].encode('ascii')), ('track',track['name'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large)]))
        pass

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
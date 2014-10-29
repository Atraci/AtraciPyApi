#!/usr/bin/python
#!/Applications/MAMP/Library/bin/python2.7
from collections import OrderedDict
import sys
import json
import cgi
form = cgi.FieldStorage()
import urllib
import urllib2
import LastFmApi
import ItunesApi
import SoundCloudApi

# Api Services
class AtraciApi:
    def requestApi(self,url):
    	print url
    	print '\n\n'
    	req = urllib2.Request(url)
    	response = urllib2.urlopen(req)
    	raw = response.readlines()
    	# return response.read()
    	return raw

    def encodeJson(self,json_raw):
    	json_object = json.loads(json_raw[0])
    	# print json_object
    	return json_object

    def encode(self,str):
    	encodedString = urllib.quote(str)
    	return encodedString

#Atraci API
atraciApi = AtraciApi()

# Requested Term from applications
# # print form.keys()
term = form["search"].value
# term = 'metallica'
term = atraciApi.encode(term)


print 'Content-Type: application/json'
#Gloabl Objects
tracksDict = []

# Last.Fm API
lastFmApi = LastFmApi.Api()
# response = atraciApi.requestApi(lastFmApi.getUrlTopAlbumsByArtist(term))
# response = atraciApi.requestApi(lastFmApi.getUrlTracksByArtistAndAlbum(term,atraciApi.encode('Master of Puppets')))
response = atraciApi.requestApi(lastFmApi.getUrlTracks(term))
jsonObject = atraciApi.encodeJson(response);
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
if len(tracksDict) > 0:
	print '[' + json.dumps(tracksDict) + ']'
	pass

#iTunes API
itunesApi = ItunesApi.Api()
# print atraciApi.requestApi(itunesApi.getUrlMedia(term))

#SoundCloud API
soundCloudApi = SoundCloudApi.Api()
# print atraciApi.requestApi(soundCloudApi.getUrlTracks(term))
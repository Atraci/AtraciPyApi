import Request
from collections import OrderedDict

#Last.Fm
Api_Key = 'c513f3a2a2dad1d1a07021e181df1b1f'
ApiUrl = 'http://ws.audioscrobbler.com/2.0/?method={0}&api_key=' + Api_Key + '&format=json'
requestHandler = Request.requestHandler()

class Api:
	Method_Artist_GetTopAlbums = 'artist.getTopAlbums'
	Method_Album_GetInfo = 'album.getInfo'
	Method_Track_Search = 'track.search'

	def getUrlTopAlbumsByArtist(self,artist):
		url = ApiUrl.replace('{0}',self.Method_Artist_GetTopAlbums) + '&artist=' + artist
		return url

	def getUrlTracksByArtistAndAlbum(self,artist,album):
		url = ApiUrl.replace('{0}',self.Method_Album_GetInfo) + '&artist=' + artist + '&album=' + album
		return url

	def getUrlTracks(self,track):
		url = ApiUrl.replace('{0}',self.Method_Track_Search) + '&track=' + track
		return url

	#Tracks
	def getBysearch(self,search):
		tracksDict = []
		if search != "":
		    response = requestHandler.request(self.getUrlTracks(search))
		    jsonObject = requestHandler.encodeJson(response);
		    tracks = jsonObject['results']['trackmatches']['track']
		    for track in tracks:
		    	if 'image' in track:
		    		cover_url_medium = ''
		    		cover_url_large = ''
		    		cover_url_extralarge = ''
		    		for image in track['image']:
		    			if image['size'] == 'medium' and image['#text'] != '':
		    				cover_url_medium = image['#text']
		    				pass
		    			elif image['size'] == 'large' and image['#text'] != '':
		    				cover_url_large = image['#text']
		    				pass
		    			elif image['size'] == 'extralarge' and image['#text'] != '':
		    				cover_url_extralarge = image['#text']
		    				pass
		    		pass
		    	tracksDict.append(OrderedDict([('title',track['name'].encode('ascii')), ('artist',track['artist'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large), ('cover_url_extralarge',cover_url_extralarge)]))
		    	pass
		return tracksDict

	#Albums by artist
	def getAlbumsByArtist(self,artist):
		tracksDict = []
		if artist != "":
		    response = requestHandler.request(self.getUrlTopAlbumsByArtist(artist))
		    jsonObject = requestHandler.encodeJson(response);
		    albums = jsonObject['topalbums']['album']
		    for album in albums:
		        if 'image' in album:
		            cover_url_medium = ''
		            cover_url_large = ''
		            cover_url_extralarge = ''
		            for image in album['image']:
		                if image['size'] == 'medium' and image['#text'] != '':
		                    cover_url_medium = image['#text']
		                    pass
		                elif image['size'] == 'large' and image['#text'] != '':
		                    cover_url_large = image['#text']
		                    pass
		                elif image['size'] == 'extralarge' and image['#text'] != '':
		    				cover_url_extralarge = image['#text']
		    				pass
		            pass
		        tracksDict.append(OrderedDict([('artist',album['artist']['name'].encode('ascii')), ('album',album['name'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large), ('cover_url_extralarge',cover_url_extralarge)]))
		        pass
		return tracksDict

	#Tracks from an album and artist
	def getTracksByArtistAndAlbum(self,artist,album):
		tracksDict = []
		if artist != "" and album != "":
		    response = requestHandler.request(self.getUrlTracksByArtistAndAlbum(artist,album))
		    jsonObject = requestHandler.encodeJson(response);
		    albumObj = jsonObject['album']
		    tracks = albumObj['tracks']['track']
		    cover_url_medium = ''
		    cover_url_large = ''
		    cover_url_extralarge = ''

		    if 'image' in albumObj:
		        for image in albumObj['image']:
		            if image['size'] == 'medium' and image['#text'] != '':
		                cover_url_medium = image['#text']
		                pass
		            elif image['size'] == 'large' and image['#text'] != '':
		                cover_url_large = image['#text']
		                pass
		            elif image['size'] == 'extralarge' and image['#text'] != '':
		    			cover_url_extralarge = image['#text']
		    			pass
		        pass

			if 'name' in tracks:#Single Object
				tracksDict.append(OrderedDict([('artist',albumObj['artist'].encode('ascii')), ('album',albumObj['name'].encode('ascii')), ('track',tracks['name'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large), ('cover_url_extralarge',cover_url_extralarge)])) 
				pass
			else:
			    for track in tracks:
			        tracksDict.append(OrderedDict([('artist',albumObj['artist'].encode('ascii')), ('album',albumObj['name'].encode('ascii')), ('track',track['name'].encode('ascii')), ('cover_url_medium',cover_url_medium), ('cover_url_large',cover_url_large), ('cover_url_extralarge',cover_url_extralarge)]))
			        pass
				pass
		return tracksDict

	#Tracks from albums by artist
	def getTracksOfAlbumsbyArtist(self,artist):
		tracksDict = []
		if artist != "":
		    response = requestHandler.request(self.getUrlTopAlbumsByArtist(artist))
		    jsonObject = requestHandler.encodeJson(response);
		    albums = jsonObject['topalbums']['album']
		    for album in albums:
		    	tracks = self.getTracksByArtistAndAlbum(artist,requestHandler.encode(album['name']))
		        tracksDict.append(tracks)
		        pass
		return tracksDict
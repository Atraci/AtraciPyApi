#Last.Fm
Api_Key = 'c513f3a2a2dad1d1a07021e181df1b1f'
ApiUrl = 'http://ws.audioscrobbler.com/2.0/?method={0}&api_key=' + Api_Key + '&format=json'

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
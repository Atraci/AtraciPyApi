#SoundCloud
Api_Key = 'dead160b6295b98e4078ea51d07d4ed2'
ApiUrl = 'https://api.soundcloud.com/{0}?client_id=' + Api_Key + '&q='

class Api:
	MethodTracks = 'tracks.json'

	def getUrlTracks(self,term):
		url = ApiUrl.replace('{0}',self.MethodTracks) + term
		return url
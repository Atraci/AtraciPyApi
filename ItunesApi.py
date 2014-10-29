#iTunes
ApiUrl = 'http://itunes.apple.com/search?media=music&entity={0}&limit=100&term='

class Api:
	Entity = 'song'

	def getUrlMedia(self,term):
		url = ApiUrl.replace('{0}',self.Entity) + term
		return url
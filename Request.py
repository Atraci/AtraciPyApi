import urllib
import urllib2
import json

# Request Class
class requestHandler:
    def request(self,url):
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
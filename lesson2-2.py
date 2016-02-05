import json
import requests
import pprint

if __name__=='__main__':
    url='http://ws.audioscrobbler.com/2.0/?method=geo.getTopArtists&api_key=4beab33cc6d65b05800d51f5e83bde1b&country=Spain&format=json'
    data = requests.get(url).text
    data = json.loads(data)
    data = data['topartists']
    data = data['artist']
    topArtist = data[0]
    artist=topArtist['name']
    print(artist)
    #for x,y in topArtist.iteritems():
    #    print("{0},{1}".format(x,y))
import urllib,json
data = json.loads(urllib.urlopen("http://api.giphy.com/v1/gifs/search?q=ryan+gosling&api_key=dc6zaTOxFJmzC&limit=5").read())
print data['data'][0]['images']['downsized_medium']['url']
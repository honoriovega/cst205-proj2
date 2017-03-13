import requests
from random import randint
def getImages(search_term):
   # fiels=detail_set
   url = "https://api.gettyimages.com/v3/search/images?fields=detail_set&sort_order=best&phrase=" \
         + search_term + "&page_size=100"

   my_headers = { "Api-Key" : 'qwj5pp6xrv4td7djmab3jeec' }
   response = requests.get(url, headers = my_headers)
   json_body = response.json()
 
   length = len(json_body['images']) 
 
         
   return json_body['images'][randint(0,length - 1)]['display_sizes'][0]['uri']

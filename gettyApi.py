import requests
from random import randint,choice
import random

def getImages(search_term):
   # fiels=detail_set
   url = "https://api.gettyimages.com/v3/search/images?fields=detail_set&sort_order=best&phrase=" \
         + search_term + "&page_size=100"

   my_headers = { "Api-Key" : 'qwj5pp6xrv4td7djmab3jeec' }
   response = requests.get(url, headers = my_headers)
   json_body = response.json()
 
   length = len(json_body['images']) 
   return json_body['images'][randint(0,length - 1)]['display_sizes'][0]['uri']

   
"""
def initBackground(search_term):
   url = "https://api.gettyimages.com/v3/search/images?fields=detail_set&sort_order=best&phrase=" \
         + search_term + "&page_size=100"

   my_headers = { "Api-Key" : 'qwj5pp6xrv4td7djmab3jeec' }
   response = requests.get(url, headers = my_headers)
   json_body = response.json()
 
   idHolder = [] # holds ids asociated with the images 
   for photoID in json_body['images']: #Pulling image ids associated with the query
        jsonID = photoID['id']
        idHolder.append(jsonID)
        random.shuffle(idHolder) #suffling the list to ensure unique images on each load
   
   getty_images_id  = random.choice(idHolder) #setting the randomly selected images id to a variable
   getty_image_source = "http://media.gettyimages.com/photos/-id" + getty_images_id #appending the variable to the HQ link to get images
   return getty_image_source
"""
def initBackground(search_term):
   url = "https://api.gettyimages.com/v3/search/images?fields=detail_set&sort_order=best&phrase=" \
         + search_term + "&page_size=100"

   my_headers = { "Api-Key" : 'qwj5pp6xrv4td7djmab3jeec' }
   response = requests.get(url, headers = my_headers)
   json_body = response.json()

				 # holds ids asociated with the images using list comprehension
   idHolder  = [ photoID['id'] for photoID in json_body['images'] ]
   
   #setting the randomly selected images id to a variable
   getty_images_id  = choice(idHolder) 
   
   #appending the variable to the HQ link to get images
   getty_image_source = "http://media.gettyimages.com/photos/-id" + getty_images_id 
   return getty_image_source
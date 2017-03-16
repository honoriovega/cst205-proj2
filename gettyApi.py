"""
 Course : CST205
 Title : botcommands.py
 Authors: Javar Alexander, Honorio Vega
 Abstract : This file contains the commands for the getty api.
			It contains two functions. One to fetch the background for
			the chat app and the other to retrieve images based on a users
			request. For example if a user types "!! getty dogs" the
			the getImages command will take that string and parse it
			It will extract the search term and make an api call to 
			Getty. It will response a result and pick a random image
			and return it.  
 Date : 03/15/2017
 Who worked on what: Honorio generated the API keys and wrote the
					 getImages function. Javar wrote the initbackground
					 function

GITHUB LINK : https://github.com/honoriovega/cst205-proj2
"""


import requests
from random import randint,choice

def getImages(search_term):
   # fiels=detail_set
   url = "https://api.gettyimages.com/v3/search/images?fields=detail_set&sort_order=best&phrase=" \
         + search_term + "&page_size=100"

   my_headers = { "Api-Key" : 'qwj5pp6xrv4td7djmab3jeec' }
   response = requests.get(url, headers = my_headers)
   json_body = response.json()
 
   length = len(json_body['images']) 
   return json_body['images'][randint(0,length - 1)]['display_sizes'][0]['uri']

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
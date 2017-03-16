"""
 Course : CST205
 Title : app.py
 Authors: Javar Alexander, Honorio Vega, Antonio Villagomez
 Abstract : This program is the driver of the program. It sets up
             the server. It also broadcasts and sends new messages.
			   aswell as saving the messages to a database. It pulls
			   pictures from Getty and Giphy API's and sends them to
			   the users
 Date : 03/15/2017
 Who worked on what: Javar and Honorio worked on this file. Javar
					   wrote the spotify feature. Honorio worked on the
					   database and received and sending images. All other
				        feautures in this file were a combination of 
				        work from Javar and Honorio. For example, Javar
				        worked on parts of the BOT and Honorio worked
				        on it also

GITHUB LINK : https://github.com/honoriovega/cst205-proj2

"""



import random, os, flask, flask_socketio, flask_sqlalchemy,requests, time
from random import randint, choice
from flask_socketio import send
import gettyApi
import botcommands

import urlparse
import json

app = flask.Flask(__name__)

#app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql://potato:potatosareawesome@localhost/postgres'
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = flask_sqlalchemy.SQLAlchemy(app)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.String(300))
	picture = db.Column(db.String(200))
	name = db.Column(db.String(100))
	apiLink = db.Column(db.String(500))

	def __init__(self, p,n,t,al=''):
		self.text = t
		self.picture = p
		self.name = n
		self.apiLink = al

	def __repr__(self):
		return '<%s %s: %s>' % (self.picture, self.name, self.text)

socketio = flask_socketio.SocketIO(app)

all_messages = []
all_connected_users = { };
all_numbers = []

# fetch all message from database and store them in dictionary 
# and append to a list
def fetchAllMessages():
	messages = Message.query.all()
	temp = []

	for message in messages:
		temp.append({
		'name': message.name,
		'picture': message.picture,
		'msg': message.text,
		'link' : message.apiLink
		})

	return temp

# broadcasst the messages
def fetchAndEmit():
	all_messages[:] = fetchAllMessages()

	socketio.emit('all messages', {
	'messages': all_messages
	})

# add message to our database
def addMessage(userPicture, name, msg):
	message = Message(userPicture,name, msg)
	db.session.add(message)
	db.session.commit()

# add message to our database
def addBotMessage(msg):
	BOT_PICTURE = '/static/bot.jpg'
	BOT_NAME = 'Bender_from_futurama'
	addMessage(BOT_PICTURE,BOT_NAME,msg)

# add message to our database
def addBotMessageAPI(link):
	BOT_PICTURE = '/static/bot.jpg'
	BOT_NAME = 'Bender_from_futurama'
	addPictureMessage(BOT_PICTURE,BOT_NAME,link)

# add message to our database
def addPictureMessage(userPicture, name, apiLink):
	message = Message(userPicture,name, '', apiLink)
	db.session.add(message)
	db.session.commit()

# this is where the app starts
@app.route('/')
def hello():
	keywords = ['technology','forest','background']
	a = gettyApi.initBackground(choice(keywords))

	return flask.render_template('index.html',back=a)

# When the user conencts call the fetchAndEmit command
# which pulls the messages from the database and broadcasts them
@socketio.on('connect')
def on_connect():
	fetchAndEmit()

# this function was used for testing purposes
@socketio.on('new number')
def on_new_number(data):
	all_numbers.append(100)
	socketio.emit('all numbers', {
			'numbers' : all_numbers
	})


# Function that Javar wrote. Fetches data from the Spotify API and display it
@socketio.on('Spotify')
def spotify(data):
	tracks =[]
	searchType = data['searchType']
	searchQuery =  data['searchQuery']
	searchQuery1 = searchQuery.replace("+", "%20")
	response = requests.get("https://api.spotify.com/v1/search?q="+searchQuery1+"&type="+searchType)
	json = response.json()
	if 'tracks' in json and 'items' in json['tracks']:
		for item in json['tracks']['items']:
			print item['uri']
    		tracks.append(item['uri'])

	my_headers = {"Accept" : "application/json", "Authorization" : "Bearer BQCm9bzjiDxNb9FurI8AWVgraOhvdZyzpBBNq753DwEXocrLa8kyPNOalfXuevtiZ10Kt8FIuvM1RMnv6mWiVsz9bXU8VQzEv3xdHAE5Qs4-eFI4dh3spBArHnzQLl6gGqvddte-H7JZQVzJEsxobx1TSStfVqonFzxWdH418b5RtzgZMHFgnKtV-6qW9g_axQ1bKwQ4Fm8e1NI"}
	url = "https://api.spotify.com/v1/tracks/1zHlj4dQ8ZAtrayhuDDmkY"
	track_response = requests.get(url, headers= my_headers)
	spotify_links = track_response.json()
	random_track = random.choice(tracks)

	random_track_link = "https://embed.spotify.com/?uri="+random_track
	socketio.emit('fromSpotify', random_track_link)


# this function was ment as featuer to greet the user on log in
# the feature was not implemented as their was issue. We didn't
# want to remove it beacause it might break our code. For now it is just here
@socketio.on('greet user')
def greet_user(data):
	picture = ''
	USERNAME = ''
	greet = ''

	if(data['google_user_token'] == '' and data['facebook_user_token'] == ''):
		send('greeting user')

	else:

		if(data['google_user_token'] == ''):
			response = requests.get('https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token=' + data['facebook_user_token'])
			json = response.json()
			USERNAME =  json['name']
			picture =  json['picture']['data']['url']
			greet = 'Hello ' + USERNAME + ' logged in from Facebook'

		else:
			response = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
			json = response.json()
			picture = json['picture']
			USERNAME = json['name']
			greet = 'Hello ' + USERNAME + ' logged in from Google'

		addBotMessage(greet)

		fetchAndEmit()

# When a new message is received this function
# stores it in the database, checks to see if it a bot command
# or a link. 
@socketio.on('new msg')
def on_new_msg(data):
	facebookAPI = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token='
	googleAPI = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='

	msg = data['msg']
	USERNAME =  ''
	picture =  ''
	msg = msg.strip()
	if(data['google_user_token'] == '' and data['facebook_user_token'] == '' ):
		send('received message')

	else:
		if(data['google_user_token'] == ''):
			response = requests.get( facebookAPI + data['facebook_user_token'])
			json = response.json()
			USERNAME =  json['name']
			picture = json['picture']['data']['url']

		else:
			response = requests.get(googleAPI + data['google_user_token'])
			json = response.json()
			picture = json['picture']
			USERNAME = json['name']

	url = msg
	parts = urlparse.urlsplit(url)

	# it is not a url so add it and emit
	if not parts.scheme or not parts.netloc:

		if('!! say' in msg):
			x = 10
		else:
			addMessage(picture,USERNAME, msg)

	else:
		print "yes an url"
		addPictureMessage(picture,USERNAME,url)
	#fetchAndEmit()
	# handle bot command
	if(msg[:2] == '!!'):
		response = botcommands.processBotCommand(msg)
		if(len(response) > 4):
			if(response[:4] == 'http'):
				addBotMessageAPI( response )
			else:
				addBotMessage(response)
		else:
			addBotMessage(response)

	fetchAndEmit()

# this gets the server up an running
if __name__ == '__main__':
	socketio.run(
		app,
		host=os.getenv('IP', '0.0.0.0'),
		port=int(os.getenv('PORT', 8080)),
		debug=True
	)


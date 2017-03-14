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

def fetchAndEmit():
	all_messages[:] = fetchAllMessages()

	socketio.emit('all messages', {
	'messages': all_messages
	})

def addMessage(userPicture, name, msg):
	message = Message(userPicture,name, msg)
	db.session.add(message)
	db.session.commit()


def addBotMessage(msg):
	BOT_PICTURE = '/static/bot.jpg'
	BOT_NAME = 'Bender_from_futurama'
	addMessage(BOT_PICTURE,BOT_NAME,msg)
	
def addBotMessageAPI(link):
	BOT_PICTURE = '/static/bot.jpg'
	BOT_NAME = 'Bender_from_futurama'
	addPictureMessage(BOT_PICTURE,BOT_NAME,link)


def addPictureMessage(userPicture, name, apiLink):
	message = Message(userPicture,name, '', apiLink)
	db.session.add(message)
	db.session.commit()
	
@app.route('/')
def hello():
	keywords = ['technology','beach','forest','background']
	a = gettyApi.initBackground(choice(keywords))

	return flask.render_template('index.html',back=a)
"""
@socketio.on('connect')
def on_connect():
	name = random.randrange(1000, 9999)

	flask_socketio.emit(
		'server generated a new name',
		{
			'name': name
		}
	)

	all_connected_users[flask.request.sid] = name

	socketio.emit(
		'list of all users',
		{
			'users': all_connected_users.values()
		}
	)
	
	

	
	greet = "Welcome to the chatroom new user. Type !! help to view list of commands"
	addBotMessage(greet)

	fetchAndEmit()
"""

@socketio.on('new number')
def on_new_number(data):
	"""
	response = requests.get('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=' + data['google_user_token'])
	json = response.json()

	all_numbers.append({
	'name': json['name'],
	'picture': json['picture'],
	'number': data['number']
	})

	socketio.emit('all numbers', {
		'numbers': all_numbers
	})
	"""
	all_numbers.append(100)
	socketio.emit('all numbers', {
			'numbers' : all_numbers
	})
	
	
	
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
	print spotify_links
	random_track = random.choice(spotify_links)
	socketio.emit('fromSpotify', random_track)
	
	
	
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

@socketio.on('new msg')
def on_new_msg(data):
	facebookAPI = 'https://graph.facebook.com/v2.8/me?fields=id%2Cname%2Cpicture&access_token='
	googleAPI = 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='

	msg = data['msg']
	USERNAME =  ''
	picture =  ''
	
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
		
		if(len(msg) > 4):
			if(msg[len(msg) - 3:] in ['edu','com','net','gov','org']):
				addPictureMessage(picture,USERNAME,'http://' +msg)
			else:
				addMessage(picture,USERNAME,  msg)
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

if __name__ == '__main__':
	socketio.run(
		app,
		host=os.getenv('IP', '0.0.0.0'),
		port=int(os.getenv('PORT', 8080)),
		debug=True
	)


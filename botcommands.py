"""
 Course : CST205
 Title : botcommands.py
 Authors: Javar Alexander, Honorio Vega
 Abstract : This contains the possible commands that the bot can do.
		    It can be made to repeat what a user said. It can also be
		    made to fetch pictures and gif's from Getty and Giffy
		    respectively. 
 Date : 03/15/2017
 Who worked on what: Honorio worked on parsing and processing the text.
				     Javar wrote on the functions called that called
				     external API's

GITHUB LINK : https://github.com/honoriovega/cst205-proj2

"""

from random import randint,choice
import gettyApi
import json
import urllib
def processBotCommand(userSubmitted):

    recognizedCommands = ['say','about','help','backwards','doMath','getty','giffy']

    if('!! about' in userSubmitted):

        msg = 'website created by Honorio Vega, Javar Alexander, Antonio Villagomez'
        return msg

    elif('!! say' in userSubmitted):
        msg = userSubmitted.split('!! say')[1]
        return msg.strip()

    elif('!! backwards' in userSubmitted):
        msg = userSubmitted.split('!! backwards')[1]
        backwards = "".join(list(reversed(msg)))
        return backwards.strip()

    elif('!! doMath' in userSubmitted):
        a = randint(1,100)
        b = randint(1,100)
        currentTime = "%d + %d = %d" % (a,b,a+b)

        messagesend =   str(currentTime)
        return messagesend.strip()

    elif('!! help' in userSubmitted):
        msg =  'I recognize these commands: ' + ", ".join(recognizedCommands)
        return msg

    elif('!! getty' in userSubmitted):

        searchTerm = userSubmitted.split('!! getty')[1]
        img = gettyApi.getImages(searchTerm)
        return img
    
    elif('!! giffy' in userSubmitted):
        searchTerm = userSubmitted.split('!! giffy')[1]
        query = searchTerm.replace(' ','+')
        
        link = "http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=dc6zaTOxFJmzC&limit=5"
        
        data = json.loads(urllib.urlopen(link).read())
        
        # no results :-*(
        if(len(data['data']) == 0 ):
            return "Sorry I didn't find any gif's with that search term"
        
        else:
        
            apilink = data['data'][randint(0,len(data['data']) -1)]['images']['downsized_medium']['url']
            return apilink
    


    else:
        msg =  'command not recognized'
        return msg

def sayBye(name):
	randomPhrases  = ["Leave and don't come back ", "Get out of here ", "Good ridance ",
					 "Be gone "]
	
	return choice(randomPhrases) + name

def greetNewUser(name):
	phrases = ['Wassup, ', 'YO ', 
	                     "How's it going ", "Hey there ", "Howdy "]
	return choice(phrases) + name

def randomPhrase():
    phrases = ['there you happy ? ',
                    'i am at your command for now ...', 
                    'computers will take over',
                    'i will be issuing commands to you soon...']
    return choice(phrases)
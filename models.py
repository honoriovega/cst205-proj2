"""
 Course : CST205
 Title : models.py
 Author: Honorio Vega
 Abstract : This file is our database model. It defines our fields and
			table. This file will be used to create the database
			in postgresql. 
 Date : 03/15/2017
 Who worked on what: Honorio wrote this file. Consulted with Antonio
					  and Javar for their input on what fields should
					   be included

GITHUB LINK : https://github.com/honoriovega/cst205-proj2
"""

from app import *
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql://potato:potatosareawesome@localhost/postgres'
#app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
db = flask_sqlalchemy.SQLAlchemy(app)


class Message(db.Model):
    
    # The structure of our database
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

from app import *
app.config[ 'SQLALCHEMY_DATABASE_URI' ] = 'postgresql://potato:potatosareawesome@localhost/postgres'
#app.app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
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

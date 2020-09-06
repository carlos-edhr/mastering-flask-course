from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import DevConfig
from db import URI

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

print(URI)

# MODELS 

#User Model
class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    
    def __init__(self, username):
        self.username = username
    
    
    def __repr__(self):
        return "<User '{}'>".format(self.username)



from mongoengine import *

class User(Document):
    username = StringField()
    password = StringField()
    fullname = StringField()
    yob = IntField()
    email = StringField()
    gender = IntField()
    

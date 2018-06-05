from mongoengine import *

class Coin(Document):
    coinname = StringField()
    

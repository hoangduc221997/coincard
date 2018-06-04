import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds147440.mlab.com:47440/coincard

host = "ds147440.mlab.com"
port = 47440
db_name = "coincard"
user_name = "admin1"
password = "admin1"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())

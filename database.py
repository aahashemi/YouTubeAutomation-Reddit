from tinydb import TinyDB
db = TinyDB('./database.json')

def load_databse():
    db = TinyDB('./database.json')
    return db


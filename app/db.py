from tinydb import TinyDB, Query

db = None


def get_db():
    global db
    if db is None:
        db = TinyDB('db.json')
    return db


def close_db():
    global db
    if db is not None:
        db.close()
        db = None

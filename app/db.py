from tinydb import TinyDB

# Глобальная переменная для хранения объекта базы данных
db = None


def get_db():
    """
        Возвращает объект базы данных TinyDB.
        Если база данных еще не инициализирована, создает новый объект.
    """
    global db
    if db is None:
        db = TinyDB('db.json')
    return db


def close_db():
    """
        Закрывает соединение с базой данных TinyDB.
    """
    global db
    if db is not None:
        db.close()
        db = None

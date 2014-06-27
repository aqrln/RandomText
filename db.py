import sqlite3
import os.path

connection = None
cursor = None


def connect(name='words.db'):
    global connection, cursor
    if os.path.isfile(name):
        new_db = False
    else:
        new_db = True
    connection = sqlite3.connect(name)
    cursor = connection.cursor()
    if new_db:
        cursor.execute('CREATE TABLE words (left varchar(1000), right varchar(100))')
        cursor.execute('CREATE INDEX leftindex ON words (left)')


def close():
    connection.commit()
    connection.close()


# TODO: escape possible SQL injections
def escape(string):
    return string.replace("'", "''")


def put(left, right):
    left = escape(" ".join(left))
    right = escape(right)
    cursor.execute("INSERT INTO words VALUES ('%s', '%s')" % (left, right))


def get(left):
    left = escape(" ".join(left))
    data = cursor.execute("SELECT right FROM words WHERE left = '%s'" % left)
    for row in data:
        yield row[0]
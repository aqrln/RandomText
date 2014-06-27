import db

try:
    db.connect()
    while True:
        print('Enter some sequences of words.\n')
        print('>', end=' ')
        words = input().split()
        for word in db.get(words):
            print('  -', word)
        print()
except (EOFError, KeyboardInterrupt):
    pass
finally:
    db.close()
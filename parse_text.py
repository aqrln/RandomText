import sys
import db


def main(filename, depth=5):
    print('Reading file...')

    with open(filename, 'r') as file:
        words = file.read().split()
    if len(words) < depth + 1:
        depth = len(words) - 1

    print('Establishing a connection with the database...')
    db.connect()

    for curr_depth in range(1, depth + 1):
        print('Processing depth %d...' % curr_depth)
        left = words[:curr_depth]
        for right in words[curr_depth:]:
            db.put(left, right)
            left = left[1:] + [right]

    print('Finalizing...')
    db.close()


if __name__ == '__main__':
    main(*sys.argv[1:])
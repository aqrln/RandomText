import random
import db


def generate(left, chain_length, max_length):
    text_length = len(left)
    print(' '.join(left), end=' ')
    db.connect()
    while text_length < max_length:
        found = False
        for j in range(chain_length):
            right_variants = list(db.get(left[j:]))
            if len(right_variants) > 0:
                found = True
                right = random.choice(right_variants)
                print(right, end=' ')
                left = left[1:] + [right]
                text_length += 1
                break
            else:
                continue
        if not found:
            break
    db.close()
    print()


def main():
    print('Initial phrase: ', end='')
    left = input().split()

    print('Chain length [%d]: ' % len(left), end='')
    try:
        chain_length = int(input())
    except ValueError:
        chain_length = len(left)

    print('Maximal text length (in words) [250]: ', end='')
    try:
        max_length = int(input())
        if max_length < chain_length:
            raise ValueError
    except ValueError:
        max_length = 250

    generate(left, chain_length, max_length)


if __name__ == '__main__':
    main()
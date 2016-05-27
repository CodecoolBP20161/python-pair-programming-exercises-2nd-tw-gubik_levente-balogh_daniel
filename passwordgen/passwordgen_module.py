import string
import random


def passwordgen():
    password = ""
    LOWER = string.ascii_lowercase
    UPPER = string.ascii_uppercase
    DIGITS = string.digits
    PUNCT = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?']
    # first we used string.punctuation, but that contains more characters, then the test.py
    n = 0
    chars = [1, 1, 1, 1]
    while n < 8 or (chars[0] or chars[1] or chars[2] or chars[3]):
        rnd = random.randrange(0, 4)
        if rnd == 0:
            indx = random.randrange(0, len(LOWER))
            password += LOWER[indx]
            chars[rnd] = 0
        elif rnd == 1:
            indx = random.randrange(0, len(UPPER))
            password += UPPER[indx]
            chars[rnd] = 0
        elif rnd == 2:
            indx = random.randrange(0, len(DIGITS))
            password += DIGITS[indx]
            chars[rnd] = 0
        elif rnd == 3:
            indx = random.randrange(0, len(PUNCT))
            password += PUNCT[indx]
            chars[rnd] = 0
        n += 1
    return password


def main():
    print (passwordgen())

main()

'''
if __name__ == '__main__':
    main()
'''

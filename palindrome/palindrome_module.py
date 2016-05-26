def palindrome(strng):
    strng = "".join(strng.split())
    return strng.lower() == strng[::-1].lower()


def main():
    is_palindrome = str(input("Give me a word please: "))
    if palindrome(is_palindrome):
        print("Yes, this is a beautiful palindrome according to the unittest You wrote :)")
    else:
        print("No, of course this is not a palindrome, according to the unittest You wrote :)")
    return


if __name__ == '__main__':
    main()

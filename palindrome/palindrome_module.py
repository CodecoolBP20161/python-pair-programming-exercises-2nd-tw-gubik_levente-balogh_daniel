def palindrome(str1):

    str_list = list(str1)
    for char in str_list :
        if char == " " :
            str_list.remove(char)
    str2 = "".join(str_list)
    print (str2)
    if str2.lower() == (str(str2[::-1])).lower() :
        statement = True
    else :
        statement = False

    return statement


def main():
    is_palindrome = str(input("Give me a word please: "))
    if palindrome(is_palindrome) == True :
        print("No, of course this is not a palindrome, according to the unittest You wrote :)")
    else :
        print("Yes, this is a beautiful palindrome according to the unittest You wrote :)")
    return


if __name__ == '__main__':
    main()

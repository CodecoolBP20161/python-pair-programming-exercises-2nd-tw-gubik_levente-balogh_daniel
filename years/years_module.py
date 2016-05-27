from datetime import date


def years(age):
    return (date.today().year+100-age)


def main():
    name = input("What is your name?: ")
    age = int(input("How old are you?: "))
    print (name + ", you will be 100 years old this year: " + str(years(age)))
    return


if __name__ == '__main__':
    main()

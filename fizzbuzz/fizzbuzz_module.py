def fizzbuzz(number):
    if (float(number) / 15) == round(number / 15) :
        sign = "FizzBuzz"
    elif (float(number) / 3) == round(number / 3) :
        sign = "Fizz"
    elif (float(number) / 5) == round(number / 5) :
        sign = "Buzz"
    else :
        sign = number
    print(sign)
    return sign



def main():
    for x in range(1, 101):
        fizzbuzz(x)
    return



if __name__ == '__main__':
    main()

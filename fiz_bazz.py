for number in range(1, 101):
    #create range between 1-101
    
    if number %3 == 0 and number %5 == 0:
        print("FizzBuzz")
        #divisible by both 3 and 5
    elif number %5 == 0:
        print("Fizz")
        #divisible by 5

    elif number %3 == 0:
        print("Bazz")
        #divisible by 3

    else:
        print(number)
    #print the number between fizz and buzz
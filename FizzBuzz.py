for number in range(1, 101):
    currentString = str(number)
    if (number % 5 == 0) & (number % 3 == 0):
        currentString = "FizzBuzz"
    elif number % 5 == 0:
        currentString = "Buzz"
    elif number % 3 == 0:
        currentString = "Fizz"
    if number % 7 == 0:
        if str(number) == currentString:
            currentString = "Bang"
        else:
            currentString = currentString + "Bang"
    print(currentString)

maxValue = int(input("Enter maximum value:"))
for number in range(1, maxValue + 1):
    specialList = []
    if (number % 5 == 0) & (number % 3 == 0):
        specialList.append("Fizz")
        specialList.append("Buzz")
    elif number % 5 == 0:
        specialList.append("Buzz")
    elif number % 3 == 0:
        specialList.append("Fizz")
    if number % 7 == 0:
        if specialList == "":
            specialList = ["Bang"]
        else:
            specialList.append("Bang")
    if number % 11 == 0:
        currentString = "Bong"
    if number % 13 == 0:
        specialList.insert(0, "Fezz")
    if (number % 17 == 0) & (specialList != ""):
        specialList.reverse()
    if specialList == "":
        print(number)
    else:
        print(specialList)

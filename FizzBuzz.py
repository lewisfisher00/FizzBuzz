maxValue = int(input("Enter maximum value:"))
for number in range(195, maxValue + 1):
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
        counter = int(0)
        while counter < len(specialList):
            if specialList[counter][0] == "B":
                indexB = int(counter)
            counter = counter + 1
        if counter == len(specialList) + 1:
            indexB = 0
        specialList.insert(indexB, "Fezz")
    if (number % 17 == 0) & (specialList != ""):
        specialList.reverse()
    if specialList == "":
        print(number)
    else:
        print(specialList)

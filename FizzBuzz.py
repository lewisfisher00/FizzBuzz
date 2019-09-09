valid = bool(False)
maxValue = 0
while not valid:
    userInput = input("Enter maximum positive integer:")
    try:
        maxValue = int(userInput)
        valid = True
    except:
        print("Not a valid input")
FB = input("Use FizzBuzz? (y/n)")
Fzz = input("Use Fizz? (y/n)")
Bzz = input("Use Buzz? (y/n)")
Bag = input("Use Bang? (y/n)")
Bon = input("Use Bong? (y/n)")
Fez = input("Use Fezz? (y/n)")
Rev = input("Use Reverse? (y/n)")


for number in range(1, maxValue + 1):
    specialList = []
    #fizzbuzz
    if (number % 5 == 0) & (number % 3 == 0) & (FB == "y"):
        specialList.append("Fizz")
        specialList.append("Buzz")
    #buzz
    elif number % 5 == 0 & (Bzz == "y"):
        specialList.append("Buzz")
    #fizz
    elif number % 3 == 0 & (Fzz == "y"):
        specialList.append("Fizz")
    #bang - 7
    if number % 7 == 0 & (Bag == "y"):
        if len(specialList) == 0:
            specialList = ["Bang"]
        else:
            specialList.append("Bang")
    #bong - 11
    if number % 11 == 0 & (Bon == "y"):
        currentString = "Bong"
    #fezz - 13 - before first B***
    if number % 13 == 0 & (Fez == "y"):
        counter = int(0)
        indexB = 0
        while counter < len(specialList):
            if specialList[counter][0] == "B":
                indexB = int(counter)
            counter = counter + 1
        if counter == len(specialList) + 1:
            indexB = 0
        specialList.insert(indexB, "Fezz")
    #reverse - 17
    if (number % 17 == 0) & (specialList != "") & (Rev == "y"):
        specialList.reverse()
    #print
    if len(specialList) == 0:
        print(number)
    else:
        print("".join(specialList))

import random

target = random.randint(1,100)
print(target)

while True:
    userChoice = input("Guess the target or Quit(q): ")
    if(userChoice == "q"):
        break

    userChoice = int(userChoice)
    if(userChoice == target):
        print("Success !")
        break
    elif(userChoice < target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number was too big. Take a smaller guess..")

print("____Game Over____")
import random

print("Hello world!")

print("I'd like to guess your age")

userNumber = int(input('How old are you?: '))

myGuess = random.randint(1, 120)

print("My guess is " + str(myGuess) + " Is this your age?")
print("Type yes or no if this is your age")

userCon = str(input())

while userCon == "no" or userCon == "nah" or userCon == "nope":
    print("Fuck, let me guess again")
    myGuess = random.randint(1, 120)
    print("Is this your age?: " + str(myGuess))
    userCon = input()

if userCon == "yes":
    print("Holy shit I actually got it lmao")
else:
    print("You didn't fucking enter yes or no bitch. I'm done with you.")
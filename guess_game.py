from random import randint

number = randint(1, 10)
trial = 0
while trial < 3:
    guess = int(input("Guess a number between 1 and 10: "))
    if number == guess:
        print("You guessed correctly.")
        break
    else:
        print("Wrong number, Try again!!!")
        trial += 1

print("Number is {}".format(number))

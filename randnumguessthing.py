import random

result = ["less than", "equal to", "more than", ]


def guess():
    somenumber = random.randint(1, 10)
    userval = -1
    while int(userval) != somenumber:
        userval = input("Guess a number between one and ten!  ")
        diff = int(userval) - somenumber
        resultindex = 1 if diff == 0 else (diff // abs(diff) + 1)
        print("The value you guessed is " + result[resultindex] + " the random number!")
    print("Congratulations! You win!")


guess()

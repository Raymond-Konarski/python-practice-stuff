import enum
import random


class RPStoEnum(enum.Enum):
    rock = 0
    paper = 1
    scissors = 2


result = ["You Tied!", "You Win!", "You Lose!"]


def user_input():
    return RPStoEnum[input("Rock, Paper, or Scissors? ").lower()].value


def cpu_input():
    return random.randint(0, 2)


def who_wins(user, cpu):
    return abs((user - cpu) % 3)


play = "yes"
while play == "yes":
    print("Welcome to the Rock, Paper, Scissors Machine!")
    player = user_input()
    computer = cpu_input()
    print("You played: " + RPStoEnum(player).name)
    print("But the computer played: " + RPStoEnum(computer).name)
    print(result[who_wins(player, computer)])
    play = input("Play again? ").lower()
    print("Bye!")

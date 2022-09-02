import random

TITLE = "Raymond's Text Adventure Game"
MENU_OPTIONS = ("     [Start]\n"
                "     [Settings]\n"
                "     [Quit]\n"
                "      ")


def menu_options(option):
    print()
    match option.upper():
        case 'START':
            start_game()
        case 'SETTINGS':
            settings()
        case 'QUIT':
            in_game_quit()
        case _:
            print("Please enter one of the three options.")
            menu_options(input(MENU_OPTIONS))


def start_game():
    print("--Game--")
    user = Player
    choose_encounter(user)


def settings():
    print("--Settings--")
    print("This game has literally no settings.")
    input("Press enter to return to the Main Menu.")
    main_menu()
    pass


def in_game_quit():
    print("--Quitting--")
    print("Bye!")
    exit(0)


def main_menu():
    print("------------------------------------------------------")
    print("Welcome to " + TITLE)
    menu_options(input(MENU_OPTIONS))


def generate_enemy():
    enemy = Enemy()
    return enemy


class Player:
    health = 100
    damage = 10
    points = 0

    # TODO add some randomness
    def __init__(self):
        pass


class Enemy:
    difficulty = 1
    health = 1
    damage = 1

    def __init__(self):
        self.difficulty = random.randint(1, 10)
        self.health = max((random.randint(0, 20)) + (5 * self.difficulty), 1)
        self.damage = max(random.randint(0, 5) - 2 + self.difficulty, 1)


def combat_menu(player, enemy):
    print("Enemy Level: " + str(enemy.difficulty))
    print("Enemy Health: " + str(enemy.health))
    print("")
    print("Player Health: " + str(player.health))
    print("     [Attack]\n"
          "     [Defend]\n"
          "     [Flee]\n")
    choice = input()
    match choice.upper():
        case 'ATTACK':
            enemy.health -= player.damage
            print("You dealt " + str(player.damage) + " damage!")
        case 'DEFEND':
            print("You don't have a shield!")
            print("Instead, you close your eyes and brace yourself... to no effect!")
        case 'FLEE':
            print("You ran away, coward!")
            choose_encounter(player)
        case _:
            print("You got confused and did... nothing!")
    if enemy.health < 1:
        print("You have slain your adversary!")
        generate_rewards(player, enemy)
    enemy_turn(player, enemy)
    if player.health < 1:
        print("You Died!")
        print("You finished with " + str(player.points) + " points!")
        main_menu()
    combat_menu(player, enemy)


def enemy_turn(player, enemy):
    print("The enemy attacks!")
    print("You take " + str(enemy.damage) + " damage!")
    player.health -= enemy.damage


def generate_rewards(player, enemy):
    print("You gained " + str(enemy.difficulty) + " points!")
    player.points += enemy.difficulty
    print("You now have " + str(player.points) + " points.")
    choose_encounter(player)


def choose_encounter(player):
    print("------------------------------------------------")
    input("Press enter to proceed to the next encounter.")
    print("You've encountered an enemy!")
    combat_menu(player, generate_enemy())


if __name__ == '__main__':
    main_menu()

import random
from random import Random


#Var
game_run = True
players = False
two_players = False
next_player = False
alone = ""

game = "|1|2|3|\n|4|5|6|\n|7|8|9|\n"
user = ""
user_2 = ""
cpu = ""
user_symbol = ""
cpu_symbol = ""
cpu_options = ["1","2","3","4","5","6","7","8","9"]
numbers_played = ""

current_game = ""
winner_symbol = "None"
yes_or_not = ""

#make a copy of the table game for a future reset
def show_the_game():
    global current_game
    for x in range(0, 24):
        for y in game[x]:
            current_game += y
    return current_game

#take the user input and the user_symbol to write in the game table
def user_choice(user, user_symbol):
    global current_game,numbers_played
    numbers_played += user
    cpu_options.remove(user)
    for x in range(0, len(game)):
             if user in game[x]:
                 current_game = current_game.replace(user, user_symbol, 1)
    return current_game

#generate a random available number in range(from 1 to 9) and write in the game table with the cpu_symbol
def cpu_choice(cpu_symbol):
    global current_game,numbers_played
    cpu = random.choice(cpu_options)
    numbers_played += cpu
    cpu_options.remove(cpu)
    for x in range(0, len(game)):
             if user in game[x]:
                 current_game = current_game.replace(cpu, cpu_symbol, 1)
    return current_game

#check if someone win with the 8 possible combinations
def winner_check():
    global winner_symbol
    if current_game[1] == current_game[3] == current_game[5]:
        winner_symbol = current_game[1]
    elif current_game[9] == current_game[11] == current_game[13]:
        winner_symbol = current_game[9]
    elif current_game[-7] == current_game[-5] == current_game[-3]:
        winner_symbol = current_game[-7]
    elif current_game[1] == current_game[9] == current_game[-7]:
        winner_symbol = current_game[1]
    elif current_game[3] == current_game[11] == current_game[-5]:
        winner_symbol = current_game[3]
    elif current_game[5] == current_game[13] == current_game[-3]:
        winner_symbol = current_game[5]
    elif current_game[1] == current_game[11] == current_game[-3]:
        winner_symbol = current_game[1]
    elif current_game[-7] == current_game[11] == current_game[5]:
        winner_symbol = current_game[-7]

    return winner_symbol

print("\n##### Welcome to the Tic Tac Toe game ######\n")

while not players:
    alone = input("Do you want to play alone? 1-(yes), 2-(not): ")
    if alone == "1":
        two_players = False
        players = True
    elif alone == "2":
        two_players = True
        players = True
    else:
        pass

#Make the user to take a choice wich one symbol want to take
while user_symbol != "X" or user_symbol != "O":
    if user_symbol == "X" or user_symbol == "O":
        break
    user_symbol_choosed = input("Chose the symbol for the player 1,\n"
                                "press 1 for ( X ) or press 2 for ( O ): ")
    if user_symbol_choosed == "1":
        user_symbol = "X"
        cpu_symbol = "O"
        break
    elif user_symbol_choosed == "2":
        user_symbol = "O"
        cpu_symbol = "X"
        break
    else:
        print("Invalid input!!!")

print(f"\nThe Player 1 have the symbol ({user_symbol})")
if two_players:
    print(f"The Player 2 have the sybol ({cpu_symbol})")
else:
    print(f"The CPU have the symbol ({cpu_symbol})")


while game_run:
    current_game = ""
    winner_symbol = "None"
    numbers_played = ""
    cpu_options = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    show_the_game()
    print(f"############\n{current_game}############")

    while winner_symbol == "None":

        if two_players:
            user = input(f"Player 1:Where do you want to put the {user_symbol}?: ")
        elif not two_players:
            user = input(f"Where do you want to put the {user_symbol}?: ")

        if user.isnumeric() == False or int(user) not in range(1,10):
            print("Is not a number or out of range, please chose an available number betwen 1 and 9")
            print(f"############\n{current_game}############")
            print(f"This number are already taked\n######{[number for number in numbers_played]}#######")

        elif user not in numbers_played :
            user_choice(user, user_symbol)
            if winner_check() == user_symbol:
                print("you win")
                yes_or_not = input("If you want to play again press number 1: ")
                if yes_or_not == "1":

                    break
                else:
                    print("thanks for play")
                    game_run = False
                    break

            if len(numbers_played) == 9:
                print("This game is Draw")
                yes_or_not = input("If you want to play again press number 1: ")
                if yes_or_not == "1":
                    break
                else:
                    print("thanks for play")
                    game_run = False
                    break

            if two_players:
                next_player = False
                print(current_game)
                while not next_player:
                    user_2 = input(f"Player 2:Where do you want to put the {cpu_symbol}: ")
                    if user_2.isnumeric() == False or int(user_2) not in range(1, 10) or user_2 in numbers_played:
                        print("Is not a number or out of range, please chose an available number betwen 1 and 9")
                        print(f"############\n{current_game}############")
                        print(f"This number are already taked\n######{[number for number in numbers_played]}#######")
                    else:
                        next_player = True
                        break

                user_choice(user_2, cpu_symbol)
                if winner_check() == cpu_symbol:
                    print("Player 2 is the winner")
                    yes_or_not = input("If you want to play again press number 1: ")
                    if yes_or_not == "1":
                        break
                    else:
                        print("thanks for play")
                        game_run = False
                        break

            if len(numbers_played) == 9:
                print("This game is Draw")
                yes_or_not = input("If you want to play again press number 1: ")
                if yes_or_not == "1":
                    break
                else:
                    print("thanks for play")
                    game_run = False
                    break

            elif not two_players:
                print("Something wrong")
                cpu_choice(cpu_symbol)
                if winner_check() == cpu_symbol:
                    print("you lose")
                    yes_or_not = input("If you want to play again press number 1: ")
                    if yes_or_not == "1":
                        break
                    else:
                        print("thanks for play")
                        game_run = False
                        break

            print(f"############\n{current_game}############")
            print(f"This number are already taked\n######{[number for number in numbers_played]}#######")
        else:
            print("This place is already taked or wrong input! Try again")
            print(current_game)
            print(f"This number are already taked\n######{[number for number in numbers_played]}#######")

import random


def game_plan() :
    game_on = True

    cpu_list = ["rock", "paper", "scissors"]
    cpu_call = random.choice(cpu_list)
    user = input("Enter your name ").lower()
    user_call = input("Enter  your call : 'R' for rock, 'P' for paper and 'S' for scissors ").lower()

    while game_on:

        if cpu_call == "rock":
            if user_call == "r":
                print("its a  tie")
                recall = input("like to play again 'yes' or 'no'  ").lower()
                if recall == "yes":
                    game_plan()
                else:
                    game_on = False
            elif user_call == 'P':
                print(f'{user} wins computer lose')
                recall = input('Want to play again? "y" or "n" ').lower()
                if recall == "yes":
                    game_plan()
                else:
                    game_on = False
            elif user_call == 's':
                print(f'{user} lose computer wins')
                recall = input('Want to play again? "y" or "n" ').lower()
                if recall == "yes":
                    game_plan()
                else:
                    game_on = False
            else:
                print("input the correct choice")

        elif cpu_call == 'paper':
            if user_call == 'R':
                print(f'{user} lose computer wins')
                recall = input('Want to play again? "y" or "n": ').lower()
                if recall == 'y':
                    game_plan()
                else:
                    game_on = False
            elif user_call == 'P':
                print('It is a tie')
                recall = input('Want to play again? "y" or "n": ').lower()
                if recall == 'y':
                    game_plan()
                else:
                    game_on = False
            elif user_call == 'S':
                print(f'{user} wins computer lose')
                recall = input('Want to play again? "y" or "n": ').lower()
                if recall == 'y':
                    game_plan()
                else:
                    game_on = False
            else:
                print('Input the correct choice')
                game_plan()
        else:
            if user_call == 'R':
                print(f'{user} wins computer lose')
                recall = input('Want to play again? "y" or "n": ').lower()
                if recall == 'y':
                    game_plan()
                else:
                    game_on = False
            elif user_call == 'P':
                print(f'{user} lose computer wins')
                user_tie_input = input('Want to play again? "y" or "n": ').lower()
                if user_tie_input == 'y':
                    game_plan()
                else:
                    game_on = False
            elif user_call == 'S':
                print('It is a tie')
                recall = input('Want to play again? "y" or "n": ').lower()
                if recall == 'y':
                    game_plan()
                else:
                    game_on = False
            else:
                print('Input the correct choice')
                game_plan()


game_plan()
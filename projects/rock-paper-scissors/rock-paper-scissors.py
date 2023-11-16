import random

def janken_game(user_input, user_points, computer_points):
    game_options = ["rock", "paper", "scissors"]
    computer_input = random.choice(game_options)

    if user_input == computer_input:
        print("Tie!")
        print("Game well played! :) \n")

    else:
        if user_input == "rock":
            if computer_input == "scissors":
                user_points += 1
                print("Your input is rock")
                print("Computer's input is scissors")
                print("You won! :) \n")
                print(f"Your score is {user_points} and computer score is {computer_points}")


            elif computer_input == "paper":
                computer_points += 1
                print("Your input is rock")
                print("Computer's input is papper")
                print("You lost! :( \n")
                print(f"Your score is {user_points} and computer score is {computer_points}")
                
            else:
                print("Your input is rock")
                print("Computer's input is rock")
                print("It's a tie \n")
                print(f"Your score is {user_points} and computer score is {computer_points}")


        elif user_input == "scissors":
            if computer_input == "rock":
                print("Your input is scissors")
                print("Computer's input is rock")
                print("You lost! :( \n")
                computer_points += 1

            elif computer_input == "paper":
                print("Your input is scissors")
                print("Computer's input is paper")
                print("You won! :) \n")
                user_points +=1

            elif computer_input == "scissors":
                print("It's a tie!")
                print("Game well played! :) \n")

            else :
                print("Invalid input")

        elif user_input == "paper":
            if computer_input == "rock":
                print("Your input is paper")
                print("Computer input is rock")
                print("You won! :) \n")
                user_points += 1
                

            elif computer_input == "scissors":
                print("Your input is paper")
                print("Computer's input is scissors")
                print("You lost! :( \n")
                computer_points += 1

            elif computer_input == "paper":
                print("It's a tie!")
                print("Game well played! :) \n")

            else:
                print("Invalid input")

        elif user_input == "exit":
            print(f"Your score is {user_points} and computer score is {computer_points}")
            
        else:
            print("Invalid input")



while True:
    user_points = 0
    computer_points = 0
    print("Enter rock, paper, scissors or exit to play and exit game respectively!")
    user_input = input("Enter your game option: ").lower()

    if user_input != "exit":
        janken_game(user_input, user_points, computer_points)

    else:
        print(f"Your score is {user_points} and computer score is {computer_points}")
        quit()


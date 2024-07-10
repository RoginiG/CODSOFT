import random
game="rock","paper","scissor"
user_score=0
computer_score=0
def game_result(user_score,computer_score):
    user=input("do you want play another round(yes/no):")
    if user=="yes":
        user_choice_and_computer_choice()
    else:
        print(f"The user game score is {user_score} and computer game score is {computer_score}")
        if user_score==computer_score:
            print("Game ties!!")
            print("Thanks for playing")
        if user_score>computer_score:
            print("user wins the game!!")
            print("Thanks for playing")
        if user_score<computer_score:
            print("computer wins the game!!")
            print("Thanks for playing")
def Game_round(user_choice,computer_choice):
    global user_score,computer_score
    if user_choice=="paper" and computer_choice=="['paper']":
        print("Tie the game")
        user_score+=1
        computer_score=+1
    elif  user_choice=="rock" and computer_choice=="['rock']":
        print("Tie the game")
        user_score+=1
        computer_score+=1
    elif user_choice=="scissor" and computer_choice=="['scissor']":
        print("Tie the game")
        user_score+=1
        computer_score+=1
    elif user_choice=="paper" and computer_choice=="['rock']":
        print("you wins the round")
        user_score+=1
    elif user_choice=="scissor" and computer_choice=="['paper']":
        print("you wins the round")
        user_score+=1
    elif user_choice=="rock" and computer_choice=="['scissor']":
        print("you wins the round")
        user_score+=1
    else:
        print("computer wins the round")
        computer_score+=1
    game_result(f"{user_score}",f"{computer_score}")
def user_choice_and_computer_choice():
    print("Game starts")
    user_choice=input(f"enter your choice in {game}:")
    computer_choice=random.choices(game)
    print(f"The computer choice in {game}:{computer_choice}")
    if user_choice  in game:
        Game_round(f"{user_choice}",f"{computer_choice}")
    else:
        print("please give the valid choice")
user_choice_and_computer_choice()

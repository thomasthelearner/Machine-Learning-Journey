import random

def play_game():
    player = int(input("""
    ================================
    Rock Paper Scissors Lizard Spock
    ================================

    1) ✊
    2) ✋
    3) ✌️
    4) 🦎
    5) 🖖

    Pick a number: """))
    computer = random.randint(1, 5)

    if player == computer:
        print(f"""
    You chose {player}, computer chose {computer}. 
    It's a tie!""")
    elif player == 1 and computer == 2:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Paper covers Rock.""")
    elif player == 1 and computer == 3:
            print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Rock breaks Scissors.""")
    elif player == 1 and computer == 4:
                print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Rock crushes Lizard.""")
    elif player == 1 and computer == 5:
                print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Rock beats Spock.""")
    elif player == 2 and computer == 1:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Paper covers Rock.""")
    elif player == 2 and computer == 3:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Scissors cut Paper.""")
    elif player == 2 and computer == 4:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Lizard eats Paper.""")
    elif player == 2 and computer == 5:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Spock vaporizes Paper.""")
    elif player == 3 and computer == 1:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Rock breaks Scissors.""")
    elif player == 3 and computer == 2:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Scissors cut Paper.""")
    elif player == 3 and computer == 4:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Lizard cuts Scissors.""")
    elif player == 3 and computer == 5:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Spock smashes Scissors.""")
    elif player == 4 and computer == 1:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Lizard beats Rock.""")
    elif player == 4 and computer == 2:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Paper beats Lizard.""")
    elif player == 4 and computer == 3:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Scissors beats Lizard.""")
    elif player == 4 and computer == 5:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Lizard poisons Spock.""")
    elif player == 5 and computer == 1:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Rock beats Spock.""")
    elif player == 5 and computer == 2:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Spock beats Paper.""")
    elif player == 5 and computer == 3:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You win! Spock beats Scissors.""")
    elif player == 5 and computer == 4:
        print(f"""
    You chose {player}, computer chose {computer}. 
    You lose! Lizard beats Spock.""")
    else:
        print("Invalid input. Please choose a number between 1 and 5.")

play_game()
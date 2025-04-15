import random
user_score = 0
computer_score = 0
user_choice = ''
computer_choice = ''


def play_game():
    global user_choice, computer_choice
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Enter your choice (rock, paper, scissors): ")

    print("Computer chose:" + computer_choice)
    print("You chose:" + user_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("User Score:", user_score)
    print("Computer Score:", computer_score)

while user_score < 10 and computer_score < 10:
    play_game()
    user_score, computer_score = count_score()

if user_score == 10:
    print("You win the game")
else:
    print("Computer wins the game")

"""

def count_score(): 
        

    if user_choice == computer_choice:
        pass
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'paper' and computer_choice == 'rock') or \
        (user_choice == 'scissors' and computer_choice == 'paper'):
        user_score += 1
    else:
        computer_score += 1
        
    print("User Score:", user_score)
    print("Computer Score:", computer_score)
    return user_score, computer_score
    
    user_score, computer_score = count_score()


while user_score < 10 and computer_score < 10:
    play_game() 
    user_score, computer_score = count_score()
""" 
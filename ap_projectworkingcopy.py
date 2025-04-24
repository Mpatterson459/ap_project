import random
user_score = 0
computer_score = 0
user_choice = ''
computer_choice = ''


#Only the play game function is from copiolt
def play_game():
    global user_choice, computer_choice
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
    else:
        print("Computer wins!")

#All the rest is myself

def count_score(): 
    global user_score, computer_score
        

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
    
def play_again(play_more):
    if play_more == 'yes':
        return True
    elif play_more == 'no':
        print("Thanks for playing!")
        return False
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        return play_again(input("Do you want to play again? (yes/no): "))
    

while True:
    user_score = 0
    computer_score = 0

    while user_score < 10 and computer_score < 10:
        play_game() 
        count_score()

    if user_score == 10:
        print("You win the game")
    else:
        print("Computer wins the game")
    
    play_more = input("Do you want to play again? (yes/no): ")
    if not play_again(play_more):
        break

    
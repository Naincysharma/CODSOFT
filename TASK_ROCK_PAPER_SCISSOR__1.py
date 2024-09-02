import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determinewinner(userchoice, computerchoice):
    if userchoice == computerchoice:
        return 'tie'
    elif (userchoice == 'rock' and computerchoice == 'scissors') or \
         (userchoice == 'scissors' and computerchoice == 'paper') or \
         (userchoice == 'paper' and computerchoice == 'rock'):
        return 'win'
    else:
        return 'lose'

def playgame():
    user_score = 0
    computer_score = 0

    while True:
        print("Welcome to Rock, Paper, Scissors!")
        print("Please choose: rock, paper, or scissors.")
        userchoice = input("Your choice: ").strip().lower()

        if userchoice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        computerchoice = get_computer_choice()
        print(f"Computer chose: {computerchoice}")

        result = determinewinner(userchoice, computerchoice)

        if result == 'win':
            print("You win!")
            user_score += 1
        elif result == 'lose':
            print("You lose.")
            computer_score += 1
        else:
            print("It's a tie.")

        print(f"Score - You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    playgame()

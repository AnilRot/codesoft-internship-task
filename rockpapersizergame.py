import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors"""
    while True:
        user_input = input("\nChoose rock (r), paper (p), or scissors (s): ").lower()
        if user_input in ['r', 'rock']:
            return 'rock'
        elif user_input in ['p', 'paper']:
            return 'paper'
        elif user_input in ['s', 'scissors']:
            return 'scissors'
        else:
            print("Invalid choice. Please enter rock (r), paper (p), or scissors (s).")

def get_computer_choice():
    """Generate a random choice for the computer"""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the game rules"""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, result, scores):
    """Display the game results and current scores"""
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    
    if result == 'tie':
        print("It's a tie!")
    elif result == 'user':
        print("You win!")
    else:
        print("Computer wins!")
    
    print(f"\nCurrent Scores - You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")

def play_game():
    """Main game function"""
    scores = {'user': 0, 'computer': 0, 'tie': 0}
    
    print("=== Rock-Paper-Scissors Game ===")
    print("Rules: Rock beats scissors, scissors beat paper, and paper beats rock.")
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        result = determine_winner(user_choice, computer_choice)
        
        scores[result] += 1
        display_result(user_choice, computer_choice, result, scores)
        
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("\nFinal Scores:")
            print(f"You: {scores['user']} | Computer: {scores['computer']} | Ties: {scores['tie']}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
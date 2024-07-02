import random

choices = ["rock", "paper", "scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while user_choice not in choices:
        user_choice = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(choices)

def play_round():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")
    
    return winner

def play_game(rounds_to_win):
    user_score = 0
    computer_score = 0
    rounds_played = 0

    while user_score < rounds_to_win and computer_score < rounds_to_win:
        print(f"\nRound {rounds_played + 1}")
        winner = play_round()
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1
        
        rounds_played += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")

    if user_score > computer_score:
        print("\nCongratulations! You won the game!")
    else:
        print("\nComputer wins the game! Better luck next time.")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    rounds_to_win = 3  
    play_game(rounds_to_win)

if __name__ == "__main__":
    main()

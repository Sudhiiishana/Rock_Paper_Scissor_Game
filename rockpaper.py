import random

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n" + "="*30)
        print("ROCK-PAPER-SCISSORS GAME")
        print("="*30)
        print(f"Current Score - You: {user_score} | Computer: {computer_score}")
        print("\nChoose one:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        
        # User input with validation
        while True:
            try:
                user_choice = int(input("Enter your choice (1-3): "))
                if user_choice in [1, 2, 3]:
                    break
                else:
                    print("Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Map numbers to choices
        choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
        user_choice_name = choices[user_choice]
        
        # Computer selection
        computer_choice = random.randint(1, 3)
        computer_choice_name = choices[computer_choice]
        
        print(f"\nYou chose: {user_choice_name}")
        print(f"Computer chose: {computer_choice_name}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 1 and computer_choice == 3) or \
             (user_choice == 2 and computer_choice == 1) or \
             (user_choice == 3 and computer_choice == 2):
            print(f"{user_choice_name} beats {computer_choice_name}. You win!")
            user_score += 1
        else:
            print(f"{computer_choice_name} beats {user_choice_name}. Computer wins!")
            computer_score += 1
        
        # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nFinal Score:")
            print(f"You: {user_score} | Computer: {computer_score}")
            if user_score > computer_score:
                print("Congratulations! You won the game!")
            elif user_score < computer_score:
                print("Computer won the game. Better luck next time!")
            else:
                print("The game ended in a tie!")
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()
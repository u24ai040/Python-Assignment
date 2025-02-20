import random

class Rock_paper_scissors:
    def __init__(self, total_rounds):
        """Initialize game with number of rounds and tracking scores."""
        self.total_rounds = total_rounds
        self.current_round = 1
        self.user_wins = 0
        self.computer_wins = 0
        self.choices = ['1', '2', '3']

    def get_computer_choice(self):
        """Randomly selects and returns the computer's choice."""
        return random.choice(self.choices)

    def find_winner(self, user_choice, computer_choice):
        """Determines the winner of the round and updates scores."""
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == '1' and computer_choice == '3') or \
             (user_choice == '3' and computer_choice == '2') or \
             (user_choice == '2' and computer_choice == '1'):
            self.user_wins += 1
            return "You win this round!"
        else:
            self.computer_wins += 1
            return "Computer wins this round!"

    def check_winner(self):
        """Checks if someone has won the game."""
        if self.user_wins > self.total_rounds // 2:
            return "Congratulations! You won the game!"
        elif self.computer_wins > self.total_rounds // 2:
            return "Computer wins the game."
        return None

    def play_game(self):
        """Handles the game loop with user input."""
        print(f"Welcome to Rock_paper_scissors! Best of {self.total_rounds} rounds.\n")
        
        while self.current_round <= self.total_rounds:
            print(f"Round {self.current_round}")
            print("Enter 1 for Rock, 2 for Scissors, or 3 for Paper.")
            user_choice = input("Enter 1, 2, or 3: ")
            while user_choice not in self.choices:
                user_choice = input("Invalid choice. Please enter 1, 2, or 3: ")
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            
            print(self.find_winner(user_choice, computer_choice))
            
            winner_message = self.check_winner()
            if winner_message:
                print(winner_message)
                break
            
            self.current_round += 1
        
        print("Game Over!")

if __name__ == "__main__":
    rounds = int(input("Enter the number of rounds to play: "))
    game = Rock_paper_scissors(rounds)
    game.play_game()
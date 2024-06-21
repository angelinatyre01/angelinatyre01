import random
from datetime import datetime
import os
import pandas as pd

# Dictionary to store high scores
high_scores = {}

# Check if the game_results.txt file exists
filename = "game_results.txt"
if not os.path.exists(filename):
    with open(filename, "a"):
        pass

def get_best_score(player_name):
    """
    Get the best score (lowest number of attempts) for a player.

    Parameters:
    - player_name (str): The name of the player.

    Returns:
    int: The best score for the player.
    """
    return high_scores.get(player_name, float('inf'))

def write_results_to_file(player_name, attempts):
    """
    Write the game results, including the best score, to a file.

    Parameters:
    - player_name (str): The name of the player.
    - attempts (int): The number of attempts in the current game.

    Returns:
    None

    This function appends the game results to the 'game_results.txt' file. The results include the player's name,
    the number of attempts in the current game, and the player's best score.
    """
    with open(filename, "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{timestamp} - Player: {player_name}, Attempts: {attempts}, Best Score: {get_best_score(player_name)}\n")

def play_game():
    """
    Play a single round of the guessing game.

    Returns:
    None
    """
    print("Welcome to the Guessing Game!")
    print("I've selected a number between 1 and 100. Can you guess it?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    attempts = 0
    while True:
        try:
            # Get the player's guess
            guess = int(input("Enter your guess: "))

            # Increment the number of attempts
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

                # Update high scores
                player_name = input("Enter your name: ")
                if player_name not in high_scores or attempts < high_scores[player_name]:
                    high_scores[player_name] = attempts
                    print(f"New high score for {player_name}! Attempts: {attempts}")

                # Simulate calling write_results_to_file after a game
                write_results_to_file(player_name, attempts)

                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

def display_high_scores():
    """
    Display high scores using Pandas DataFrame.

    Returns:
    None
    """
    # Convert high scores dictionary to DataFrame
    scores_df = pd.DataFrame(list(high_scores.items()), columns=['Player', 'Attempts'])

    # Display high scores
    print("\nHigh Scores:")
    print(scores_df)

if __name__ == "__main__":
    while True:
        play_game()

        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    # Display high scores using Pandas DataFrame
    display_high_scores()

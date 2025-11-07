import random

def get_word():
    """Selects a random word from a predefined list."""
    words = ['python', 'hangman', 'programming', 'computer', 'keyboard', 'apple', 'banana', 'bookkeeper']
    return random.choice(words)
def play_game():
    """Main function to run the Hangman game."""
    word = get_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    
    while incorrect_guesses < max_incorrect_guesses:
        # Display the current state of the word
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(f"\nWord: {display_word}")
        
        # Display incorrect guesses
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        # Check if the word has been guessed
        if "_" not in display_word:
            print("\nCongratulations! You've guessed the word correctly!")
            break
            
        # Get player input
        guess = input("Guess a letter: ").lower()
        
        # Validate the input
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
            
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try a new one.")
            continue
        
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            incorrect_guesses += 1
            
    # Game over
    if incorrect_guesses >= max_incorrect_guesses:
        print("\nGame Over! You ran out of guesses.")
        print(f"The word was: {word}")

if __name__ == "__main__":
    play_game()




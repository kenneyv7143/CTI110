#Valerie Kenney 

#9 May 2026

#final project 8    

#Spelling Game for First and Second Graders that keeps score .

import random

def run_spelling_game():
    # Vocabulary list suitable for 1st and 2nd graders
    words = ["Apple", "House", "School", "Friend", "Garden", "Smile", "Happy", "Bread", "Water", "Lunch"]
    
    print("--- SPELLING ADVENTURE ---")
    name = input("What is your name? ").strip().capitalize()
    print(f"Welcome, {name}! Let's fill in the missing letters.")
    
    score = 0
    total_chances = 6

    for round_num in range(1, total_chances + 1):
        # Pick a random word and capitalize it
        word = random.choice(words).upper()
        
        # Select one random index to hide
        blank_index = random.randint(0, len(word) - 1)
        correct_letter = word[blank_index]
        
        # Create the display word (e.g., A_PLE)
        display_word = list(word)
        display_word[blank_index] = "_"
        
        print(f"\nRound {round_num}: " + " ".join(display_word))
        
        # Loop until we get a valid letter input
        user_guess = ""
        while True:
            user_guess = input("What letter is missing? ").strip().upper()
            
            if len(user_guess) == 1 and user_guess.isalpha():
                break
            print("Please pick just ONE letter from the alphabet!")

        if user_guess == correct_letter:
            print(f"Great job, {name}! {word} is correct.")
            score += 1
        else:
            print(f"Nice try! The full word was {word}.")
            
        print(f"Current Score: {score}")

    print(f"\nGame Over! You got {score} out of {total_chances} correct.")
    print(f"Way to go, {name}!")

if __name__ == "__main__":
    run_spelling_game()


'''
Design python program that aids 1st and 2nd graders by spelling via fill in the blanks.
 Ask player's name and welcome them. Capitalize each word. Allow for letter input only 
 Give each player up to 3 tries per word. if right letter not picked after 3rd attempt, give correct answer.
give option to play or stop up to 6 games.
'''



# hangman game
import random
from words_list import words

hangman_art = {0:  ("   ",
                    "   ",
                    "   "),
            
                1: (" o ",
                    "   ",
                    "   "),
                
                2: (" o ",
                    " | ",
                    "   "),
                
                3: (" o ",
                    "/| ",
                    "   "),
                
                4: (" o ",
                    "/|\\",
                    "   "),
                
                5: (" o ",
                    "/|\\",
                    "/  "),
                
                6: (" o ",
                    "/|\\",
                    "/ \\")}

def display_man(wrong_guesses):
    print("***************************")
    # wrong_guesses is an integer
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("***************************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words) # pick random word in words_list to be guessed
    hint = ["_"] * len(answer) # set the hint to _ according to the length of answer
    wrong_guesses = 0 
    guessed_letters = set() # user input
    is_running = True # will keep the loop running
    
    while is_running: 
        display_man(wrong_guesses) # displays hangman art
        display_hint(hint) # displays hint
        guess = input("Enter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input!")
            continue
        
        if guess in guessed_letters: # will not let the user input the same letter again previously
            print(f"{guess} is already guessed") # wrong_guesses is not incremented even if it's wrong
            continue
        guessed_letters.add(guess) # adds letter to the guessed_letters
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess: # if character in the answer == user's guess
                    hint[i] = guess # then the user's guess is displayed in hint (consisting of _ at first)
        else:
            wrong_guesses += 1 # else, wrong guesses is incremented
            
        if "_" not in hint: # means the hint is filled and user has guessed all of the letters
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False # terminates the program
            
        elif wrong_guesses >= len(hangman_art) - 1: # if wrong guesses is not more than 6 
            display_man(wrong_guesses)
            print("YOU LOSE!")
            is_running = False # terminates the program
            
if __name__ == "__main__":
    main()
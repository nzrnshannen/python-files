import numpy as np

QUIT = 0
input_name = ""
best_classic = 999
best_unli = 999
# creating the functions
def stats():
    print("*****")
    print(input_name + "'s Statistics")
    print("Classic = " + str(best_classic) + " tries")
    print("Unlimited = " + str(best_unli) + " tries")
    
    return

def rules():
    print("test rules")
    return

def menu():
    print("\tWelcome, " + input_name + "!")
    print("[1] Classic")
    print("[2] Unlimited")
    print("[3] Rules")
    print("[4] View Stats")
    print("[0] QUIT")
    print("===============")
    
    try:
        user_choice = input("Choice: ")
        choice = int(user_choice)
        
    except ValueError:
        print("\nInvalid input. Try again!")
        menu()

    return choice

def classic_mode():
    tries = 0
    secret = np.random.randint(0, 101)
    
    while tries <= 3:
        try:
            input_guess = input("Guess: ")
            input = int(input_guess)
            if input >= 0:
                tries = tries + 1
                if input == secret:    
                    print("NOICE! The number was: " + str(secret))
                    print("Tries: " + str(tries) + "\n")
                    if best_classic > tries:
                        best_classic = tries
                    break
            else:
                print("Enter a positive number!")
                continue
            
        except ValueError:
            print("Invalid input. Try again!\n")
    
    if tries > 3:
        print("GAME OVER. The number was: " + str(secret))
    
def unli_mode():
    secret = np.random.randint(0, 101)

    while True:
        try:
            input_guess = input("Guess: ")
            input = int(input_guess)
            if input >= 0:
                tries = tries + 1
                if input == secret:
                    print("NOICE! The number was: " + str(secret))
                    print("Tries: " + str(tries) + "\n")
                    if best_unli > tries:
                        best_unli = tries
                    break
        except ValueError:
            print("Invalid input. Try again!\n")
            continue
    return


# start

username = input("Enter your name: ")
choice = menu()
while choice != QUIT: 
    if choice < 0 or choice > 4:
        print("\tEnter values 0 - 4\n")
        choice = menu()
    
    def switch(choice):
        if choice == 1:
            print("\n***********************")
            print("> CLASSIC MODE <\n")
            classic_mode()
            return
        elif choice == 2:
            print("\n***********************")
            print("> UNLIMITED MODE <\n")
            unli_mode()
            return
        elif choice == 3:
            rules()
            return
        elif choice == 4:
            stats()
            return
    
    choice = menu()
    

print("\n*** END OF PROGRAM")
    

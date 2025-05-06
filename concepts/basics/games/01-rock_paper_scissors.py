# rock paper scissors
import random

playerName = input("Enter your name: ")

print(f"Welcome, {playerName}!");

playerScore = computerScore = 0;
LIMIT = 5 # interchangeable
game_running = True
options = ['rock', 'paper', 'scissors']

def generateComputerMove():
    return random.choice(options)

def showMoves(playerMove, computerMove):
    print(f"{playerName} choose {playerMove}. Computer choose {computerMove}.");
    
def showScores(playerScore, computerScore):
    print(f"{playerName}: {playerScore} | Computer: {computerScore}");

def updateScore(score): # redundant
    return score + 1

print("\n\tROCK, PAPER, SCISSORS")
while game_running:
    print('------------------------------------------')
    playerMove = input("Choose your move ([Q] to quit): ").lower().strip()
    print()
    computerMove = generateComputerMove();
    
    if playerMove == 'q':
        game_running = False
    elif playerMove not in options:
        print("\tINVALID MOVE. TRY AGAIN. ")
        print()
    else:
        showMoves(playerMove, computerMove)
        if computerMove == playerMove:
            print("Tie.")
        elif playerMove == 'scissors' and computerMove == 'rock':
            print("You lose!")
            computerScore = updateScore(computerScore)
        elif playerMove == 'scissors' and computerMove == 'paper':
            print("You win!")
            playerScore = updateScore(playerScore)
        elif playerMove == 'paper' and computerMove == 'rock':
            print("You win!")
            playerScore = updateScore(playerScore)
        elif playerMove == 'paper' and computerMove == 'scissors':
            print("You lose!")
            computerScore = updateScore(computerScore)
        elif playerMove == 'rock' and computerMove == 'paper':
            print("You lose!")
            computerScore = updateScore(computerScore)
        elif playerMove == 'rock' and computerMove == 'scissors':
            print("You win!")
            playerScore = updateScore(playerScore)

        showScores(playerScore, computerScore)
        
        if playerScore == LIMIT or computerScore == LIMIT:
            game_running = False
    
    
if playerMove == 'q' and (computerScore < LIMIT or playerScore < LIMIT):
        print('\t---- SESSION TERMINATED ----')
else:
    print("=================================================")
    print(f"{playerName} wins!" if playerScore == LIMIT else "Computer wins!")    

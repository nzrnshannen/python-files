# slot machine
import random 
import time

def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    
    # for every iteration in range(3), return a random symbol
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print("*************************")
    print("    |   ".join(row)) # join each element by the given string
    print("*************************")
    
def get_payout(row, bet):
    payout = 0
    if row[0] == row[1] == row[2]:
        match row[0]:
            case '🍒':
                payout = bet * 3
            case '🍉':
                payout = bet * 4
            case '🍋':
                payout = bet * 5
            case '🔔':
                payout = bet * 10
            case '⭐':
                payout = bet * 20
    return payout

def show_symbols():
    print("Symbols: 🍒 | 🍉 | 🍋 | 🔔 | ⭐ ")
    print("********************************")
def main():
    balance = 100
    
    print("********************************")
    print("WELCOME TO PYTHON SLOTS")
    print("Symbols: 🍒 | 🍉 | 🍋 | 🔔 | ⭐ ")
    print("********************************")

    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number.")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("Insufficient funds")
            continue
        
        if bet <=0:
            print("Bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        
        print("Spinning...\n")
        time.sleep(1)
        print_row(row)
        
        # payout added to balance
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f">> You won ${payout}! <<\n")
        else:
            print(">> Sorry, you lost this round. <<\n")
            
        balance += payout
        
        play_again = input("Do you want to spin again? \n[Y] Yes [N] No\n[Choice]: ").upper()
        
        if play_again != 'Y':
            break
        
        print("================================")
        show_symbols()
    
    print("\n ------------- GAME OVER ------------- ")
    print(f"Your final balance is ${balance}.")
        
if __name__ == '__main__':
    main()
# dice roller program

import random 

# print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518")
# ● ┌ ─ ┐ │ └ ┘

# "┌─────────┐"
# "│         │"
# "│         │"
# "│         │"
# "└─────────┘"


dice_art = {
    1: ("┌─────────┐", 
        "│         │", 
        "│    ●    │", 
        "│         │", 
        "└─────────┘"),
    2: ("┌─────────┐", 
        "│  ●      │", 
        "│         │", 
        "│       ● │", 
        "└─────────┘"),
    3: ("┌─────────┐", 
        "│  ●      │", 
        "│    ●    │", 
        "│      ●  │", 
        "└─────────┘"),
    4: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│         │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    5: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│    ●    │", 
        "│  ●   ●  │", 
        "└─────────┘"),
    6: ("┌─────────┐", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "│  ●   ●  │", 
        "└─────────┘")
}

dice = []
total = 0

num_of_dice = int(input("How many dice?: "))

# 1: randomly generates dices and appends it to dice list
for die in range(num_of_dice):
    dice.append(random.randint(1, 6))


# 2: prints dice art
# if num_of_dice = 4:
# die = runs from 0 to 3 [0, 1, 2, 3]
# dice[] = contains random dice numbers 
for die in range(num_of_dice): # 2.a number of iterations (number of dices that will be displayed)
    # How loop works if num_of_dice = 4:
    # dice_art.get(dice[0]) - getting random generated die(0) in dice at index 0 ==> dice_art.get(dice[0]) if dice[0] is 5, then dice_art.get(5) 
    # dice_art.get(dice[1]) - getting random generated die(1) in dice at index 1
    # dice_art.get(dice[2]) - getting random generated die(2) in dice at index 2
    # dice.art'get(dice[3]) - getting random generated die(3) in dice at index 3
    for line in dice_art.get(dice[die]): # 2.b if dice_art.get[5], this loop will print the entire dice_art.get[5] line by line
        print(line)
        
for die in dice:
    total += die

print(f"Total: {total}")
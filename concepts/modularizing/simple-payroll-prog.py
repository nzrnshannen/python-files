# declarations

PROMPT = "Enter hours worked: "
RATE = 13.00

# start

while True:
    try:
        hours_input = input(PROMPT)
        hours = float(hours_input) # having 2.5 hours for instance
        
        if hours > 0:
            # calculations
            pay = hours * RATE
            
            print("\n==============")
            print("Pay = Php" + f"{pay: .2f}")
            break
        
        else:
            print("Please enter a positive number for hours!\n") # if user enter value <= 0
            continue
        
    except ValueError:
        print("\n\tInvalid input. Try again!\n") # if user input a non numeric value
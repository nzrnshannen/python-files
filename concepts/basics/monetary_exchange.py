# 9: program allows user to enter a number of dollars and convert it to Euros and Japanese yen

# =================================
# 1 Euro: 0.920768 EUR
# 1 Japanese Yen: 153.0096 JPY
# ================================

eur_one_dol= 0.920768
jpy_one_dol = 153.0096 

while True:
    dollar_input = input("Enter value in dollars: ")
    
    try: 
        dollar = float(dollar_input)
        if dollar > 0:
            eur_output = float(dollar * eur_one_dol)
            jpy_output = float(dollar * jpy_one_dol)
            
            # Printing results with 2 decimal places
            print("\n=========================================================")
            print(f"{dollar:.2f} dollars in Euros = {eur_output:.2f} EUR")
            print(f"{dollar:.2f} dollars in Japanese Yen = {jpy_output:.2f} JPY")
            break
        else:
            print("Enter a positive value!\n")
            continue
        
    except ValueError:
        print("\n--------------------\nInvalid input. Try again!\n")
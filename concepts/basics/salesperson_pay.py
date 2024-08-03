# 10: a program that allows user to enter values for base salary, total sales, and commission rate

user_name = input("Enter name: ")

base_salary = total_sales = com_rate = 0

while True:
    base_salary_input = input("Enter base salary: ")
    
    try:
        base_salary = float(base_salary_input)
        if base_salary > 0:
            break
        else:
            print("Enter a positive value!\n")
    except ValueError:
        print("\n--------------------------\nInvalid input. Try again!\n")
    
    
while True:
    total_sales_input = input("Enter total sales: ")
    
    try: 
        total_sales = float(total_sales_input)
        if total_sales > 0:
            break
        else:
            print("Enter a positive value!\n")
    except ValueError:
            print("\n--------------------------\nInvalid input. Try again!\n")
            

while True:
    com_rate_input = input("Enter commission rate: ")
    
    try:
        com_rate = float(com_rate_input)
        if com_rate > 0:
            break
        else:
            print("Enter a positive value!\n")
    except ValueError:
            print("\n--------------------------\nInvalid input. Try again!\n")
            
            
# calculations
salesp_pay = (total_sales * com_rate) + base_salary

print("\n===================\n" + user_name + "'s pay = Php" + f"{salesp_pay: .2f}")
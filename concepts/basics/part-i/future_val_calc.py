amt = float(input("Enter principal amount: "))
intr = float(input("Enter rate of interest: "))
yrs = int(input("Enter number of years: "))


print(f"Output = {round((amt * (1 + (0.01  * intr)) ** yrs), 2)}")
# payroll report (converting flowchart & pseudocode to a program)

# declarations
REPORT_HEADING = "\tPayroll Report"
COLUMN_HEADING = "NAME | GROSS | DEDUCTIONS | NET"
END_LINE = "*** End of Report ***"
RATE = 0.25
QUIT = "XXX"
input_name = ""


# creating the functions
def housekeeping():
    print(REPORT_HEADING)
    print(COLUMN_HEADING)
    input_name = input("Enter name: ")
    return input_name

def detailLoop(name):
    input_gross = input("Enter gross: ")
    gross = float(input_gross)
    
    # calculations 
    deduct = gross * RATE
    net = gross - deduct
    
    print("\n=======================")
    print("Name: " + name)
    print("Gross: " + f"{gross: .2f}")
    print("Deduct: " + f"{deduct: .2f}")
    print("Net: " + f"{net: .2f}")
        
    print("***\n")
    
    input_name = input("Enter name: ")
    return input_name

def endOfJob():
    print("\n")
    print(END_LINE)
    

# start
retName = housekeeping()

while True:
    try:
        if retName != QUIT:
            retName = detailLoop(retName)
        else:
            break
    except ValueError:
        print("\nInvalid input. Try again!\n")

endOfJob()

# end of program
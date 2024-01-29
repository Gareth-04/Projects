'''
This piece of software can be used to calculate one or two salaries, 
with the option to include the calculations of 
National Insurance and/or Student Loan.
'''

# The function that takes care of all the tax calculations
def calculateTax(salaries):
    # Variables used for salary comparison
    compareSalary = -1          # Saves the main salary in case its needed for comparison
    salaryDifference = 0        # Used to store the difference of two salaries

    for i in range(salaries):

        # Naming the salaries based on the position within the for loop
        if i == 0:
            i = "main"
        else:
            i = "secondary"
        
        # Lets user to type in their salary
        print("Input the", i ,"annual Gross Pay (up to £10,000,000)")   # Prints text which depends on its position within the for loop
        theSalary = input("£")                                          # Lets user input value
        theSalary = int(theSalary)                                      # Converts the input into integer

        #Checks if the salary is within the limits
        if 0 > theSalary:
            theSalary = 0                                               # changes the salary value to the minimum value possible
            print("Your salary was changed to the lowest possible value - £0")
        elif theSalary > 10000000:
            theSalary = 10000000                                        # changes the salary value to the highest value possible
            print("Your salary was changed to the highest possible value - £10,000,000")

        # Setting up the variables
        tax1 = 0                    # 20% Tax
        tax2 = 0                    # 40% Tax
        tax3 = 0                    # 45% Tax
        theTax = 0                  # Total Tax
        trueSalary = 0              # Salary after deductions
        personalAllowance = 12570   # Personal Allowance
        natIns = 0                  # National Insurance
        stuLoan = 0                 # Student Loan

        # Starting the calculation rules
        # Student Loan (weekly)
        if theSalary > 27295:       # Option only appears after a certain treshold
            userChoice = input("Calculate a Student Loan? / 1. Yes / 2. No ")
            if userChoice == "1":   # Includes the Student Loan calculation if the user inputs number 1
                stuLoan = (theSalary - 27295) * (0.09 + 0.0125)
        
        # National Insurance (weekly)
        if (theSalary / 52) > 242:                          # Option only appears after a certain treshold
            userChoice = input("Calculate the National Insurance? / 1. Yes / 2. No ")
            if userChoice == "1":                           # Includes the Student Loan calculation if the user inputs number 1
                if 242 < (theSalary/52) <= 967:             # First treshold for the National Insurance 
                    natIns = ((theSalary/52) - 242) * 0.12
                elif (theSalary/52) > 967:                  # Second treshold for the National Insurance 
                    natIns = ((967 - 242) * 0.12) + (((theSalary/52) - 967) * 0.02)
        
        # Rule 0 and 1
        if   0 <= theSalary <= personalAllowance:
            print("You earn under the Tax Free Allowance")
            trueSalary = theSalary
        # Rule 2
        elif personalAllowance < theSalary < 50271:
            taxedPay = theSalary - personalAllowance
            theTax = taxedPay * 0.2
            trueSalary = theSalary - theTax
        # Rule 3
        elif 50720 <= theSalary <= 125140:
            if theSalary > 100000:                                                  # For all salaries in range and over 100000
                personalAllowance = personalAllowance - ((theSalary - 100000)/2)    # Tax Free Salary
                if personalAllowance > 0:
                    tax1 = (50270 - personalAllowance) * 0.2
                    tax2 = (theSalary - 50270) * 0.4
                    theTax = tax1 + tax2
                    trueSalary = theSalary - (tax1 + tax2)
                else:
                    tax1 = 50270 * 0.2
                    tax2 = (theSalary - 50270) * 0.4
                    theTax = tax1 + tax2
                    trueSalary = theSalary - (tax1 + tax2)
            else: # In range and Under 100000
                tax1 = (50270 - personalAllowance) * 0.2
                tax2 = (theSalary - 50270) * 0.4
                theTax = tax1 + tax2
                trueSalary = theSalary - (tax1 + tax2)
        # Rule 4
        elif theSalary > 125140:                           #Salaries above 125140 - Part 4
            tax1 = (50270 - personalAllowance) * 0.2
            tax2 = (125140 - 37700) * 0.4
            tax3 = (theSalary - 125140) * 0.45
            theTax = tax1 + tax2 + tax3
            trueSalary = theSalary - (tax1 + tax2 + tax3)

        # Prints the Salary after tax
        trueSalary = trueSalary - stuLoan - (natIns * 52)
        print("Take Home Pay / Yearly: ", "£" + str(round(trueSalary, 2)))

        # Prints Tax
        if theTax > 0:
            yTax = "£" + str(round(theTax, 2))      # This adds currency symbol to the output
            print("Tax / Yearly: ", yTax)
            mTax = "£" + str(round(theTax / 12,2))
            print("Tax / Monthly: ", mTax)          # This takes the total taxable income and divides it by 12 (Monthly)
            wTax = "£" + str(round(theTax / 52, 2))
            print("Tax / Weekly: ", wTax)           # This takes the total taxable income and divides it by 52 (Weekly)

        # Prints National Insurance
        if natIns > 0:
            wIns = "£" + str(round(natIns,2))
            print("National Insurance / Weekly:", wIns)

        # Prints Student Loan
        if stuLoan > 0:
            wLoan = "£" + str(round(stuLoan / 52,2))
            print("Student Loan / Weekly:", wLoan)

        # Separation line between salaries
        print("-" * 50)

        # Comparison of the two salaries
        if compareSalary >= 0:
            if compareSalary > trueSalary:
                salaryDifference = compareSalary - trueSalary
                print("The difference of the two salaries is", "£" + str(round(salaryDifference, 2)))
            elif compareSalary < trueSalary:
                salaryDifference = trueSalary - compareSalary
                print("The difference of salaries is", "£" + str(round(salaryDifference, 2)))
            else:
                print("Both salaries are equal")
        
        # Prepares the variable compareSalary for the comparison of two salaries
        compareSalary = trueSalary



# Start of the program
def main():
    # Lets user to choose how many salaries they want to calculate
    print("1. Calculate one salary / 2. Calculate two salaries")
    userChoice = input("type in your choice: ")

    # Forwarding the users choice over to the calculateTax function
    if userChoice == "1":
        calculateTax(1)
    elif userChoice == "2":
        calculateTax(2)
    else:
        print(1000 * " ")
        main()



if __name__ == "__main__":
    main()

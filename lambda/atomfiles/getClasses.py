"""
Description:
Author: William Lai
Date: 4/20/22
"""
def validateLabInput(prompt, choice1, choice2):
    validInput = False
    while validInput == False:
        userInput = input(prompt)
        if userInput == choice1 or userInput == choice2:
            validInput = True
        else:
            print("Please enter %s or %s. \n" % (choice1, choice2))
    return userInput

def validateDayinput(prompt):
    # days in the schedule
    days = ["A", "B", "C", "D", "E", "F", "G"]

    validInput = False
    while validInput == False:
        # used upper to match characters in list days
        userInput = input(prompt).upper()
        if userInput in days:
            validInput = True
        else:
            print("Please enter a letter day between A and G. \n")
    return userInput

def getLabs(period):
    # checks to see if user input is valid
    haveLab = validateLabInput("Lab Period? (Y/N): ", "Y", "N")
    if haveLab == "Y":
        for index in range(1, 3):
            # checks to see if user input is valid
            labDay = validateDayinput("Day of Lab: ")
            period[index] = labDay

    return period

def getClasses():
    # key is the period number, data is the class name, and two lab days if applicable
    classes = {}
    for i in range(1, 9):
        # the "8th" period is X
        if i == 8:
            i = "X"

        print("\nPeriod %s" % i)
        print("---------------")

        period = ["", "", ""]
        # gets the days with lab
        period = getLabs(period)

        # gets the name of the class
        period[0] = input("Enter your Period %s class: " % i)
        classes[str(i)] = period

    return classes

if __name__ == '__main__':
    classes = getClasses()
    print(classes)

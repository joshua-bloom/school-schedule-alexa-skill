"""
Description:
Author: William
Date: 5/4/22
"""
from getLetterDay import *
from getClasses import *

def checkDate(prompt):
    validInput = False
    validMonth = False
    validDay = False
    validYear = False

    while validInput == False:
        date = input(prompt)
        date = date.split("/")

        try:
            monthNum = int(date[0])
            if monthNum > 12 or monthNum == 0 or len(date[0]) != 2:
                print("Invalid month. Please enter a number between 1 and 12 in the correct form. \n")
            else:
                validMonth = True
        except:
            print("Invalid input. Please enter a number for month in the correct form. \n")

        try:
            dayNum = int(date[1])
            if dayNum > 32 or dayNum == 0 or len(date[1]) != 2: # didn't bother making it work depending on the month, if i have time then i will
                print("Invalid day. Please enter a number between 1 and 31 in the correct form. \n")
            else:
                validDay = True
        except:
            print("Invalid input. Please enter a number for day in the correct form. \n")

        try:
            yearNum = int(date[2])
            if yearNum > 2022 or yearNum < 2021 or len(date[2]) != 4:
                print("Invalid year. Please enter either 2021 or 2022 in the correct form. \n")
            else:
                validYear = True
        except:
            print("Invalid input. Please enter a number for year in the correct form. \n")

        if validMonth and validDay and validYear:
            validInput = True
    date = "/".join(date)

    return date

def makeSchedule():
    schedule = {}
    letterDays = ["A", "B", "C", "D", "E", "F", "G"]
    xDays = ["A", "C", "E", "G"]

    periodNumber = 1
    for day in letterDays:
        periods = []
        for i in range(4):
            if periodNumber == 8:
                periodNumber = 1
            periods.append(str(periodNumber))
            periodNumber += 1
        if day in xDays:
            periods.append("X")
        else:
            periods.append("")
        schedule[day] = periods

    return schedule

def displaySchedule(schedule, classes, letterDay):
    periods = schedule[letterDay]
    print(periods)
    if periods[4] == "X":
        n = 5
    else:
        n = 4
    for period in periods:
        classInfo = classes[period]
        if (classInfo[1] == "" and classInfo[2] == "") or letterDay in classInfo:
            print("Period %s: %s" % (period, classInfo[0]))
        else:
            print("Period %s: Free" % period)

    return


def main():
    schedule = makeSchedule()
    days = readFile("Academic_Calendar.csv")
    classes = getClasses()
    date = checkDate("What is today's date? (mm/dd/yyyy) ")

    displaySchedule(schedule, classes, days[date])




main()

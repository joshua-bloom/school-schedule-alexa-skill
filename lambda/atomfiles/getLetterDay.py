"""
Description:
Author: William Lai
monthDayYear: 3/9/22
"""
def findMonth(str, months):
    for month in months:
        if str == month:
            return months.index(month)+1
    return -1

def getDate(monthDayYear, line):
    months = ["JANUARY", "FEBRUARY", "MARCH", "APRIL", "MAY", "JUNE", "JULY", "AUGUST", "SEPTEMBER", "OCTOBER", "NOVEMBER", "DECEMBER"]
    year = ["2021", "2022"]

    monthNum = findMonth(line[0], months)
    if monthNum != -1:
        if monthNum < 10:
            monthNum = "0" + str(monthNum)
        else:
            monthNum = str(monthNum)
        monthDayYear[0] = monthNum
        if int(monthNum) >= 8:
            monthDayYear[2] = year[0]
        else:
            monthDayYear[2] = year[1]
    else:
        if int(line[1]) < 10:
            line[1] = "0" + line[1]
        numberDay = line[1]
        monthDayYear[1] = numberDay
    date = "/".join(monthDayYear)

    return date

def readFile(filename):
    academicCalendar = open(filename, 'r')

    days = {}
    monthDayYear = ["", "", ""]
    for line in academicCalendar:
        line = line.strip().split(",")

        date = getDate(monthDayYear, line)

        days[date] = line[2]

    academicCalendar.close()

    return days

if __name__ == '__main__':
    # gets the letter day for a certain date
    days = readFile("Academic_Calendar.csv")

    print("test")
    print("05/09/2022, %s" % days["05/09/2022"])

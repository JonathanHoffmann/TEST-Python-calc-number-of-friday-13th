from tabulate import tabulate
#install tabulate:
#pip install tabulate --user

#Set DBG to True for more debug printouts
DBG=False;
def debug(s):
    if(DBG):
        print("debug: " + str(s))

def monday():
    return "monday"
def tuesday():
    return "tuesday"
def wednesday():
    return "wednesday"
def thursday():
    return "thursday"
def friday():
    return "friday"
def saturday():
    return "saturday"
def sunday():
    return "sunday"
def default():
    return "Incorrect day"

switcher = {
    1: monday,
    2: tuesday,
    3: wednesday,
    4: thursday,
    5: friday,
    6: saturday,
    7: sunday
    }

def switch(dayOfWeek):
    return switcher.get(dayOfWeek, default)()

thirteenofmonthdays=[13, 44, 72, 103, 133, 164, 194, 225, 255, 286, 316, 347]
thirteenofmonthdaysleap=[13, 44, 73, 104, 134, 165, 195, 226, 256, 287, 317, 348]
startingDay = 1
Leapyears=["Leap year"]
Years=["Normal year"]
while(startingDay<=7):
    debug("\n\nYear starting with a " + switch(startingDay))
    countF13=0
    currentday = 1
    allFriday=[]
    if(startingDay<=5):
        allFriday.append(6-startingDay);
    elif(startingDay==6):
        allFriday.append(5)
    else:
        allFriday.append(6)
    curFriday=allFriday[0]
    while(curFriday<=366-7):
        curFriday=curFriday+7
        allFriday.append(curFriday)
    
    debug(allFriday)


    while(currentday<=365):
        for thirteen in thirteenofmonthdays:
            if(currentday==thirteen):
                if(currentday in allFriday):
                    countF13 = countF13+1
                    debug("In a year starting with day " + switch(startingDay) + ", the 13th of month " + str(thirteenofmonthdays.index(thirteen)+1) + " will be a friday the 13th.")
        currentday=currentday+1

    debug("A year starting with day " + switch(startingDay) + " will have " + str(countF13) + " Friday the 13th.")
    Years.append(countF13)

    countF13Leap=0
    currentday = 1
    while(currentday<=366):
        for thirteen in thirteenofmonthdaysleap:
            if(currentday==thirteen):
                if(currentday in allFriday):
                    countF13Leap = countF13Leap+1
                    debug("In a LEAPyear starting with day " + switch(startingDay) + ", the 13th of month " + str(thirteenofmonthdaysleap.index(thirteen)+1) + " will be a friday the 13th.")
        currentday=currentday+1

    debug("A LEAPyear starting with day " + switch(startingDay) + " will have " + str(countF13Leap) + " Friday the 13th.")
    Leapyears.append(countF13Leap)
    startingDay=startingDay+1

print("Amount of Friday the 13th in a given year")
data=[Years, Leapyears]
print(tabulate(data, headers=["1st January:", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]))
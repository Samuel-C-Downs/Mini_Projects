import random
import datetime


def gen_bdays(num_bdays):
    ## Makes empty list for bdays to be stored 
    ## startOfYear Jan 1, year doesn't matter but needed for a date object
    bdays = []
    startOfYear = datetime.date(2001, 1, 1)
    for i in range(num_bdays):
        ## For number of bdays, generate random number of days (between 0 and 364) since jan 1 for this simulated Bday
        ## Append this generated Bday to list created above 
        bday = startOfYear + datetime.timedelta(random.randint(0, 364))
        bdays.append(bday)
    return bdays


def match_bday(bdays):
    if len(bdays) == len(set(bdays)):
        print("There are no matching birthdays in this group")
        return None

    for a, bday_A in enumerate(bdays):
        for b, bday_B in enumerate(bdays[a+1 :]):
            if bday_A == bday_B:
                return bday_A


print("get fucked")

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print("How many birthdays should be generated? (Max is 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break
print("")

print("Here are", num_bdays, "randomly generated bithdays:" )
birthdays = gen_bdays(num_bdays)
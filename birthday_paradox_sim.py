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
        ##print("There are no matching birthdays in this group")
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

## Generate list of bdays and assign to variable
birthdays = gen_bdays(num_bdays)
for i, bday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    month_text = MONTHS[bday.month-1]
    date_text = "{} {}".format(month_text, bday.day)
    print(date_text, end ="")

print("")
print("")


## Check for matches in list of generated bdays
match = match_bday(birthdays)

## Display the results
print("In this simulation, ", end = "")

if match != None: 
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print("There are no matches")

print('Generating', num_bdays, 'random birthdays 100,000 times...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulations.')

simMatch = 0 

for i in range(100000):

    if i % 10000 == 0:
        print(i, "simulations run...")

    birthdays = gen_bdays(num_bdays)
    if match_bday(birthdays) != None:
        simMatch += 1

print('100,000 simulations run.')

probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of', num_bdays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', num_bdays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

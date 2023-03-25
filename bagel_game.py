import random 
from random import randint


##Game Parameter
## 1. Number of digits in the random number
## 2. Number of guesses the player gets 

num_dig = 3
max_guess = 10


def get_secret_num():
    ##secret_num = ''.join(["{}".format(randint(0, 9)) for num in range(0, num_dig)])
    secret_num = '123'
    return secret_num

def get_clues(guess, secret_num):
    ## Returns string hint based on the guess and the secret number

    ## Case for when the player gets the answer right
    if guess == secret_num:
        return "You Got It!"
    
    clues = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues)




def main ():
    print('''Bagels, a deductive logic game.
 By Al Sweigart al@inventwithpython.com

 I am thinking of a {}-digit number with no repeated digits.
 Try to guess what it is. Here are some clues:
 When I say:    That means:
   Pico         One digit is correct but in the wrong position.
   Fermi        One digit is correct and in the right position.
   Bagels       No digit is correct.
 
 For example, if the secret number was 248 and your guess was 843, the
 clues would be Fermi Pico.'''.format(num_dig))


while True: #game loop
    secret_num = get_secret_num()
    print('I have thought up a number.')
    print(' You have {} guesses to get it.'.format(max_guess))
    num_guess = 1 
    while num_guess <= max_guess:
        guess = ''
        ## Make sure guess is valid, (correct length, not a decimal and a number)
        while len(guess) != num_dig or not guess.isdecimal():
            print('Guess #{}: '.format(num_guess))
            guess = input('> ')
        clues = get_clues(guess,secret_num)
        print(clues)
        num_guess += 1

        if guess == secret_num:
            break

        if num_guess > max_guess:
            print("You ran out of guesses.")
            print('The answer was {}.'.format(secret_num))
            print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing!')
    


if __name__ == '__main__':
    main()
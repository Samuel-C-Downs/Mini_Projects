import random 


##Game Parameter
## 1. Number of digits in the random number
## 2. Number of guesses the player gets 

num_dig = 3
max_guess = 10

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
    break


def get_secret_num():
    secret_num = 1
    return secret_num



if __name__ == '__main__':
    main()
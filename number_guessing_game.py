import random


try:
    print('Enter the range of numbers to guess: ')
    startRange = int(input('Enter start range: '))
    endRange = int(input('Enter end range: '))

    if startRange >= endRange:
        raise Exception('Start range must be less than end range')

    number_to_guess = random.randint(startRange, endRange)

    maxGuesses = 5
    guessesMade = 0

    while True:

        guess = int(
            input(f'Guess the number between {startRange} and {endRange}: '))

        if guessesMade == maxGuesses:
            print('You ran out of guesses! The correct number was: ', number_to_guess)
            break

        elif guess < number_to_guess:
            print('Too low!')
            guessesMade += 1
            print('Guesses remaining: ', maxGuesses - guessesMade)

        elif guess > number_to_guess:
            print('Too high!')
            guessesMade += 1
            print('Guesses remaining: ', maxGuesses - guessesMade)

        else:
            print('You guessed the number!')
            break


except ValueError:
    print('Please enter a valid number')

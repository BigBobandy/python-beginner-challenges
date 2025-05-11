import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

# dictionaries map key -> value
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '🧻'}

# tuple is read-only list
# choices = ('r', 'p', 's')
choices = tuple(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')


def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')


def determine_winner(user_choice, computer_choice, statistics):
    if user_choice == computer_choice:
        print('Tie!')
        statistics['ties'] += 1
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
            (user_choice == PAPER and computer_choice == ROCK)):
        print('You win!')
        statistics['user_wins'] += 1
        print(
            f'User wins: {statistics['user_wins']} \n Computer wins: {statistics['computer_wins']}')
    else:
        print('You lose!')
        statistics['computer_wins'] += 1
        print(
            f'User wins: {statistics['user_wins']} \n Computer wins: {statistics['computer_wins']}')


def restart_game(statistics):
    while True:
        restart_game = input('Start a new game? (y/n): ').lower()
        if restart_game == 'y':
            statistics['user_wins'] = 0
            statistics['computer_wins'] = 0
            break
        elif restart_game == 'n':
            print('Thanks for playing!')
            break
        else:
            print('Please respond with y or n!')


def display_statistics(statistics):
    print(f"""Stats for this game:
Rounds User won: {statistics['user_wins']}
Rounds Computer won: {statistics['computer_wins']}
Round Ties: {statistics['ties']}
Rounds Played: {statistics['rounds_played']}
Games Played: {statistics['games_played']}""")


def play_game():

    statistics = {'user_wins': 0, 'computer_wins': 0,
                  'ties': 0, 'rounds_played': 0, 'games_played': 0}

    while True:

        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice, statistics)

        if statistics['user_wins'] < 3 and statistics['computer_wins'] < 3:
            should_continue = input('Continue to next round? (y/n): ').lower()
            if should_continue == 'n':
                break
            elif should_continue == 'y':
                continue
            else:
                print('Please respond with y or n!')

        else:
            if statistics['user_wins'] == 3:
                print("Congrats! You won the game! 🎊")
                statistics['games_played'] += 1
                display_statistics(statistics)
                restart_game(statistics)
            elif statistics['computer_wins'] == 3:
                print("The computer wins! Better luck next time!")
                statistics['games_played'] += 1
                display_statistics(statistics)
                restart_game(statistics)


play_game()

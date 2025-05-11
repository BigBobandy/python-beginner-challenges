print('Welcome to my Country Capital Quiz!')

playing = input('Do you want to play?').lower()

if playing != 'y' and playing != 'yes':
    print('Goodbye!')
    quit()

print('Okay! Let\'s play: ')


capital_quiz: dict = {'France': 'Paris', 'Canada': 'Ottawa',
                      'Ireland': 'Dublin', 'Turkey': 'Ankara',
                      'Russia': 'Moscow', 'China': 'Beijing',
                      'Japan': 'Kyoto', 'Afghanistan': 'Kabul',
                      'Germany': 'Berlin', 'Egypt': 'Cairo', }


def start_quiz():
    quiz: list = list(capital_quiz.items())

    answered_correctly: int = 0

    for question in quiz:
        answer: str = input(f'What is the capital of {question[0]}? ').lower()

        if answer == question[1].lower():
            print('Correct!')
            answered_correctly += 1
        else:
            print(f'Incorrect! \n the correct answer is {question[1]}')

    print(f'You answered {answered_correctly}/{len(quiz)} correctly!')


start_quiz()

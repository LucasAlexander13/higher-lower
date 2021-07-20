from functions import *

playing = True
score = 0
b = get_movie()

while True:
    while playing:
        a = b
        b = get_movie()
        b = compare(a, b)

        clean()
        higher_or_lower(a, b, score)
        guess = input('Which has the highest metascore? Type \'A\' or \'B\': ').lower()

        if guess == 'a':
            if a['metascore'] > b['metascore']:
                score += 1

            else:
                print('Wrong!')
                print(f'Your final score was: {score}')
                playing = False

        elif guess == 'b':
            if b['metascore'] >= a['metascore']:
                score += 1

            else:
                print('Wrong!')
                print(f'Your final score was: {score}')
                playing = False

    if input('Type \'yes\' to play again: ').lower() == 'yes':
        playing = True
    else:
        break

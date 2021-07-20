from random import randint
from ascii_art import logo, versus
from time import sleep
from dataset import data

def clean():
    '''Cleans the terminal'''
    sleep(1)
    return print("\033c", end='')

def get_movie():
    '''return a dictionary with the data of the movie'''
    return data[randint(0, 50)]

def compare(a, b):
    '''Returns a new value for b if b is equal to a'''
    if a['name'] == b['name']:
        b = randint(0, 50)
        compare(a, b)
    else:
        return b

def higher_or_lower(a, b, score):
    '''Print the core messages of the Higher or Lower game'''
    print(logo)
    print(f'You score is: {score}')
    print(f"Compare A: {a['name']}, from {a['company']}, released in {a['release']}.")
    sleep(1)
    print(versus)
    sleep(1)
    print(f"Against B: {b['name']}, from {b['company']}, released in {b['release']}.")

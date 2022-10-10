import random
from random import randint, choice
from string import ascii_lowercase


def ran_num():
    """This function return random number with range from 100 to 1000"""
    return randint(100, 1000)


def ran_str():
    """This function return random string with range from 5 to 7 symbols"""
    return ''.join(choice(ascii_lowercase) for _ in range(randint(5, 7)))


def emails(names: list, domains: list):
    """This function return generator emails with ran.name+dot+ran.num+at+ran.str+dot+ran.domains"""
    email = random.choice(names) + "." + str(ran_num()) + "@" + str(ran_str()) + "." + random.choice(domains)
    print("(Exercise 8) Generator for emails: ", email)
    return email

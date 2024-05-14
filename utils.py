import random

def get_randon_id():
    return random.randrange(1 << 30, 1 << 31)
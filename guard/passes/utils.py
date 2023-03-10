import random
import string


def create_mfuid():
    population = string.ascii_uppercase + string.digits
    return (
        ''.join(random.choices(population, k=5))
        + '-'
        + ''.join(random.choices(population, k=5))
        + '-'
        + ''.join(random.choices(population, k=8))
    )

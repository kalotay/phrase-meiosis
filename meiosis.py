import random as rn
import string
import hammingdist as hd

#all possible characters
ALPHABET = ' '.join([string.lowercase, string.punctuation])

def fitness(phrase, target):
#fitness of a phrase
#defined as the phrase length minus the Hamming distance to target
    assert len(phrase) == len(target)
    return len(phrase) - hd.hamming_distance(phrase, target)

def mutate(phrase, rate):
#mutates a phrase
#each character has a probability 'rate' of mutation to any random character
    assert 0.0 <= rate <= 1.0
    for c in phrase:
        if rn.random() > rate:
            yield c
        else:
            yield rn.choice(ALPHABET)

def cross_breed(phrase1, phrase2, rate):
#cross between two phrases
#similar to meiosis
#produces two offsprings
    assert len(phrase1) == len(phrase2)
    assert 0.0 <= rate <= 1.0
    crosses = [rn.random() < rate for i in phrase1]
    n_crosses = 0
    for x, y, cross in zip(phrase1, phrase2, crosses):
        n_crosses += cross
        if n_crosses % 2:
            yield x, y
        else:
            yield y, x

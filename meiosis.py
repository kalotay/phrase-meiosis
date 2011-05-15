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
    assert 0.0 <= rate <= 1.0
    for c in phrase:
        if rn.random() > rate:
            yield c
        else:
            yield rn.choice(ALPHABET)

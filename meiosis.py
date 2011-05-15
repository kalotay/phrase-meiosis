import random as rn
import string
import hammingdist as hd

#all possible characters
ALPHABET = ' '.join([string.lowercase, string.punctuation])

def mutate(phrase, rate):
    assert 0.0 <= rate <= 1.0
    for c in phrase:
        if rn.random() > rate:
            yield c
        else:
            yield rn.choice(ALPHABET)
